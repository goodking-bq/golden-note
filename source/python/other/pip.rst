Pip 管理 Python包
---------------------

安装
^^^^^

直接使用 ``easy_install pip`` 就行了，想 pyenv 或是 anconda 环境都自动会装上

配置
^^^^^^

配置文件放在:

- windows下： %USER HOME%\\pip\\pip.ini
- linux下: ~/.pip/pip.conf

如果想使用国内原，可以在配置文件里添加下面内容::

    [global]
    format = columns
    index-url = http://pypi.douban.com/simple
    trusted-host = pypi.douban.com

经常使用
^^^^^^^^^^^^^^^^^^^

* **命令** ::

    Usage:
      pip <command> [options]

    Commands:
      install                     安装需要的包.
      download                    下载包.
      uninstall                   卸载.
      freeze                      生成当前环境的 requirements.
      list                        列出所有已安装的包.
      show                        某个包的详细信息.
      check                       验证已安装的包具有兼容的依赖性.
      search                      搜索某个包.
      wheel                       根据 requirements 创建wheel包.
      hash                        计算软件包档案的哈希.
      completion                  用于命令完成的一个助手命令.
      help                        Show help for commands.

    General Options:
      -h, --help                  Show help.
      --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
      -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
      -V, --version               Show version and exit.
      -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to
                                  WARNING, ERROR, and CRITICAL logging levels).
      --log <path>                Path to a verbose appending log.
      --proxy <proxy>             使用代理 [user:passwd@]proxy.server:port.
      --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
      --timeout <sec>             Set the socket timeout (default 15 seconds).
      --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup,
                                  (a)bort.
      --trusted-host <hostname>   Mark this host as trusted, even though it does not have valid or any HTTPS.
      --cert <path>               Path to alternate CA bundle.
      --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the
                                  certificate in PEM format.
      --cache-dir <dir>           Store the cache data in <dir>.
      --no-cache-dir              Disable the cache.
      --disable-pip-version-check
                                  Don't periodically check PyPI to determine whether a new version of pip is available for
                                  download. Implied with --no-index.

* 关于 **pip install**

    - ``pip install -U packages`` 安装或升级包
    - ``pip install git+<git url>`` 从git上下载并安装包，git上都是最新的。
    - ``pip install -U -r requirements.txt`` 根据requirements安装包
    - ``pip install package.whl`` 安装whl包，由于windows编译环境难安装，所以可以从 `pythonlibs <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ 下载编译好的包安装,比如 mysql-python