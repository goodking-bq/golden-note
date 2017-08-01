#############################################
Sphinx 文档
#############################################

前言
----------------------------------------------
工作越来越久，就越来越觉得写文档是非常重要的，用过几种方式写文档：

* 做过blog，用过WordPress，也自己用python写过一个，维护成本太高了，工作忙的时候完全管不过来，离线的时候不能写。
* 各种云笔记，包括映像笔记，有道笔记，他们总有一定的局限性，在线才能同步文档，并且想导出到其他格式或是其他地方也很不方便，写出来的东西太离散，不能很好的组织目录。
* `gitbook <https://www.gitbook.com/@goodking-bq/dashboard>`_，个人觉得功能不行，markdown格式虽然简单易用易懂。但是对pdf排版特别不好。
* `sphinx <http://www.sphinx-doc.org/en/stable/>`_ + `reStructuredText <http://sphinx-doc-zh.readthedocs.io/en/latest/rest.html>`_  这个正在体验，等我写完这个说不定就喜欢上它了。


安装 Sphinx
-----------------------------------------------

1. 安装Python 环境,windows下需要安装，其他系统都会自带。

2. 安装sphinx ::

    pip install sphinx
3. 执行 sphinx-quickstart 初始化目录 ::

    Welcome to the Sphinx 1.5.1 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Enter the root path for documentation.
    > Root path for the documentation [.]:

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: y

    Inside the root directory, two more directories will be created; "_templates"
    for custom HTML templates and "_static" for custom stylesheets and other static
    files. You can enter another prefix (such as ".") to replace the underscore.
    > Name prefix for templates and static dir [_]:

    The project name will occur in several places in the built documentation.
    > Project name: operation platform
    > Author name(s): golden

    Sphinx has the notion of a "version" and a "release" for the
    software. Each version can have multiple releases. For example, for
    Python the version is something like 2.5 or 3.0, while the release is
    something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
    just set both to the same value.
    > Project version []: 0.1
    > Project release [0.1]:

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    http://sphinx-doc.org/config.html#confval-language.
    > Project language [en]: zh

    The file name suffix for source files. Commonly, this is either ".txt"
    or ".rst".  Only files with this suffix are considered documents.
    > Source file suffix [.rst]:

    One document is special in that it is considered the top node of the
    "contents tree", that is, it is the root of the hierarchical structure
    of the documents. Normally, this is "index", but if your "index"
    document is a custom template, you can also set this to another filename.
    > Name of your master document (without suffix) [index]:

    Sphinx can also add configuration for epub output:
    > Do you want to use the epub builder (y/n) [n]: y

    Please indicate if you want to use one of the following Sphinx extensions:
    > autodoc: automatically insert docstrings from modules (y/n) [n]: y
    > doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
    > intersphinx: link between Sphinx documentation of different projects (y/n) [n]: y
    > todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
    > coverage: checks for documentation coverage (y/n) [n]: y
    > imgmath: include math, rendered as PNG or SVG images (y/n) [n]: y
    > mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
    Note: imgmath and mathjax cannot be enabled at the same time.
    imgmath has been deselected.
    > ifconfig: conditional inclusion of content based on config values (y/n) [n]: y
    > viewcode: include links to the source code of documented Python objects (y/n) [n]: y
    > githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

    A Makefile and a Windows command file can be generated for you so that you
    only have to run e.g. `make html' instead of invoking sphinx-build
    directly.
    > Create Makefile? (y/n) [y]: y
    > Create Windows command file? (y/n) [y]: y

    Creating file .\source\conf.py.
    Creating file .\source\index.rst.
    Creating file .\Makefile.
    Creating file .\make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file .\source\index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
       make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
4. 初始化之后的文档目录::

    -|--source
        |--_static
        |--_templates
        conf.py
        index.rst
     |--build
     |--make.bat
     |--Makefile
5. 执行make.bat 可以把文档编译成各种格式。

.. code-block:: guess

    Sphinx v1.6.3
    Please use `make target' where target is one of
    html        to make standalone HTML files
    dirhtml     to make HTML files named index.html in directories
    singlehtml  to make a single large HTML file
    pickle      to make pickle files
    json        to make JSON files
    htmlhelp    to make HTML files and an HTML help project
    qthelp      to make HTML files and a qthelp project
    devhelp     to make HTML files and a Devhelp project
    epub        to make an epub
    latex       to make LaTeX files, you can set PAPER=a4 or PAPER=letter
    text        to make text files
    man         to make manual pages
    texinfo     to make Texinfo files
    gettext     to make PO message catalogs
    changes     to make an overview of all changed/added/deprecated items
    xml         to make Docutils-native XML files
    pseudoxml   to make pseudoxml-XML files for display purposes
    linkcheck   to check all external links for integrity
    doctest     to run all doctests embedded in the documentation (if enabled)
    coverage    to run coverage check of the documentation (if enabled)

配置
----------------------------------------------------------------
配置文件是放在source目录下面，名字叫 *conf.py*，是个python文件，主要配置是这样的。

.. code-block:: python
    version = 'lastest'
    release = 'lastest'
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme' # 主题设置
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
