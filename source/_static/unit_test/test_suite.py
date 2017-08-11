# coding:utf-8
from __future__ import absolute_import, unicode_literals
import unittest

__author__ = "golden"
__date__ = '2017/8/11'

from .test_case import *


def suite1():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestHash('test_get_all'))
    test_suite.addTest(TestString('test_get_string_is_str'))
    return test_suite


def suite2():
    tests = ['test_get_string_value', 'test_get_string_is_str']
    return unittest.TestSuite(map(TestString, tests))


def all():  # 多个套件还可以构成更大的套件
    _suite1 = suite1()
    _suite2 = suite2()
    return unittest.TestSuite([_suite1, _suite2])
