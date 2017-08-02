reStructuredText 格式说明
*******************************************

  reStructuredText是一种轻量级的文本标记语言，直译为：重构建的文本，为Python中Docutils项目的一部分。其一般保存的文件以.rst为后缀。在必要的时候，.rst文件可以被转化成PDF或者HTML格式，也可以有Sphinx转化为LaTex,man等格式，现在被广泛的用于程序的文档撰写。

标题等级
===========================================

* ``#`` 及上划线表示部分，第一级
* ``*`` 及上划线表示章节，第二级
* ``=`` 及上划线表示小章节，第三级
* ``-`` 及上划线表示子章节，第四级
* ``^`` 及上划线表示子章节的子章节，第五级
* ``"`` 及上划线表示段落，第六级

段落
===================================

  段落(ref)是reST文档中最基本的块。段落是由一个或多个空白行分离的简单的文本块。在Python中，缩进在reST中是具有重要意义，所以同一段落的所有行必须左对齐而且是同一级缩进。

.. _neilianbiaoji:

内联标记
=============================================

rest的内联标记非常丰富，
reST 也允许自定义 “文本解释角色”’, 这意味着可以以特定的方式解释文本. Sphinx以此方式提供语义标记及参考索引，操作符为 ``:rolename:`content```.

.. _my-figure:

.. figure:: plus.png

   自动标签

* ``*text*`` 是强调, *强调*
* ``**text**`` 是重点强调, **重点强调**
* ````text```` 代码样式， ``rm -f /``
* ``:durole:`emphasis``` 也是强调 :emphasis:`强调`
* ``:durole:`strong``` 也是重点强调 :strong:`重点强调`
* ``:durole:`literal``` 也是代码样式， :literal:`代码样式，`
* ``:durole:`subscript`` 这是下标 :subscript:`下标`
* ``:durole:`superscript`` 上标 :superscript:`上标`
* ``:durole:`title-reference``` 书、期刊等材料的标题 :title-reference:`书、期刊等材料的标题`
* ``:ref:`label-name``` 引用,要先用 ``.. _my-reference-label:`` 定义唯一引用名,在标题前引用显示的标题名 ，如  :ref:`neilianbiaoji`
* ``.. _my-figure:.. figure:: whatever 这是显示名字`` 引用 :ref:`my-figure`
* ``:doc:`../people``` 链接到文档 :doc:`quick-start`
* ``:download:`this example script <../example.py>``` 也是强调 :download:`这是一张图片 <plus.png>`
* ``:envvar:`A=B``` 环境变量 , :envvar:`A=B`
* ``:token:`ADFASDFASDFASDFASDF``` 语法名子 , :token:`ADFASDFASDFASDFASDF`
* ``:abbr:`LIFO (last-in, first-out)``` 缩写 , :abbr:`LIFO (last-in, first-out)`
* ``:command:`rm``` 系统级命令 , :command:`rm`
* ``:dfn:`rm``` 在文本中标记术语定义. (不产生索引条目) , :dfn:`rm`
* ``:file:`plus.png``` 文件 , :file:`plus.png`
* ``:kbd:`Control-x Control-f``` 标记键值序列 , :kbd:`Control-x Control-f`
* ``:mailheader:`Content-Type``` RFC 822-样式邮件头的名字 , :mailheader:`Content-Type`
* ``:samp:`print 1+{variable}``` 一块字面量文本 , :samp:`print 1+{variable}`
* ``:regexp:`rm``` 正则表达式 , :regexp:`[1-9]`
* ``:pep:`1#anchor``` 对Python Enhancement Proposal 的参考. 会产生适当的索引条目及文本 “PEP number” ; , :pep:`1#anchor`
* ``:rfc:`1#anchor``` Internet Request for Comments的参考. 也会产生索引条目及文本 “RFC number” ; 在HTML文档里是一个超链接 , :rfc:`1#anchor`
* ``|today|`` 今天的日期 |today|
* ``|version|`` 被项目文档的版本替换. |version|
* ``|release|`` 被项目文档的发布版本替换. |release|

星号及反引号在文本中容易与内联标记符号混淆，可使用反斜杠符号转义.
标记需注意的一些限制:

* 不能相互嵌套,
* 内容前后不能由空白: 这样写``* text*`` 是错误的,
* 如果内容需要特殊字符分隔. 使用反斜杠转义，如: thisis\ *one*\ word.

超链接
=============================================

* 外部链接 使用 ```链接文本 <http://example.com/>`_`` 可以插入网页链接. 链接文本是网址，则不需要特别标记，分析器会自动发现文本里的链接或邮件地址.如  `百度 <http://baidu.com>`_

* 内部链接 详见 :ref:`my-figure`


列表与引用
===============================================

* ``*`` 开始的列表
* 是这样的

1. ``1.`` 这样开始的列表
    这是说明
2. 是这样的
    这是说明

  1. 这是嵌套
  2. 列表
  3. 第三项

#. ``#.`` 开始的是有序列表
#. 是这样的
#. 这样的


term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

 [#]_ is a reference to footnote 1, and [#]_ is a reference to
 footnote 2.

 .. [#] This is footnote 1.
 .. [#] This is footnote 2.
 .. [#] This is footnote 3.

 [#]_ is a reference to footnote 3.

.. _table:

表格
====================================

- 这是比较复杂的表格

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

- 还有一种简单的表格

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

- 另一种简单的表格

.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====

- 列表形式的表格

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

- CSV 表格

.. csv-table:: Frozen Delights!
   :header: "Treat", "Quantity", "Description"
   :widths: 15, 10, 30

   "Albatross", 2.99, "On a stick!"
   "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
   crunchy, now would it?"
   "Gannet Ripple", 1.99, "On a stick!"

块
===============================

块在reStructuredText中的表现方式也有好几种，但是最常见的是文字块(Literal Blocks)。这种块的表达非常简单，就是在前面内容结束之后，用两个冒号" :: "(空格[Optional]，冒号，冒号）来分割，并在之后紧接着插入空行，而后放入块的内容，块内容要相对之前的内容有缩进。

这就是一个块::

  for i in [1,2,3,4,5]:
    print i

  就算空行也不能截断


这是一个普通快.

>>> print 'this is a Doctest block'
this is a Doctest block

这是一个文字块::

    >>> This is not recognized as a doctest block by
    reStructuredText.  It *will* be recognized by the doctest
    module, though!

指令
=========================

指令或者标识符是一个通用的显式标记块。除了roles，指令或者标识符是reST的扩展机制，Sphinx大量地使用了它。使用都是 ``.. 指令::`` 使用

支持如下指令:

- 警告： 支持

  - attention
  - caution
  - danger
  - error
  - hint
  - important
  - note
  - tip
  - warning
  - admonition ， 如：

.. DANGER::

  Beware killer rabbits!

.. note::

    Beware killer rabbits!

- 图片：

  - images 普通图片
  - figure 带标题和可选图例的图片， 如：

.. image:: plus.png
  :name: plus

.. figure:: plus.png
   :scale: 250 %
   :alt: map to buried treasure

- 特色表格 详见 :ref:`table`
- 特色指令

  - raw 包括原生格式标记
  - include 在Sphinx中，当给定一个绝对的文件路径，该指令（标识符）将其作为相对于源目录来处理
  - class class属性赋给下一个元素

.. class:: special

  This is a "special" paragraph.


- HTML 特性

  - meta 生成HTML <meta> 标签
  - title 覆盖文件的标题

- 其他内容元素

  - contents 一个局部的，即只对当前文件的，内容表
  - container 具有特定类的容器，用于HTML 生成 div
  - rubir 一个与文件章节无关的标题
  - topic, sidebar 特别强调了内容元素
  - parsed-literal 支持行内标记的文字块
  - epigraph 带有属性行的块引用
  - highlights, pull-quote 带自己的类属性的块引用
  - compound 组合段落

如：

.. topic:: Topic Title

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

.. sidebar:: Sidebar Title
   :subtitle: Optional Sidebar Subtitle

   Subsequent indented lines comprise
   the body of the sidebar, and are
   interpreted as body elements.

.. line-block::

   Lend us a couple of bob till Thursday.
   I'm absolutely skint.
   But I'm expecting a postal order and I can pay you back
       as soon as it comes.
   Love, Ewan.

.. code:: python

   def my_function():
       "just a test python code"
       print 8/2


.. math::

  α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)


.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.


脚注
=======================================

可以使用 ``[#name]_`` 标注在脚注的位置，在文档的最后的 ``.. rubric:: Footnotes`` 后添加脚注的内容，像这样:

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.


.. This is a comment.
