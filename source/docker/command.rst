Docker 命令
===================

    .. note::

        Docker 版本: ``Docker version 17.06.0-ce, build 02c1d87``

        各个版本命令稍有不同


详细命令::

    Usage:  docker COMMAND

    A self-sufficient runtime for containers

    Options:
          --config string      本地配置文件路径
      -D, --debug              启用调试模式
          --help               打印本帮助文档
      -H, --host list          进程绑定的 socket(s)
      -l, --log-level string   设置日志级别 ("debug"|"info"|"warn"|"error"|"fatal") (默认 "info")
          --tls                连接方式使用 TLS; implied by --tlsverify
          --tlscacert string   Trust certs signed only by this CA (default
                               "C:\Users\golden\.docker\ca.pem")
          --tlscert string     Path to TLS certificate file (default
                               "C:\Users\golden\.docker\cert.pem")
          --tlskey string      Path to TLS key file (default
                               "C:\Users\golden\.docker\key.pem")
          --tlsverify          Use TLS and verify the remote
      -v, --version            版本

    管理命令:
      config      管理设置
      container   管理 containers
      image       管理 images
      network     管理 networks
      node        管理 Swarm nodes
      plugin      管理 plugins
      secret      管理 Docker secrets
      service     管理 services
      stack       管理 Docker stacks
      swarm       管理 Swarm
      system      管理 Docker
      volume      管理 volumes

    Commands:
      attach      重新登录一个正在执行的容器
      build       使用 Dockerfile 生成一个镜像
      commit      在老的镜像基础上创建一个新镜像
      cp          在镜像和本地之间拷贝文件
      create      创建一个新镜像
      diff        比较变化
      events      从服务器拉取个人动态，可选择时间区间。
      exec        在启动的镜像中执行一条命令
      export      将指定的容器保存成 tar 归档文件， docker import 的逆操作。导出后导入（exported-imported)）的容器会丢失所有的提交历史，无法回滚。
      history     查看指定镜像的创建历史。
      images      查看镜像 列表
      import      导入一个镜像
      info        显示 Docker 系统信息，包括镜像和容器数。
      inspect     检查镜像或者容器的参数，默认返回 JSON 格式。
      kill        杀死一个或多个指定容器进程。
      load        从 tar 镜像归档中载入镜像， docker save 的逆操作。保存后再加载（saved-loaded）的镜像不会丢失提交历史和层，可以回滚。
      login       登录一个镜像仓库。
      logout      退出
      logs        获取容器运行时的输出日志。
      pause       暂停某一容器的所有进程。
      port        List port mappings or a specific mapping for the container
      ps          列出所有运行中容器。
      pull        从 Docker Hub 中拉取或者更新指定镜像。
      push        将镜像推送至远程仓库，默认为 Docker Hub 。
      rename      重命名容器
      restart     重启容器
      rm          从本地移除一个或多个指定的镜像。
      rmi         从本地移除一个或多个指定的镜像。
      run         启动一个容器，在其中运行指定命令
      save        将指定镜像保存成 tar 归档文件， docker load 的逆操作。保存后再加载（saved-loaded）的镜像不会丢失提交历史和层，可以回滚。
      search      从 Docker Hub 中搜索符合条件的镜像。
      start       启动停止的容器
      stats       Display a live stream of container(s) resource usage statistics
      stop        停止正在执行的容器
      tag         标记本地镜像，将其归入某一仓库。
      top         查看一个正在运行容器进程，支持 ps 命令参数。
      unpause     恢复某一容器的所有进程。
      update      更新容器配置
      version     版本
      wait        等待容器停止，返回退出码

    Run 'docker COMMAND --help' for more information on a command.

docker build
---------------

* docker build 的命令::

    Usage:	docker build [OPTIONS] PATH | URL | -

    Build an image from a Dockerfile

    Options:
          --add-host list              Add a custom host-to-IP mapping (host:ip)
          --build-arg list             创建镜像是的参数
          --cache-from stringSlice     Images to consider as cache sources
          --cgroup-parent string       Optional parent cgroup for the container
          --compress                   Compress the build context using gzip
          --cpu-period int             限制 CPU CFS周期
          --cpu-quota int              限制 CPU CFS配额
      -c, --cpu-shares int             设置 cpu 使用权重
          --cpuset-cpus string         指定使用的CPU id (0-3, 0,1)
          --cpuset-mems string         指定使用的内存 (0-3, 0,1)
          --disable-content-trust      忽略校验 (default true)
      -f, --file string                指定要使用的Dockerfile路径
          --force-rm                   设置镜像过程中删除中间容器
          --help                       Print usage
          --isolation string           使用容器隔离技术
          --label list                 设置镜像使用的元数据
      -m, --memory bytes               设置内存最大值
          --memory-swap bytes          置Swap的最大值为内存: '-1' 不限制
          --network string             设置网络 (default "default")
          --no-cache                   创建镜像的过程不使用缓存
          --pull                       尝试去更新镜像的新版本
      -q, --quiet                      安静模式，成功后只输出镜像ID
          --rm                         设置镜像成功后删除中间容器(default true)
          --security-opt stringSlice   安全选项
          --shm-size bytes             设置/dev/shm的大小
      -t, --tag list                   指定tag 'name:tag'
          --target string              设置目标镜像
          --ulimit ulimit              Ulimit配置 (default [])

* Dockerfile 创建规则

.. note::

    Dockerfile里的指令是忽略大小写的，一般都是用大写，``#``作为注释，每一行只支持一条指令，每条指令可以携带多个参数。

    指令根据作用可以分为两种:

        - 构建指令 操作不会在运行image的容器上执行
        - 设置指令 操作将在运行image的容器中执行

它的指令有以下这些:

    * ``FROM`` 指定一个基础镜像，可以是任意的镜像

        #. 它一定是首个非注释指令
        #. 可以有多个，创建混合的镜像
        #. 没有指定tag，默认使用 latest
    * ``MAINTAINER`` 指定镜像制作作者的信息
    * ``RUN`` 在当前image中执行任意合法命令并提交执行结果

        #. 没一个 RUN 都是独立运行的
        #. 指令缓存不会在下个命令执行时自动失效
        #. ``RUN <command> (命令用shell执行 - `/bin/sh -c`)``
        #. RUN ["executable", "param1", "param2" ... ]  (使用exec 执行)
    * ``ENV`` 设置容器的环境变量，设置的变量可以用 docker inspect命令来查看
    * ``USER`` 设置运行命令的用户，默认是 ``root``
    * ``WORKDIR``  切换工作目录（默认是 /)，相当于 ``cd``, 对RUN,CMD,ENTRYPOINT生效
    * ``COPY <src> <dest>`` 拷贝文件

        #. 源文件相对被构建的源目录的相对路径
        #. 源文件可以是一个远程的url，并且下下来的文件权限是 600
        #. 所有的新文件和文件夹都会创建UID 和 GID

    * ``ADD <src> <dest>``  从src复制文件到container的dest路径

        #. 源文件相对被构建的源目录的相对路径
        #. 源文件也可以是个url
        #. 如果源文件是可识别的压缩文件，会解压
    * ``VOLUME`` 创建一个可以从本地主机或其他容器挂载的挂载点
    * ``EXPOSE`` 指定在docker允许时指定的端口进行转发

        #. 端口可以有多个
        #. 运行容器的时候要用 -p 指定设置的端口
        #. 如 ``docker run -p expose_port:server_port  image``
    * ``CMD``  设置container启动时执行的操作

        #. 可以是自定义脚本
        #. 也可以是系统命令
        #. 有多个只执行最后一个
        #. 当你使用shell或exec格式时，  CMD 会自动执行这个命令。
        #. ``RUN <command> (命令用shell执行 - `/bin/sh -c`)``
        #. RUN ["executable", "param1", "param2" ... ]  (使用exec 执行)(指定了 ENTRYPOINT 必须用这种)

    * ``ENTRYPOINT`` 设置container启动时执行的操作,和 ``CMD`` 差不多

        #. 如果同时设置了 ``CMD`` 和 ``ENTRYPOINT`` ,并且都是 命令形式， 那最后那个生效
        #. ``CMD`` 和 ``ENTRYPOINT`` 配合使用的话，``ENTRYPOINT`` 和 ``CMD`` 只能是 ``["param"]``形式，``ENTRYPOINT``指定命令,``CMD``指定参数。

    * ``ONBUILD``  在子镜像中执行, 指定的命令在构建镜像时并不执行，而是在它的子镜像中执行。使用情景是在建立镜像时取得最新的源码
    * ``ARG``  定义的变量 只在建立 image 时有效，建立完成后变量就失效消失
    * ``LABEL`` 定义一个 image 标签 Owner，并赋值，其值为变量 Name 的值。(LABEL Owner=$Name )

例子网上一大堆

docker run
--------------

      启动一个容器，在其中运行指定命令。
      -a stdin 指定标准输入输出内容类型，可选 STDIN/
      STDOUT / STDERR 三项；

    * -d 后台运行容器，并返回容器ID；
    * -i 以交互模式运行容器，通常与 -t 同时使用；
    * -t 为容器重新分配一个伪输入终端，通常与 -i 同时使用；
    * --name"nginx-lb" 为容器指定一个名称；
    * --dns 8.8.8.8  指定容器使用的DNS服务器，默认和宿主一致；
    * --dns-search example.com 指定容器DNS搜索域名，默认和宿主一致；
    * -h "mars" 指定容器的hostname；
    * -e username"ritchie" 设置环境变量；
    * --env-file[] 从指定文件读入环境变量；
    * --cpuset"0-2" or --cpuset"0,1,2"
      绑定容器到指定CPU运行；
    * -c 待完成
    * -m 待完成
    * --net"bridge" 指定容器的网络连接类型，支持 bridge /
      host / none
      container:<name|id> 四种类型；
    * --link[] 待完成
    * --expose[] 待完成
