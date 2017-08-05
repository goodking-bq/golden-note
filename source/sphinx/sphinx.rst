Sphinx 标记结构
***************************

TOC树
===========================

由于reST不便于多个文件相互关联或者分割文件到多个输出文件中，Sphinx通过使用自定义的指令（标识符）来处理构成文档的单个文件的关系，这同样使用与内容表。toctree 指令（标识符）就是核心要素。

``.. toctree::`` 该指令（标识符）使用在指令（标识符）主体中给出的文件作为单个TOCs(包含”sub-TOC树”)，在当前位置插入一个”TOC树”

如下::

  .. toctree::
   :maxdepth: 2

   intro
   strings
   datatypes
   numeric
   (many more documents listed here)

*toctree* 有几个选项：
  - maxdepth 文件的内容表被加入的最大的深度
  - numbered 开启章节编号
  - titlesonly 仅显示在树中的文件的标题，而不是其他的同级别的标题
  - glob  所有的条目都将进行匹配而不是直接按照列出的条目，匹配的结果将会按照字母表顺序插入

特殊名称
=============================

#. genindex 总索引
#. modindex python 模块索引
#. search 搜索页
#. 不要创建以 ``_`` 开头的文件或目录


显示代码块
=============================

默认的你可以用 ``::`` 显示代码块，带上没有高亮.
sphinx 代码高亮用的pygments模块。

- ``.. highlight:: language``
- ``.. code-block:: language``

都可以用来显示代码块，但是不知道为什么 highlight会报错：Error in "highlight" directive
支持高亮的语言有（pygments支持的）：

  - none 没有高亮
  - python
  - guess 猜
  - rest
  - c
  - ... 其他pygments支持的语言

如

.. code-block:: python
  :linenos:
  :emphasize-lines: 2,3
  :caption: this.py
  :name: this-py

  def test_error(self, msg):
    print ""self""
    raise Exception(Exception('123'))
    return a

**行号支持**

  - highlight 使用 *linenothreshold* ，超过设置的行数将显示行号
  - code-block 使用 *linenos* ，显示行号
  - code-block 使用 *emphasize-lines* 给的行号高亮

- ``.. literalinclude:: filename`` 显示文件代码

  - language 设置语言
  - emphasize-lines 高亮行号
  - linenos 显示行号
  - encoding 编码
  - pyobject 只包含特定的对象，如Timer.start
  - lines 包含行号
  - diff 对比
  - dedent 缩进


.. literalinclude:: ../conf.py
  :language: python
  :linenos:
