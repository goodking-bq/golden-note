# coding:utf-8

from __future__ import absolute_import, unicode_literals

__author__ = "golden"
__date__ = '2017/8/3'

# !/usr/bin/python
# -*- coding:utf-8 -*-


import wx
import threading
import time
import sys, os
import requests
from bs4 import BeautifulSoup


########################################################################
class SpiderThread(threading.Thread):
    """
        爬虫 线程
    """

    # ----------------------------------------------------------------------
    def __init__(self, category, page_data, current_page, current_item, show_info, set_status_text, lock, name):
        threading.Thread.__init__(self)
        self.category = category
        self.page_data = page_data
        self.current_page = current_page
        self.current_item = current_item
        self.set_status_text = set_status_text
        self.show_info = show_info
        self.lock = lock
        self.name = name

    def run(self):
        self.load_page()

    def get_page(self, page_num):
        wx.CallAfter(self.set_status_text, message='正在加载第 %s 页...' % str(page_num))
        URL = "http://www.qiushibaike.com/" + self.category + "/page/" + str(page_num)
        agent_header = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': agent_header}
        page_content = requests.get(URL, headers=headers).content  # .decode('utf-8').encode('GBK','ignore')
        soup = BeautifulSoup(page_content, "lxml")
        items1 = soup.find_all('div', class_='article')
        item_number = 1
        if not os.path.exists('tmp_jpg'):
            os.makedirs('tmp_jpg')
        if not os.path.exists(r'tmp_jpg/def.jpg'):
            ir = requests.get('http://pic8.nipic.com/20100703/4887831_015505282659_2.jpg')
            open('tmp_jpg/def.jpg', 'wb').write(ir.content)
        for item in items1:
            try:
                myjpg = item.find('div', class_='thumb').find('img')
            except Exception as e:
                myjpg = None
            stats_vote = item.find('span', class_='stats-vote').find('i').get_text()  ####提取好笑个数
            stats_comments = item.find('span', class_='stats-comments').find('i').get_text()  ####提取回复个数
            voting = [span.get_text() for span in item.find_all('span', class_='number hidden')]  ####提取顶、拍个数
            auth = item.find('h2').get_text().strip()
            content = item.find('div', class_='content').find('span').get_text().strip()
            if page_num not in self.page_data.keys():
                self.page_data[page_num] = {}
            self.page_data[page_num].update(
                {item_number: {
                    'auth': auth,
                    'content': content,
                    'stats_vote': stats_vote,
                    'stats_comments': stats_comments,
                    'voting_up': voting[0],
                    'voting_down': voting[1],
                    'jpg': '',
                    'jpg_name': '',
                }})
            if myjpg:
                jpg_name = myjpg['src'].split('/')[-1]
                ir = requests.get(myjpg['src'].replace('//', 'http://'))
                open('tmp_jpg/' + jpg_name, 'wb').write(ir.content)
                self.page_data[page_num][item_number].update({
                    'jpg': myjpg,
                    'jpg_name': jpg_name,
                })
            item_number += 1
            wx.CallAfter(self.set_status_text, message='第 %s 页已加载 %s 条' % (str(page_num), str(item_number)))
        wx.CallAfter(self.show_info, message='第%s页(共%s条)加载完成。' % (str(page_num), str(item_number)))

    def load_page(self):
        while self.lock.isSet():
            if self.page_count < self.current_page + 2:
                try:
                    self.get_page(str(self.page_count + 1))
                    time.sleep(0.1)
                except Exception as ex:
                    msg = u'无法连接糗百：%s' % ex
                    wx.CallAfter(self.set_status_text, message=msg)
                    time.sleep(1)
            else:
                msg = u'加载爬虫休眠中...'
                wx.CallAfter(self.set_status_text, message=msg)
                time.sleep(3)
        wx.CallAfter(self.set_status_text, message='%s 成功退出。' % self.name)

    @property
    def page_count(self):
        return len(self.page_data.keys())


########################################################################
class MyFrame(wx.Frame):
    """
        重构Frame
    """

    # ----------------------------------------------------------------------
    def __init__(self, page_data, current_page, current_item):
        self.page_data = page_data
        self.current_page = current_page
        self.current_item = current_item
        self.current_page_data = {}
        self.current_item_data = {}
        self.category = 'hot'
        self.lock = threading.Event()
        wx.Frame.__init__(self, None, -1, u'我的糗百客户端', size=(600, 720))
        self.create_menu_bar()
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('white')
        self.qbtext = wx.TextCtrl(panel, -1, pos=(100, 10), size=(400, 150),
                                  style=wx.TE_CENTER | wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_NOHIDESEL | wx.TE_RICH2)
        self.stc = wx.StaticText(panel, -1, pos=(150, 0))
        self.stccom = wx.StaticText(panel, -1, pos=(150, 155))
        self.jpgbutton = wx.BitmapButton(panel, -1)
        self.status_bar = self.CreateStatusBar()
        next_button = wx.Button(panel, label=u'下一条', pos=(520, 300), size=(40, 100), style=wx.BU_ALIGN_MASK)
        next_button.Bind(wx.EVT_BUTTON, self.next_item, next_button)
        previous_button = wx.Button(panel, label=u'上一条', pos=(20, 300), size=(40, 100), style=wx.BU_ALIGN_MASK)
        previous_button.Bind(wx.EVT_BUTTON, self.previous_item, previous_button)
        self.jpgbutton.Bind(wx.EVT_BUTTON, self.next_item, self.jpgbutton)
        self.show_info()
        self.Show()

    def show_info(self, message=''):
        self.load_info()
        if self.current_item_data:
            text = self.current_item_data.get('content')
            voting_up = self.current_item_data.get('voting_up')
            voting_down = self.current_item_data.get('voting_down')
            stats_comments = self.current_item_data.get('stats_comments')
            stats_vote = self.current_item_data.get('stats_vote')
            auth = self.current_item_data.get('auth')
        else:
            text = '正在加载中...'
            voting_up = 0
            voting_down = 0
            stats_comments = 0
            stats_vote = 0
            auth = ''
        self.qbtext.SetLabel(text)
        self.stc.SetLabel(
            u'第 ' + str(self.current_page) + u' 页 第 ' + str(self.current_item) + u' 条 作者：' + auth)
        self.stccom.SetLabel(
            u'%s个顶  %s个拍  %s个评论  %s个好笑' % (voting_up, voting_down, stats_comments, stats_vote))
        self.jpgbutton.SetBitmap(self.jpg)
        self.jpgbutton.SetPosition(self.jpg_pose)
        self.jpgbutton.SetSize(self.jpg_size)

    def set_status_text(self, message):
        if not self.status_bar.GetStatusText() == message:
            self.status_bar.SetStatusText(message)

    def next_item(self, event):
        if self.current_page_item_count > self.current_item:
            self.current_item += 1
        else:
            self.current_page += 1
            self.current_item = 1
            if str(self.current_page) in self.page_data:
                self.current_page_data = self.page_data[str(self.current_page)]
        self.show_info()

    @property
    def current_page_item_count(self):
        return len(self.current_page_data.keys())

    def previous_item(self, event):
        if self.current_item > 1:  # 当前页面大于1,到当前页前一条
            self.current_item -= 1
        else:  # 到前一页最后一条
            if self.current_page > 1:  # 有前一页
                self.current_page -= 1
                self.current_page_data = self.page_data[str(self.current_page)]
                self.current_item = max(self.current_page_data.keys())
            else:
                self.set_status_text(u'前面没有页了')
        self.show_info()

    def load_info(self):
        if not self.current_page_data:
            self.current_page_data = self.page_data.get(str(self.current_page), {})
        if self.current_item in self.current_page_data.keys():
            self.current_item_data = self.current_page_data[self.current_item]
            if self.current_item_data.get('jpg'):
                jpg_path = 'tmp_jpg/' + self.current_item_data.get('jpg_name')
                jpg = wx.Image(jpg_path, type=wx.BITMAP_TYPE_JPEG)
                W, H = jpg.GetWidth(), jpg.GetHeight()
                if (W > 400 and H <= 500) or (W > H and W > 400 and H > 500):
                    H = 400 * H / W
                    W = 400
                elif (W <= 400 and H > 500) or (400 < W < H and H > 500):
                    W = 500 * W / H
                    H = 500
                self.jpg_pose = (300 - W / 2, 420 - H / 2)
                self.jpg_size = (W, H)
                self.jpg = jpg.Rescale(W, H).ConvertToBitmap()
            else:
                jpg_path = 'tmp_jpg/def.jpg'
                self.jpg_pose = (150, 270)
                self.jpg_size = (301, 300)
                self.jpg = wx.Image(jpg_path, type=wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        else:
            jpg_path = 'tmp_jpg/def.jpg'
            self.jpg_pose = (150, 270)
            self.jpg_size = (301, 300)
            self.jpg = wx.Image(jpg_path, type=wx.BITMAP_TYPE_JPEG).ConvertToBitmap()

    def create_menu_bar(self):
        menu_bar = wx.MenuBar()
        for each in self.menu_data:
            menu_label = each[0]
            menu_item = each[1:]
            menu_bar.Append(self.create_menu(menu_item), menu_label)
        self.SetMenuBar(menu_bar)
        return menu_bar

    def create_menu(self, menu_data):
        menu = wx.Menu()
        kind = wx.ITEM_NORMAL
        for _data in menu_data:
            if len(_data) == 3:
                label, status, handler = _data
            else:
                label, status, handler, kind = _data
            if not label:
                menu.AppendSeparator()
                continue
            menu_item = menu.Append(-1, label, status, kind)
            self.Bind(wx.EVT_MENU, handler, menu_item)
        return menu

    def set_category(self, event):
        categorys = {
            '8hr': '热门',
            'hot': '24小时',
            'imgrank': '热图',
            'text': '文字',
            'history': '穿越',
            'pic': '糗图',
            'textnew': '新鲜'
        }
        categorys = {categorys[key]: key for key in categorys}
        menu_bar = self.GetMenuBar()
        item_id = event.GetId()
        item = menu_bar.FindItemById(item_id)
        category = categorys.get(item.GetLabel())
        self.category = category
        self.page_data = {}
        self.current_page_data = {}
        self.current_item_data = {}
        self.current_page = 1
        self.current_page = 1
        self.show_info()
        self.stop_spider()
        self.start_spider()

    def defa(self):
        pass

    @property
    def menu_data(self):
        return (
            (u"文件",
             (u"新建", u"新建窗口", self.defa),
             (u'关闭', u'关闭当前窗口', self.defa)),
            (u'编辑',
             (u'复制', u'复制结果到剪切板', self.defa),
             (u'粘贴', u'粘贴剪切板内容到输入框', self.defa),
             (u'清空剪切板', u'清空剪切板', self.defa),
             ('', '', ''),
             (u'选项', u'选项', self.defa)),
            (u'分类',
             (u'热门', u'热门', self.set_category, wx.ITEM_RADIO),
             (u'24小时', u'24小时', self.set_category, wx.ITEM_RADIO),
             (u'热图', u'热图', self.set_category, wx.ITEM_RADIO),
             (u'文字', u'文字', self.set_category, wx.ITEM_RADIO),
             (u'穿越', u'穿越', self.set_category, wx.ITEM_RADIO),
             (u'糗图', u'糗图', self.set_category, wx.ITEM_RADIO),
             (u'新鲜', u'新鲜', self.set_category, wx.ITEM_RADIO)),
            (u'帮助',
             (u'关于', u'关于', self.defa))

        )


        ########################################################################

    def start_spider(self):
        self.lock.set()
        sp = SpiderThread(self.category, self.page_data, self.current_page, self.current_item, self.show_info,
                          self.set_status_text, lock=self.lock, name=self.category)
        sp.setDaemon(1)
        sp.start()
        self.spider_thread = sp
        self.set_status_text('%s 爬虫启动。' % self.category)

    def stop_spider(self):
        self.lock.clear()
        while True:
            if self.spider_thread.is_alive():
                time.sleep(1)
            else:
                self.set_status_text('%s 爬虫成功退出' % self.category)
                break


class MyApp(wx.App):
    """
    重构APP
    """

    # ----------------------------------------------------------------------
    def __init__(self, page_data, current_page, current_item):
        """Constructor"""
        wx.App.__init__(self)
        frame = MyFrame(page_data, current_page, current_item)
        frame.start_spider()
        frame.Center()
        frame.Show()
        self.page_data = page_data
        self.current_page = current_page
        self.current_item = current_item
        self.frame = frame

    def MainLoop(self):
        return super(MyApp, self).MainLoop()


########################################################################


if __name__ == '__main__':
    page_data = {}  # 数据
    current_page = 1  # 当前页数,从1开始
    current_item = 1  # 当前条数,从1开始
    app = MyApp(page_data, current_page, current_item)
    app.MainLoop()
