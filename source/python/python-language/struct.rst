struct 包
----------------------

基本概念
^^^^^^^^^^^^

.. note::

    对python基本类型值与用python字符串格式表示的C struct类型间的转化。

    多用于存取文件，或是socket数据交换时使用。

    它的类型对照表

.. csv-table::
    :widths: 20,40,40,40
    :header: "格式","C 语言类型","python 类型","字节数"

    "x","填充字节","no value","1"
    "c","char","string of length 1","1"
    "b","signed char","integer","1"
    "B","unsigned char","integer","1"
    "?","_Bool","bool","1"
    "h","short","integer","2"
    "H","unsigned short","integer","2"
    "i","int","int","4"
    "I","unsigned int","integer or long","4"
    "l","long","integer","4"
    "L","unsigned long","long","4"
    "q","long long","long","8"
    "Q","unsigned long long","long","8"
    "f","float","float","4"
    "d","double","float","8"
    "s","char[]","string","1"
    "p","char[]","string","1"
    "P","void *","long",""

.. hint::

    - 每个格式前面可以有个数字，表示个数
    - s与p, s表示一定格式的字符串，但是p表示的是pascal字符串
    - P用来转换一个指针，其长度和机器字长相关


对齐方式:

.. csv-table::
    :widths: 20,30,30,40
    :header: "Character","Byte order","Size","Alignment"

    "@(默认)","本机","本机","本机，凑够4个字节"
    "=","本机","标准","none,按原字节数"
    "<","小端","标准","none,按原字节数"
    ">","大端","标准","none,按原字节数"
    "!","network(大端)","标准","none,按原字节数"

.. hint::

    - 小端：较高的有效字节存放在较高的存储器地址中，较低的有效字节存放在较低的存储器地址，符合计算机处理
    - 大断：较低的有效字节存放在较高的存储器地址中，较高的有效字节存放在较低的存储器地址，符合人类正常思维逻辑

使用
^^^^^^

- calcsize: 计算格式的字节长度

    >>> struct.calcsize('>IH') # I 4个 H 2个 总共6个
    6

- pack 和 unpack

    pack 将python类型转换成C 二进制

    unpack 则是反过来，将二进制转换成python类型

    >>> struct.pack('<iHs',2,3,'e.w/'.encode())
    b'\x02\x00\x00\x00\x03\x00e'
    >>> struct.pack('<iH3s',22,3,'e.w/'.encode()) # 前面可以跟数字
    b'\x16\x00\x00\x00\x03\x00e.w'
    >>> struct.pack('<2i',22,3)
    b'\x16\x00\x00\x00\x03\x00\x00\x00'
    >>> struct.pack('>2i',22,3) # 大端 和小端 的区别
    b'\x00\x00\x00\x16\x00\x00\x00\x03'
    >>> struct.unpack('>2i',b'\x00\x00\x00\x16\x00\x00\x00\x03') #转换成python数据
    (22, 3)

- pack_into 和 unpack_from

