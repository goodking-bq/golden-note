Sqlalchemy 查询
----------------

sqlachemy的查询是非常强大，越是强大的东西越是复杂。 查询是通过 session 的 query() 实现。它可以接受任何数量的任何类和描述符的组合。

这里也只有一些常用的，需要更详细的，查看 `官方文档 Query <http://docs.sqlalchemy.org/en/latest/orm/query.html>`_

query的 参数控制返回
^^^^^^^^^^^^^^^^^^^^

    - 如果跟的是模型类，那返回的就是这个这个类的实例或是列表。如::

        session.query(User)

    - 如果都给了表字段，那结果是元祖列表,如::

        session.query(User.name, User.fullname)

    - 如果同时给了模型类和表字段，那返回的是named tuples,如::

        session.query(User, User.name)

    - 你可以 label 方法控制列返回的名称。如::

        session.query(User.name.label('name_label'))

    - 你可以用aliased方法控制类返回的名称，如::

        session.query(aliased(User, name='user_alias'))

    - 可以用 limit,offset来控制返回的条数。如::

        session.query(User).limit(10)，
        session.query(User).offset(1,20) # offset跟list的切片效果类似。

    - 过滤数据使用 filter_by,filter

        - filter_by 参数为关键字参数，这种过滤功能有限 如::

            filter_by(id=1)

        - filter 的参数是更像python的操作符，过滤功能很强大,如::

            filter(User.id.in_([1,2])``

    - 可以有多个过滤，也就是可以多个filter或是filter_by连着写。如::

        session.query(User).filter(type=1).filter_by(User.id.in_([1,2,3]))

filter - 基本的操作符
^^^^^^^^^^^^^^^^^^^^^^^

数据过滤是通过filter来实现的，支持数据库里所有的操作符。

* 等于::

    query.filter(User.name == 'ed')

* 不等于::

    query.filter(User.name != 'ed')

* like::

    query.filter(User.name.like('%ed'))

* in::

    query.filter(User.id.in_([1,2,3]))

* not in::

    query.filter(User.id.notin_([1,2,3]))

* is NULL::

    query.filter(User.name == None)
    query.filter(User.name.is_(None))

* is not NULL::

    query.filter(User.name != None)
    query.filter(User.name.isnot(None))

* and::

    from sqlalchemy import and_

    query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
    query.filter(User.name == 'ed', User.fullname == 'Ed Jones')
    query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')

* or::

    from sqlalchemy import or_
    query.filter(or_(User.name == 'ed', User.name == 'wendy'))

* match or contains::

    query.filter(User.name.match('wendy'))

order_by - 排序
^^^^^^^^^^^^^^^^^^^^^

    - 很简单的排序::

        query.filter(User.name.match('wendy')).order_by(User.id)
        query.filter(User.name.match('wendy')).order_by('id desc')

group_by - 分组
^^^^^^^^^^^^^^^^^^^^^

    .. hint::

        SQL 的 group by 语句用于结合合计函数，根据一个或多个列对结果集进行分组。

        多和统计函数一起使用，如 count（计数）,sum（求和）,avg（平均）

- 下面统计每个user_id 有多少个地址::

    from sqlalchemy import func
    query(Address.user_id, func.count('*')).group_by(Address.user_id)

- having 过滤统计数据，必须和 ``goup_by`` 一起使用，下面返回了user 地址大于1的user::

    from sqlalchemy import func
    query(Address.user_id, func.count('*')).group_by(Address.user_id).having(func.count('*'))

text - 直接写sql
^^^^^^^^^^^^^^^^^^^^

* 在text里写sql语句，并在 ``filter`` 和 ``order_by`` 中使用。看了下面几个例子就知道了::

    from sqlalchemy import text
    session.query(User).filter(text("id<224")).order_by(text("id")).all()

* text里可以用 ``:name`` 传动态参数，并params传值，如::

    session.query(User).filter(text("id<:value and name=:name")). \
        params(value=224, name='fred').order_by(User.id).one()

* text里也可以给完整的sql语句,然后传给 ``from_statement`` 如下面这样匹配所有的列::

    session.query(User).from_statement(text("SELECT * FROM user where name=:name")). \
        params(name='ed').all()

* 如果用from_statement中不是给的所有字段，那可用 columns 将值赋给字段，如::

    stmt = text("SELECT name, id, fullname, password FROM users where name=:name")
    stmt = stmt.columns(User.name, User.id, User.fullname, User.password)
    session.query(User).from_statement(stmt).params(name='ed').all()

JOIN or OUTER JOIN - 更精简，效率更高
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    多张表联合查询的时候，可以这样写::

        session.query(User, Address).filter(User.id==Address.user_id).\
                        filter(Address.email_address=='jack@google.com').\
                        all()

    但是用 ``join`` 则更好

        - 有外键关联::

            session.query(User).join(Address).\
                filter(Address.email_address=='jack@google.com').all()

        - 没有外键,则需要手动添加 join 关系::

            session.query(User).join(Address,User.id==Address.user_id).\
                filter(Address.email_address=='jack@google.com').all()

Aliases - 别名
^^^^^^^^^^^^^^^^^^^

    别名可以在这样的情况下使用::

        from sqlalchemy.orm import aliased
        adalias1 = aliased(Address) # 定义别名
        adalias2 = aliased(Address) # 定义别名
        for username, email1, email2 in \
            session.query(User.name, adalias1.email_address, adalias2.email_address).\
            join(adalias1, User.addresses).\
            join(adalias2, User.addresses).\
            filter(adalias1.email_address=='jack@google.com').\
            filter(adalias2.email_address=='j25@yahoo.com'):
            print(username, email1, email2)

Subqueries - 子查询
^^^^^^^^^^^^^^^^^^^^^^^

    要实现下面的sql::

        SELECT users.*, adr_count.address_count FROM users LEFT OUTER JOIN
           (SELECT user_id, count(*) AS address_count
               FROM addresses GROUP BY user_id) AS adr_count
           ON users.id=adr_count.user_id

    就需要用到子查询了::

        from sqlalchemy.sql import func
        stmt = session.query(Address.user_id, func.count('*').\
                label('address_count')).\
                group_by(Address.user_id).subquery()  #定义子查询
        session.query(User, stmt.c.address_count).\
            outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id) # 这样使用

exists - 高效的子查询
^^^^^^^^^^^^^^^^^^^^^^^^^

.. hint::

    EXISTS用于检查子查询是否至少会返回一行数据，该子查询实际上并不返回任何数据，而是返回值True或False

那怎么在 Sqlalchemy 写出 exists的 sql呢？

* 直接使用 ``exists()`` 方法::

    from sqlalchemy.sql import exists
    stmt = exists().where(Address.user_id==User.id)
    session.query(User.name).filter(stmt)

* 使用 ``any()`` 方法，用于 **一对多/多对多** 关系，可在前面加 ``~`` 号表示 ``not exists``::

    session.query(User.name).filter(User.addresses.any(Address.email_address.like('%google%')))

* 使用 ``has()`` 方法，用于 **多对一**，同样可在前面加 ``~`` 号表示 ``not exists``::

    session.query(Address).filter(~Address.user.has(User.name=='jack')).all()

* 使用 ``contains()`` 方法，用于 **一对多** 关系::

    session.query.filter(User.addresses.contains(someaddress_object))

* 使用 ``with_parent()`` 方法，可用于 **任何关系**

    session.query(Address).with_parent(someuser, 'addresses')

subqueryload - 子查询加载
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. hint::

    当查询的表有关联的表时，它是关联的表的字段缓一步加载，也就是分两次查询一个query的数据，多和 first() limit() offset() order_by() 一起使用。

这对于数据量大的表来说很有用::

    session.query(User).\
                options(subqueryload(User.addresses)).\
                filter_by(name='jack').one()

返回结果大小控制
^^^^^^^^^^^^^^^^^^^

- all() 返回所有
- first() 查询并返回第一条,没有数据为空
- one() 查询所有并严格返回一条数据，如果查询到多条数据或没有数据，都会报错
- one_or_none 同 one，没有数据会返回None，不会报错，其他一样。
- scalar 同 one，但是只返回那条数据的第一个字段。