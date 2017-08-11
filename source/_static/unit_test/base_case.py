# coding:utf-8
from __future__ import absolute_import, unicode_literals
import unittest
import redis

__author__ = "golden"
__date__ = '2017/8/11'


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.redis = redis.StrictRedis(host='192.168.137.3', db=6)

    def tearDown(self):
        self.redis.flushdb()  # 清空
