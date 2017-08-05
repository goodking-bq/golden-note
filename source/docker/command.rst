命令详解
***************************

* ``docker version``

     显示 Docker 版本信息。

* ``docker info``

    显示 Docker 系统信息，包括镜像和容器数。

* ``docker search``

    从 Docker Hub 中搜索符合条件的镜像。

* ``docker pull``

    从 Docker Hub 中拉取或者更新指定镜像。

* ``docker login``

    按步骤输入在 Docker Hub 注册的用户名、密码和邮箱即可完成登录。

* ``docker logout``

    运行后从指定服务器登出，默认为官方服务器。

* ``docker images``

    列出本地所有镜像。其中 [name] 对镜像名称进行关键词查询。

* ``docker ps``

    列出所有运行中容器。

* ``docker rmi``

    从本地移除一个或多个指定的镜像。

* ``docker rm``

    *  -f 强行移除该容器，即使其正在运行；
    *  -l 移除容器间的网络连接，而非容器本身；
    *  -v 移除与容器关联的空间。

* ``docker history``

    查看指定镜像的创建历史。

* ``docker start|stop|restart``

    启动、停止和重启一个或多个指定容器。

* ``docker kill``

    杀死一个或多个指定容器进程。

* ``docker events``

    从服务器拉取个人动态，可选择时间区间。

* ``docker save``

    将指定镜像保存成 tar 归档文件， docker load 的逆操作。保存后再加载（saved-loaded）的镜像不会丢失提交历史和层，可以回滚。

* ``docker load``

    从 tar 镜像归档中载入镜像， docker save 的逆操作。保存后再加载（saved-loaded）的镜像不会丢失提交历史和层，可以回滚。

* ``docker export``

    将指定的容器保存成 tar 归档文件， docker import 的逆操作。导出后导入（exported-imported)）的容器会丢失所有的提交历史，无法回滚。

* ``docker import``

    从归档文件（支持远程文件）创建一个镜像， export 的逆操作，可为导入镜像打上标签。导出后导入（exported-imported)）的容器会丢失所有的提交历史，无法回滚。

* ``docker top``

    查看一个正在运行容器进程，支持 ps 命令参数。

* ``docker inspect``

    检查镜像或者容器的参数，默认返回 JSON 格式。

* ``docker pause``

    暂停某一容器的所有进程。

* ``docker unpause``

    恢复某一容器的所有进程。

* ``docker tag``

    标记本地镜像，将其归入某一仓库。

* ``docker push``

    将镜像推送至远程仓库，默认为 Docker Hub 。

* ``docker logs``

      获取容器运行时的输出日志。

* ``docker run``

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
