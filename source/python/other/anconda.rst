anconda 一个好用 python 发行版
------

Anaconda 是一个用于科学计算的 Python 发行版，支持 Linux, Mac, Windows, 包含了众多流行的科学计算、数据分析的 Python 包。

最好的是 他自带 ``python 多版本管理器, 可以支持多 python 版本同时存在或切换，并且同时支持所有系统。`` 是python 版本管理利器。

安装
^^^^

安装很简单，去 `官网 <https://www.continuum.io/downloads>`_ 下载就行没什么难度。

配置
^^^^

它的配置文件：

    - Windows 放在 C:\\Users\\username\\.condarc
    - Linux 放在 ~/.condarc
    - 如果没有可自建

如果你想使用国内原 可以修改配置文件 ::

    channels:
     - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
     - defaults
    show_channel_urls: yes

或是执行命令::

    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --set show_channel_urls yes

国内原下载非常快

使用
^^^^^^^^^^

* **命令** ::

    usage: conda [-h] [-V] command ...

    conda is a tool for managing and deploying applications, environments and packages.

    Options:

    positional arguments:
      command
        info         显示当前conda环境的新信息.
        help         Displays a list of available conda commands and their help
                     strings.
        list         列出当前环境的所有包.
        search       搜索包.
        create       创建一个环境.
        install      当前环境安装包.
        update       更新包，也可以更新当前环境的python版本.
        upgrade      同update.
        remove       删除包.
        uninstall    同remove.
        config       配置 conda
        clean        Remove unused packages and caches.
        package      Low-level conda package utility. (EXPERIMENTAL)

    optional arguments:
      -h, --help     Show this help message and exit.
      -V, --version  Show the conda version number and exit.

    other commands, such as "conda build", are available when additional conda
    packages (e.g. conda-build) are installed

* **常用命令**

    - ``conda info -e`` 列出所有的虚拟环境
    - ``conda create -n py2.7 python=2.7`` 安装一个名为 py2.7的环境，python 版本为2.7的最新版
    - ``conda update --all`` 将所有包升级到最新版
    - ``activate py2.7`` 切换环境到 py2.7
    - ``deactivate`` 退出当前虚拟环境

