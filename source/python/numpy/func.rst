numpy 强大的函数库
--------------

随机函数
^^^^^^^^^^^^^^^^^^^

    .. csv-table:: 随机函数
        :widths: 20,40,40
        :header: "函数名","功能","参数实例"

        "rand","0~1之间的随机浮点数","rand(2,3)"
        "randn","标准正太分布的随机数","rand(4,3)"
        "randint","指定范围内的随机数","randint(2,5,(5,4)) # 范围和形状"
        "normal","正态分布","normal(100,10,(5,4)) # 期望值 标准差 形状"
        "uniform","均匀分布","uniform(10,20,(4,3)) #起始值 终止值 形状"
        "poisson","泊松分布","poisson(2.0,(4,3)) # 系数"
        "permutation","随机分布","permutation(10 or a) #返回的新数组"
        "shuffle","随机打乱顺序","shuffle(a), # 将输入的数组顺序打乱"
        "choice","随机抽取", "choice(a,size=(3,3),p=a/np.sum(a)) #p 指定抽取元素的概率，表示越大，抽取概率也越大"
        "seed","设置随机数种子","可以保证每次运行是得到相同的随机数"

求和 平均值 方差
^^^^^^^^^^^^^

    .. csv-table:: 函数
        :widths: 20,40,40
        :header: "函数名","功能","参数实例"

        "sum","求和","sum(a,axis=1) # axis 对哪个轴求和，返回列表 keepdims参数指定是否保持原来的维数"
        "mean","求期望"
        "average","加权平均数"
        "std","标准差"
        "var","方差"
        "product","连乘积"

大小和排序
^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. csv-table:: 大小和排序函数
        :widths: 20,40,40
        :header: "函数名","功能","参数实例"

        "min","最小值",""
        "max","最大值",""
        "minimum","二元最小值",""
        "maximum","二元最大值",""
        "ptp","最小值最大值之差",""
        "argmin","最小值下标",""
        "argmax","最大值下标",""
        "unravel_index","一维下标转换成多维下标",""
        "sort","数组排序",""
        "argsort","计算数组排序的下标",""
        "lexsort","多列排序",""
        "partition","快速计算前K位",""
        "argpartition","前k位下标",""
        "media","中位数",""
        "percentile","百分中位数",""
        "searchsorted","二分查找",""

统计函数
^^^^^^^^^^^^^^

    .. csv-table:: 统计函数
        :widths: 20,40,40
        :header: "函数名","功能","参数实例"

        "unique","去除重复元素",""
        "bincount","对整数数组的元素计数",""
        "histogram","一维直方图统计"
        "digitze","离散化"

分段函数
^^^^^^^^^^^^^^^^^^^^^^

    .. csv-table:: 分段函数
        :widths: 20,40,40
        :header: "函数名","功能","参数实例"

        "where","矢量化判断表达式","where(x>1,x*2,x*3) # 如果>1 ,x*2 否则 x*3"
        "piecewise","分段函数","piecewise(x,[x>1,x<1],[lambda x: x*x,lambda x: x*2,0]) # x>1=x*x x<1=x*2,else 0"
        "select","多分支判断选择",

操作多维数组
^^^^^^^^^^^^^^^^^

    .. csv-table:: 操作多维数组的函数
        :widths: 20,40,40
        :header: "函数名","功能","参数实例"

        "concatenate","连接多个数组",""
        "vstack","延0轴连接数组",""
        "hstack","延1轴连接数组",""
        "column_stack","按列连接多个一维数组",""
        "split,array_split","将数组分为多段",""
        "transpose","重新设置轴的顺序",""
        "swapaxes","交换两个轴的顺序",""

    例：

        >>> a=np.arange(3)
        >>> a
        array([0, 1, 2])
        >>> b=np.arange(10,13)
        >>> b
        array([10, 11, 12])
        >>> np.vstack((a,b))
        array([[ 0,  1,  2],
               [10, 11, 12]])
        >>> np.hstack((a,b))
        array([ 0,  1,  2, 10, 11, 12])
        >>> np.column_stack((a,b))
        array([[ 0, 10],
               [ 1, 11],
               [ 2, 12]])
        >>> c=np.random.randint(1,19,(1,2,3,4))
        >>> c.shape
        (1, 2, 3, 4)
        >>> np.transpose(c,(2,1,0,3)).shape
        (3, 2, 1, 4)
        >>> np.swapaxes(c,2,3).shape
        (1, 2, 4, 3)