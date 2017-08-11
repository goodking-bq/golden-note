unittest 使用
----------------

.. note::

    unittest 是python 最常用的单元测试框架.支持自动化测试,测试代码共享启动和关闭代码，集合测试以等。有几个概念:

    #. test fixture: 开始测试前所作的工作，一般使用setUp()和tearDown()函数完成。
    #. test case: 测试案例，最小的测试单元
    #. test suite: 测试套件，测试案例的集合
    #. test runner： 运行测试

    命名方法：

    * 测试类 以 ``Test`` 开头
    * 测试方法 以 ``test`` 开头

    测试要用到 ``assert`` 断言语法

    python assert 断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。

test fixture
^^^^^^^^^^^^^^^^^^^^

测试开始和结束的准备工作，一般用于创建和关闭数据库连接，开始或停止一个进程等, 如果是一系列测试需要相同的准备和结束工作，那建议写一个基类定义它们，具体测试在继承它

只需要定义下面两个函数:

* ``setUp`` 开始前的准备
* ``和tearDown`` 结束后的操作

例:

:file:`base_case.py`

.. literalinclude:: ../../_static/unit_test/base_case.py
    :language: python
    :linenos:
    :pyobject: BaseTestCase
    :caption: base_case.py

test case
^^^^^^^^^^^^^^^^^

通过继承 ``unittest.TestCase`` 或是自己的 ``unittest.TestCase`` 基类，就可以创建测试单元，测试方法 都是以 ``test``开头。

如:

.. literalinclude:: ../../_static/unit_test/test_case.py
    :language: python
    :linenos:
    :caption: test_case.py

最后目录结构为：

    unit_test :
       | __init__.py
       | base_case.py
       | test_case.py
       | test_suite.py

要执行测试，可以在命令行执行命令： :command:`python -m unittest unit_test.case` 得到下面结果::

    > python -m unittest unit_test.test
    {b'key1': b'value1', b'key2': b'value2'}
    ...F # 成功三个，失败一个
    ======================================================================
    FAIL: test_get_string_value (unit_test.test.TestString)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "D:\operation-platform\source\_static\unit_test\test.py", line 22, in test_get_string_value
        assert self.redis.get('test_string') == 'python'
    AssertionError

    ----------------------------------------------------------------------
    Ran 4 tests in 0.016s

    FAILED (failures=1) # 失败一个

test suite
^^^^^^^^^^^^^^^^^^^^^^^

测试套件是测试单元的集合，构建测试套件需要用到 ``unittest.TestSuite()`` 类,我们一般写成一个方法，如：

.. literalinclude:: ../../_static/unit_test/test_suite.py
    :language: python
    :linenos:
    :caption: test_suite.py

运行命令 :command:`python -m unittest unit_test.test_suite.suite1` 结果如下::

    > python -m unittest unit_test.test_suite.suite1
    {b'key2': b'value2', b'key1': b'value1'}
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.009s # 只运行了两个测试

    OK

跳过测试和预期的失败
^^^^^^^^^^^^^^^^^^^^^^^^

由几个装饰器来控制：

    - ``@unittest.skip(reason)`` 由什么原因跳过测试
    - ``@unittest.skipIf(condition, reason)`` 满足 condition 条件时跳过
    - ``@unittest.skipUnless(condition, reason)`` 不满足 条件时跳过
    - ``@unittest.expectedFailure`` 如果失败 ，不包含在失败结果中
    - ``exception unittest.SkipTest(reason)`` 报错错误
    - 装饰器都可以用于方法或类

提供的其他测试方法
^^^^^^^^^^^^^^^^^^

还有一些其他的测试方法，如:

* assertEqual(a, b)	a == b
* assertNotEqual(a, b)	a != b
* assertTrue(x)	bool(x) is True
* assertFalse(x)	bool(x) is False
* assertIs(a, b)	a is b	3.1
* assertIsNot(a, b)	a is not b	3.1
* assertIsNone(x)	x is None	3.1
* assertIsNotNone(x)	x is not None	3.1
* assertIn(a, b)	a in b	3.1
* assertNotIn(a, b)	a not in b	3.1
* assertIsInstance(a, b)	isinstance(a, b)	3.2
* assertNotIsInstance(a, b)	not isinstance(a, b)	3.2

详见 `其他 <https://docs.python.org/dev/library/unittest.html#unittest.TestCase.debug>`_

生成 HTML 的测试报告
^^^^^^^^^^^^^^^^^^^^

详见 `HTMLTestRunner <https://pypi.python.org/pypi/HTMLTestRunner/0.8.0>`_