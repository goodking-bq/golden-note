什么是numpy
--------------

    numpy(Numerical Python extensions)是一个第三方的Python包，用于科学计算。这个库的前身是1995年就开始开发的一个用于数组运算的库。经过了长时间的发展，基本上成了绝大部分Python科学计算的基础包，当然也包括所有提供Python接口的深度学习框架。

支持的数据类型
---------------------

    - ``bool`` 用一位存储的布尔类型（值为TRUE或FALSE）
    - ``inti`` 由所在平台决定其精度的整数（一般为int32或int64）
    - ``int8`` 整数，范围为 -128至127
    - ``int16`` 整数，范围为 -2**16至32767
    - ``int32`` 整数，范围为 -2**31至2**31-1
    - ``int64`` 整数，范围为 -2**64至2**64-1
    - ``uint8`` 无符号整数，范围为0至255
    - ``uint16`` 无符号整数，范围为0至 65 535
    - ``uint32`` 无符号整数，范围为0至 2**32-1
    - ``uint64`` 无符号整数，范围为0至 2**64-1
    - ``float16`` 半精度浮点数（16位）：其中用1位表示正负号，5位表示指数，10位表示尾数
    - ``float32`` 单精度浮点数（32位）：其中用1位表示正负号，8位表示指数，23位表示尾数
    - ``float64`` 或 ``float`` 双精度浮点数（64位）：其中用1位表示正负号，11位表示指数，52位表示尾数
    - ``complex64`` 复数，分别用两个32位浮点数表示实部和虚部
    - ``complex128`` 或 ``complex`` 复数，分别用两个64位浮点数表示实部和虚部

array 核心模块
---------------

.. note::

    array - 由多个元素类型组成的数组。数组中所有元素的类型必须是相同的，要么是上面说的基本类型，要么是列表。
    数组中有两个概念：

    - axes(轴)   就是每个元素类型的长度
    - rank(秩)   他是轴的个数，也叫组维度

    如一个二维数组 array([[1,2,3],[3,4,5]]),他的秩 为2 ，轴为3,

创建数组
^^^^^^^^^^^^^^^^^^^

    >>> import numpy as np
    >>> a=np.array([1,2,3,4]) # 一维数组
    >>> b=np.array([[1,2,3],['a','b','c']]) # 二维数组
    >>> a.shape # shape属性只有一个元素，所以是一维数组
    (4,)
    >>> b.shape # shape属性有两个元素，所以是二维数组，0轴长度为2,1轴长度为3
    (2, 3)
    >>> np.arange(1,5,1) # 自动生成 开始，结束，步长
    array([1, 2, 3, 4])
    >>> np.linspace(1,5,5) # 等差数列 开始，结束，个数
    array([ 1.,  2.,  3.,  4.,  5.])
    >>> np.logspace(0,2,5) # 等比数列
    array([   1.        ,    3.16227766,   10.        ,   31.6227766 ,  100.        ])
    >>> np.empty((3,4),np.int) # 只分配空间，不初始化操作，速度最快。注意，没有初始化
    array([[1739692720,        517, 1787770920,        517],
       [1787772000,        517, 1787543216,        517],
       [1787543088,        517, 1788022832,        517]])
    >>> np.zeros((2,2)) # 初始化为0
    array([[ 0.,  0.],
       [ 0.,  0.]])
    >>> np.ones(2) #初始化 1
    array([ 1.,  1.])
    >>> np.fromstring(b'abcde',dtype=np.int8) # 从字符串生成 ，取得ASCII编码值
    array([ 97,  98,  99, 100, 101], dtype=int8)
    >>> np.fromfunction(lambda x,y:x+y+1,(2,2)) # 从方法生成
    array([[ 1.,  2.],
       [ 2.,  3.]])


存取元素
^^^^^^^^^^^^^^^^

#. 一维数组

    .. note::

        一维数组大致上和列表相同

        >>> a=np.arange(10)
        >>> a
        array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        >>> a[5] # 一维数组存取同  list
        5
        >>> a[1:-1:2] # 第三个参数表示步长
        array([1, 3, 5, 7])
        >>> a[::-1] # 步长1 负数表示顺序颠倒
        array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        >>> a[1,2]=100,200 #可以改变
        array([  0, 100, 200,   3,   4,   5,   6,   7,   8,   9])
        >>> b=a[3:6] # b与a使用相同的地址，改一个两个都改
        >>> a[[2,4,-1]] #
        array([200,   4,   9])
        >>> x=np.arange(10,1,-1)
        >>> x[np.array([3,3,1,8])] #array 取数据
        array([7, 7, 9, 2])
        >>> x[[3,3,1,8,3,3,3,3]].reshape(2,4)
        array([[7, 7, 9, 2],
           [7, 7, 7, 7]])

#. 多维数据

    .. note::

        多维数组需要两个点才能确定一个元素

        >>> a=np.array([[1,2,3,4,5],[22,32,42,52,62],[33,43,53,63,73]])
        >>> a[2,3] or a[(2,3)] # 第三列 第4个元素
        63
        >>> a[1:,[0,2,4]] # 1: 选取的是1行之后的所有行，[0,2,4] 选取的是行的第 0,2,4 个元素
        array([[22, 42, 62],
           [33, 53, 73]])

#. 结构数组

    .. note::

        numpy.dtype 很容易定义结构数组

        >>> person=np.dtype({'names':['name','age'],'formats':['S30','i']},align=True)
        >>> persons=np.array([(b'zhang san',22),(b'li si',23),(b'wang er',44)],dtype=person)
        >>> persons.dtype # 类型
        {'names':['name','age'], 'formats':['S30','<i4'], 'offsets':[0,32], 'itemsize':36, 'aligned':True}
        >>> persons.shape # 这里为什么不是3,2
        (3,)
        >>> persons[2] # 原来是这样
        (b'wang er', 44)
        >>> persons[2]['name'] # 取姓名
        b'wang er'
        >>> persons.flags # 一些属性
          C_CONTIGUOUS : True # 数据存储区域是否是 C 语言格式的连续区域
          F_CONTIGUOUS : True # 数据存储区域是否是 Fortran 语言格式的连续区域
          OWNDATA : True # 数组是否拥有次数据存储区域，当一个数组是其他数组视图时为False
          WRITEABLE : True # 可写
          ALIGNED : True # 对齐
          UPDATEIFCOPY : False # 复制时更新
        >>> persons.strides # 每个轴上相邻元素的地址差
        (36,)
        >>> persons.T # 转置
        [(b'zhang san', 22) (b'li si', 23) (b'wang er', 44)] # 一维没变
        >>> persons.T.flags
          C_CONTIGUOUS : True
          F_CONTIGUOUS : True
          OWNDATA : False #
          WRITEABLE : True
          ALIGNED : True
          UPDATEIFCOPY : False

ufunc 函数
^^^^^^^^^^^^^^^^

ufunc 是 universal function 的缩写，他是一种对数组的每个元素进行运算的函数，都是用C所写，速度非常快。

#. 四则运算

    .. csv-table:: 四则运算对应的 ufunc 函数
       :header: "四则运算表达式", "对应的 ufunc 函数"
       :widths: 20, 40

       "y = x1 + x2", "add(x1, x2)"
       "y = x1 - x2", "subtract(x1, x2)"
       "y = x1 * x2", "multiply(x1, x2)"
       "y = x1 / x2", "divide(x1, x2) , 如果是都是整数，用整数除法。"
       "y = x1 / x2", "true_divide(x1, x2) , 总是返回精确的商"
       "y = x1 // x2", "floor_divide(x1, x2) , 总是对返回值取整"
       "y = -x1", "negative(x1, x2)"
       "y = x1 ** x2", "power(x1, x2)"
       "y = x1 % x2", "remainder(x1, x2) , mode(x1, x2)"

    例：

        >>> a=np.arange(1,20)
        >>> b=np.arange(0,19)
        >>> c=a+b
        >>> a
        array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
        >>> b
        array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        >>> c
        array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37])


#. 比较运算和布尔运算

    .. csv-table:: 比较运算与对应的 ufunc 函数
        :header: "比较运算表达式", "对应的 ufunc 函数"
        :widths: 20, 40

        "x1 == x2", "equal(x1, x2)"
        "x1 != x2", "not_equal(x1, x2)"
        "x1 < x2", "less(x1, x2)"
        "x1 <= x2", "less_equal(x1, x2)"
        "x1 > x2", "greater(x1, x2)"
        "x1 >= x2", "greater_equal(x1, x2)"
        "x1 and x2", "logical_and(x1, x2) # x1 and x2 会报错"
        "x1 or x2", "logical_or(x1, x2)"
        "not x2", "logical_not(x2)"
        "","any(x1) , x1 任何一个为True,返回True"
        "","all(x1) , x1 全部为True,返回True"
        "x1 & x2 , 按位与", "between_and(x1, x2)"
        "x1 | x2 , 按位或", "between_or(x1, x2)"
        "x1 ^ x2 , 按位亦或", "between_xor(x1, x2)"
        "~x2 , 按位非", "between_not(x1)"

    例:

        >>> ~np.arange(5)
        array([-1, -2, -3, -4, -5], dtype=int32)
        >>>~np.arange(5,dtype=np.uint8)
        array([255, 254, 253, 252, 251], dtype=uint8)

#. 自定义 ufunc

    可以用 `frompyfunc()`, `vectorize()` 来把普通的对单个运算的方法转成 ufunc 方法。vectorize 可以通过otypes指定返回元素类型

    例：

    .. code::

        import numpy as np

        p_type = np.dtype({'names': ['name', 'age', 'sex'],
                           'formats': ['S30', 'i', 'S1']}, align=True)
        a = np.array([('golden', 30, 'b'), ('gg', 20, 'g')], dtype=p_type)


        def gender_cn(a):
            b = list(a)
            if a[2] == b'b':
                return 1
            elif a[2] == b'g':
                return 2
            else:
                return 0


        f1 = np.frompyfunc(gender_cn, 1, 1)
        f2 = np.vectorize(gender_cn, otypes=[np.bool])
        f1(a) # np.array([1, 2])
        f2(a) # np.array([True,True])

#. 广播

    .. tip::

        **当使用ufunc时，如果两个数组的形状不同，会做如下处理：**

        - 让所有输入数组都向其中维数最多的看齐，shape熟悉中不足的部分通过在前面加1补齐
        - 输出输入的shape属性是输入数组的shape属性的各个轴上的最大值
        - 如果输入数组的某个轴的长度为1或输出数组的对应轴长度相同，这个数组能够用来计算，否则报错。
        - 当输入数组的某个轴的长度为1时，沿着此轴运算是用此轴上的第一组值

    .. code::

        a = np.array([1,2,3,4]) # a.shape = (4,)
        b = np.array([[1],[2],[3],[4],[5]]) # b.shape = (5, 1)
        c = a + b
        # c： [[2 3 4 5]
        #      [3 4 5 6]
        #      [4 5 6 7]
        #      [5 6 7 8]
        #      [6 7 8 9]]
        # c.shape = (5, 4)
        # a + b 得到一个加法表，得到一个形状为 (5, 4) 数组

    .. note::

        - 由于 a, b 的维数不同，根据规则，需要在让a的shape像b对齐，于是在a的shape前加1，变成 *(1, 4)*
        - 这样 两个做加法运算的shape 属性为 *(1, 4), (5, 1)*, 根据规则，输出数组的shape是输入的各个轴上的最大值，所以结果形状是  (5, 4)
        - 由于 a 的0轴长度为1，而b的0轴长度为5，所以需要将a的0轴长度扩展为5，相当于 a.shape=1,4 a=a.repeat(5, axis=0),所以a最后变成了array([[1, 2, 3, 4], [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]])
        - 由于 b 的 1周长度为1，而a的1轴长度为4,为了相加，相当于 b=b.repeat(4,axis=1),变为 array([[1, 1, 1, 1],[2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4],[5, 5, 5, 5]])
        - 最后相加得到结果。当然真正的过程不是这样，这样耗内存。

    `ogrid` 专门用于创建广播运算的数组

        x, y = np.ogrid[:5,:7] # x=array([[0],[1],[2],[3],[4]]) y=array([[0, 1, 2, 3, 4, 5, 6]])

    `mgrid` 与 `ogrid` 类似，但是返回的是广播之后的数组

