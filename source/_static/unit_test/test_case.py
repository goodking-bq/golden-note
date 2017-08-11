# coding:utf-8
from __future__ import absolute_import, unicode_literals
import unittest
from .base_case import BaseTestCase

__author__ = "golden"
__date__ = '2017/8/11'


class TestString(BaseTestCase):
    def setUp(self):
        super(TestString, self).setUp()
        self.redis.set('test_string', 'python')

    def test_get_string_is_str(self):
        assert not isinstance(self.redis.get('test_string'), str)

    def test_get_string_is_bytes(self):
        assert isinstance(self.redis.get('test_string'), bytes)

    def test_get_string_value(self):
        assert self.redis.get('test_string') == 'python'


class TestHash(BaseTestCase):
    def setUp(self):
        super(TestHash, self).setUp()
        self.redis.hset('test_hash', 'key1', 'value1')
        self.redis.hset('test_hash', 'key2', 'value2')

    def test_get_all(self):
        res = self.redis.hgetall('test_hash')
        print(res)
        assert isinstance(res, dict)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestString)
    unittest.main(defaultTest=suite)
