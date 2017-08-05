# coding:utf-8
from __future__ import absolute_import, unicode_literals
import wx
import math

'''
Created on 2014年7月8日

@author: golden
'''


class CalculatorFrame(wx.Frame):
    def __init__(self, parent, _id, size, pos, option):
        wx.Frame.__init__(self, parent, _id, u'我的计算器', size=size, pos=pos)
        self.StatusBar = self.CreateStatusBar()
        self.create_menu_bar()
        self.option = option
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('white')
        self.set_button(panel)
        self.txt_box = wx.TextCtrl(panel, -1, "", pos=(20, 30), size=(340, 30), style=wx.ALIGN_RIGHT)
        self.txt_box.SetForegroundColour('blue')
        wx.StaticText(panel, -1, u"输入:", pos=(10, 10))
        self.txt_box1 = wx.TextCtrl(panel, -1, "", pos=(20, 80), size=(340, 30), style=wx.ALIGN_RIGHT)
        wx.StaticText(panel, -1, u"输出:", pos=(10, 60))

    def set_button(self, panel):
        i = 0
        if self.option == u'高级':
            for value, name, x_size, y_size, handle in self.high_button_vau:
                x, y = 1, 1
                x, y = x + i // 5, y + i % 5
                pos = (20 + (y - 1) * 70, 120 + (x - 1) * 50)
                size = (x_size, y_size)
                i += 1
                self.create_button(panel, label=value, pos=pos, size=size, handle=handle, name=name)
        elif self.option == u'初级':
            for value, name, x_size, y_size, handle in self.simple_button_value:
                x, y = 1, 1  # x: 列  y: 行
                x, y = x + i // 5, y + i % 5
                pos = (20 + (y - 1) * 70, 120 + (x - 1) * 50)
                size = (x_size, y_size)
                i += 1
                self.create_button(panel, label=value, pos=pos, size=size, handle=handle, name=name)
        elif self.option == u'中级':
            for value, name, x_size, y_size, handle in self.middle_button_vau:
                x, y = 1, 1
                x, y = x + i // 5, y + i % 5
                pos = (20 + (y - 1) * 70, 120 + (x - 1) * 50)
                size = (x_size, y_size)
                i += 1
                self.create_button(panel, label=value, pos=pos, size=size, handle=handle, name=name)
        else:
            print('版本选择错误')

    def create_button(self, panel, label, pos, size, handle, name):
        button = wx.Button(panel, label=label, pos=pos, size=size, name=name)
        button.SetForegroundColour('blue')
        button.Bind(wx.EVT_BUTTON, handle, button)
        button.Bind(wx.EVT_ENTER_WINDOW, self.on_enter_window, button)
        button.Bind(wx.EVT_LEAVE_WINDOW, self.on_enter_window, button)

    def create_menu_bar(self):
        menu_bar = wx.MenuBar()
        for menu in self.menu_data:
            menu_label = menu[0]
            menu_item = menu[1:]
            menu_bar.Append(self.create_menu(menu_item), menu_label)
        self.SetMenuBar(menu_bar)
        return menu_bar

    def create_menu(self, menu_data):
        menu = wx.Menu()
        for eachLabel, eachStatus, eachHandler in menu_data:
            if not eachLabel:
                menu.AppendSeparator()
                continue
            menu_item = menu.Append(-1, eachLabel, eachStatus)
            self.Bind(wx.EVT_MENU, eachHandler, menu_item)
        return menu

    def on_click(self, event):
        self.txt_box.SetValue(self.txt_box.GetValue() + event.GetEventObject().GetLabel())

    def del_click(self, event):
        self.txt_box.SetForegroundColour('Default')
        val = self.txt_box.GetValue()
        self.txt_box.SetValue(val[:-1])
        self.txt_box1.SetValue('')

    def clear_click(self, event):
        self.txt_box1.SetForegroundColour('Default')
        self.txt_box.SetValue('')
        self.txt_box1.SetValue('')

    def equ_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(eval(self.txt_box.GetValue())))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def suq_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.pow(eval(self.txt_box.GetValue()), 2)))
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def suqt_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.pow(eval(self.txt_box.GetValue()), 1.0 / 2)))
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def suq3_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.pow(eval(self.txt_box.GetValue()), 3)))
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def suqt3_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.pow(eval(self.txt_box.GetValue()), 1.0 / 3)))
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def acos_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.acos(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def acosh_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.acosh(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def asin_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.asin(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def atan_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.atan(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def atan2_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.atan2(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def atanh_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.atanh(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def cos_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.cos(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def cosh_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.cosh(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def sin_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.sin(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def tan_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.tan(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def tanh_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.tanh(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def degrees_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.degrees(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def radians_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.radians(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def log10_click(self, event):
        try:
            self.txt_box1.SetForegroundColour('Default')
            self.txt_box1.SetValue(str(math.log10(eval(self.txt_box.GetValue()))))
        except ZeroDivisionError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'除数为0，请重新输入！')
        except SyntaxError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入算式错误，请重新输入！')
        except ValueError:
            self.txt_box1.SetForegroundColour('red')
            self.txt_box1.SetValue(u'输入值错误，不能运算，请重新输入！')

    def pi_click(self, event):
        self.txt_box.SetValue(self.txt_box.GetValue() + event.GetEventObject().GetLabel())
        self.txt_box1.SetValue(str(math.pi))

    def e_click(self, event):
        self.txt_box.SetValue(self.txt_box.GetValue() + event.GetEventObject().GetLabel())
        self.txt_box1.SetValue(str(math.e))

    def on_close_me(self, event):
        self.dlg = wx.MessageDialog(None, u'确定关闭？', u'消息框(MessageDialog)', wx.YES_NO | wx.ICON_WARNING)
        if (self.dlg.ShowModal() == wx.ID_NO):
            self.dlg.Destroy()
        else:
            self.Destroy()

    def copy_click(self, event):
        if wx.TheClipboard.Open():
            data_obj = wx.TextDataObject()
            data_obj.SetText(self.txt_box1.GetValue())
            wx.TheClipboard.SetData(data_obj)
        else:
            wx.MessageBox(u"不能打开剪切板", u"Error")

    def paste_click(self, event):
        self.txt_box.Paste()

    @staticmethod
    def clear_clipboard(event):
        if wx.TheClipboard.Open():
            wx.TheClipboard.Flush()
            wx.TheClipboard.Close()
        else:
            wx.MessageBox(u"不能打开剪切板", "Error")

    @staticmethod
    def about_me_click(event):
        wx.MessageBox(u'计算器版本1.0', u"关于", wx.OK | wx.ICON_INFORMATION)

    def set_click(self, event):
        ob = event.GetEventObject()
        opt = ob.GetLabel(event.GetId())
        self.chang_win(opt)

    def option_click(self, event):
        dlg = wx.SingleChoiceDialog(None, u'选择计算器', u'选项', [u'初级', u'中级', u'高级'])
        if dlg.ShowModal() == wx.ID_OK:
            opt = dlg.GetStringSelection()
            self.chang_win(opt)
        else:
            dlg.Destroy()

    @property
    def menu_data(self):
        return (
            (u"文件",
             (u"新建", u"新建窗口", self.new_win),
             (u'关闭', u'关闭当前窗口', self.on_close_me)),
            (u'编辑',
             (u'复制', u'复制结果到剪切板', self.copy_click),
             (u'粘贴', u'粘贴剪切板内容到输入框', self.paste_click),
             (u'清空剪切板', u'清空剪切板', self.clear_clipboard),
             ('', '', ''),
             (u'选项', u'选项', self.option_click)),
            (u'设置',
             (u'初级', u'初级', self.set_click),
             (u'中级', u'中级', self.set_click),
             (u'高级', u'高级', self.set_click)),
            (u'帮助',
             (u'关于', u'关于', self.about_me_click))
        )

    @property
    def high_button_vau(self):
        x_size = 60
        y_size = 40
        return (
            (u'1', u'数字1', x_size, y_size, self.on_click),
            (u'2', u'数字2', x_size, y_size, self.on_click),
            (u'3', u'数字3', x_size, y_size, self.on_click),
            (u'+', u'加法(正)', x_size, y_size, self.on_click),
            (u'-', u'减肥(负)', x_size, y_size, self.on_click),

            (u'4', u'数字4', x_size, y_size, self.on_click),
            (u'5', u'数字5', x_size, y_size, self.on_click),
            (u'6', u'数字6', x_size, y_size, self.on_click),
            (u'*', u'乘法', x_size, y_size, self.on_click),
            (u'/', u'除法', x_size, y_size, self.on_click),

            (u'7', u'数字7', x_size, y_size, self.on_click),
            (u'8', u'数字8', x_size, y_size, self.on_click),
            (u'9', u'数字9', x_size, y_size, self.on_click),
            (u'(', u'左括号', x_size, y_size, self.on_click),
            (u')', u'右括号', x_size, y_size, self.on_click),

            (u'0', u'数字0', x_size, y_size, self.on_click),
            (u'.', u'点号', x_size, y_size, self.on_click),
            (u'=', u'等号', x_size, y_size, self.equ_click),
            (u'clear', u'清除', x_size, y_size, self.clear_click),
            (u'del', u'删除', x_size, y_size, self.del_click),

            (u'^2', u'平方', x_size, y_size, self.suq_click),
            (u'2√', u'平方根', x_size, y_size, self.suqt_click),
            (u'3√', u'根三', x_size, y_size, self.suqt3_click),
            (u'e', u'自然常数', x_size, y_size, self.e_click),
            (u'π', u'圆周率', x_size, y_size, self.pi_click),

            (u'|', u'按位或', x_size, y_size, self.on_click),
            (u'~', u'按位取反', x_size, y_size, self.on_click),
            (u'&amp;', u'按位与', x_size, y_size, self.on_click),
            (u'&lt;&lt;', u'向左移', x_size, y_size, self.on_click),
            (u'&gt;&gt;', u'向右移', x_size, y_size, self.on_click),

            (u'^', u'按位异或', x_size, y_size, self.on_click),
            (u'acos', u'反余弦', x_size, y_size, self.acos_click),
            (u'acosh', u'反双曲余弦', x_size, y_size, self.acosh_click),
            (u'asin', u'反正弦', x_size, y_size, self.asin_click),
            (u'atan', u'反正切', x_size, y_size, self.atan_click),

            (u'atan2', u'反正切', x_size, y_size, self.atan2_click),
            (u'atanh', u'反双曲正弦', x_size, y_size, self.atanh_click),
            (u'cos', u'余弦', x_size, y_size, self.cos_click),
            (u'cosh', u'双曲余弦', x_size, y_size, self.cosh_click),
            (u'sin', u'正弦', x_size, y_size, self.sin_click),

            (u'tan', u'正切', x_size, y_size, self.tan_click),
            (u'tanh', u'双曲正切', x_size, y_size, self.tanh_click),
            (u'degrees', u'將 x (弧长) 转成角度', x_size, y_size, self.degrees_click),
            (u'radians', u'將 x(角度) 转成弧长', x_size, y_size, self.radians_click),
            (u'log10', u'log10', x_size, y_size, self.log10_click)
        )

    @property
    def simple_button_value(self):
        x_size = 60
        y_size = 40
        return ((u'1', u'数字1', x_size, y_size, self.on_click),
                (u'2', u'数字2', x_size, y_size, self.on_click),
                (u'3', u'数字3', x_size, y_size, self.on_click),
                (u'+', u'加法(正)', x_size, y_size, self.on_click),
                (u'-', u'减肥(负)', x_size, y_size, self.on_click),

                (u'4', u'数字4', x_size, y_size, self.on_click),
                (u'5', u'数字5', x_size, y_size, self.on_click),
                (u'6', u'数字6', x_size, y_size, self.on_click),
                (u'*', u'乘法', x_size, y_size, self.on_click),
                (u'/', u'除法', x_size, y_size, self.on_click),

                (u'7', u'数字7', x_size, y_size, self.on_click),
                (u'8', u'数字8', x_size, y_size, self.on_click),
                (u'9', u'数字9', x_size, y_size, self.on_click),
                (u'(', u'左括号', x_size, y_size, self.on_click),
                (u')', u'右括号', x_size, y_size, self.on_click),

                (u'0', u'数字0', x_size, y_size, self.on_click),
                (u'.', u'点号', x_size, y_size, self.on_click),
                (u'=', u'等号', x_size, y_size, self.equ_click),
                (u'clear', u'清除', x_size, y_size, self.clear_click),
                (u'del', u'删除', x_size, y_size, self.del_click))

    @property
    def middle_button_vau(self):
        x_size = 60
        y_size = 40
        return ((u'1', u'数字1', x_size, y_size, self.on_click),
                (u'2', u'数字2', x_size, y_size, self.on_click),
                (u'3', u'数字3', x_size, y_size, self.on_click),
                (u'+', u'加法(正)', x_size, y_size, self.on_click),
                (u'-', u'减肥(负)', x_size, y_size, self.on_click),

                (u'4', u'数字4', x_size, y_size, self.on_click),
                (u'5', u'数字5', x_size, y_size, self.on_click),
                (u'6', u'数字6', x_size, y_size, self.on_click),
                (u'*', u'乘法', x_size, y_size, self.on_click),
                (u'/', u'除法', x_size, y_size, self.on_click),

                (u'7', u'数字7', x_size, y_size, self.on_click),
                (u'8', u'数字8', x_size, y_size, self.on_click),
                (u'9', u'数字9', x_size, y_size, self.on_click),
                (u'(', u'左括号', x_size, y_size, self.on_click),
                (u')', u'右括号', x_size, y_size, self.on_click),

                (u'0', u'数字0', x_size, y_size, self.on_click),
                (u'.', u'点号', x_size, y_size, self.on_click),
                (u'=', u'等号', x_size, y_size, self.equ_click),
                (u'clear', u'清除', x_size, y_size, self.clear_click),
                (u'del', u'删除', x_size, y_size, self.del_click),

                (u'sin', u'正弦', x_size, y_size, self.sin_click),
                (u'cos', u'余弦', x_size, y_size, self.cos_click),
                (u'tan', u'正切', x_size, y_size, self.tan_click),
                (u'e', u'自然常数', x_size, y_size, self.e_click),
                (u'π', u'圆周率', x_size, y_size, self.pi_click),
                )

    @property
    def win_size(self):
        return ((u'初级', 400, 410),
                (u'中级', 400, 510),
                (u'高级', 400, 670),
                )

    def on_enter_window(self, event):
        ob = event.GetEventObject()
        ob.SetForegroundColour('red')
        ob.SetBackgroundColour('white')
        self.StatusBar.SetBackgroundColour('grey')
        self.StatusBar.SetStatusText(ob.GetName())
        event.Skip()

    def on_leave_window(self, event):
        ob = event.GetEventObject()
        ob.SetForegroundColour('blue')
        ob.SetBackgroundColour('Default')
        self.StatusBar.SetBackgroundColour('Default')
        self.StatusBar.SetStatusText('')
        event.Skip()

    def new_win(self, event):
        self.Destroy()
        app = wx.App(redirect=False)
        frame = CalculatorFrame(parent=None, _id=-1, size=(400, 620), pos=(100, 100), option=option)
        frame.Show()
        app.MainLoop()

    def chang_win(self, opt):
        self.Destroy()
        for _opt, x_size, y_size in self.win_size:
            size = (x_size, y_size)
            if _opt == opt:
                app = wx.App(redirect=False)
                frame = CalculatorFrame(parent=None, _id=-1, size=size, pos=(100, 50), option=opt)
                frame.Show()
                app.MainLoop()


if __name__ == "__main__":
    app = wx.App(redirect=False)
    option = u'初级'
    frame = CalculatorFrame(parent=None, _id=-1, size=(400, 410), pos=(100, 50), option=option)
    frame.Show()
    app.MainLoop()
    app.Destroy()
