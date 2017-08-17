windows10 上使用 docker
==========================

安装
------------------

#. 安装最新版的windows10(必须64位)
#. 开启hyper-v windows自己的虚拟机程序。
#. `InstallDocker.msi <https://download.docker.com/win/stable/InstallDocker.msi>`_ 下载此文件,并安装
#. 打开命令行，运行 docker 命令，检查是否安装成功。

设置
-----------------

#. Advanced里面可以设置docker使用的cpu个数和内存大小，如果启动的时候提示内存不足，可适当的调小内存。
#. 网络和代理也是一看就懂。
#. Docker Deamon 里可以编辑它的配置，如添加个仓库::

    {
      "registry-mirrors": [
        "daocloud.io"
      ],
      "insecure-registries": [],
      "debug": false
    }

