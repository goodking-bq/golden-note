表的继承
------------------

当我们有多个 *Model* 的结构都很相似的时候，我们就希望模型也能像python对象一样能够继承，这个 Sqlalchemy 是完全支持的。

**下面所有例子都是用 flask-sqlalchemy 来完成的。与纯粹的sqlalchemy差别不大**

当然继承也有多种方式，完全能够满足需求。

Joined Table Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

这种继承通过外键方式将基表和继承表相关联，这种继承的特点:

    * 基类会在数据库建一张表，拥有基类的所有字段
    * 继承的类也会在数据库建表，拥有继承的类的字段
    * 继承类的数据会在两个表里面存放，它们的 ID 相同
    * 继承类拥有基类的所有方法
    * 查询基类会自动返回继承类的对象

具体的做法是：

    - 基类的 __mapper_args__ 需要配置下面两个参数
        - polymorphic_identity 表示是基类数据的类别，字符串就可以
        - polymorphic_on 类别字段的名称
    - 继承的类需要配置__mapper_args__的参数
        - polymorphic_identity 表示是数据的类别

一个例子：

.. code-block:: python

    class Animal(db.Model):
    """动物基类"""
    __tablename__ = 'animal' # 会创建animal 表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(20))
    __mapper_args__ = {
        'polymorphic_identity': 'animal',
        'polymorphic_on': type
    }


    class Cat(Animal):
        """爬行动物"""
        __tablename__ = 'cat' # 会创建 cat 表
        id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key=True)
        cat_name = db.Column(db.String(255))
        __mapper_args__ = {
            'polymorphic_identity': 'cat',
        }

    class Dog(Animal):
        """爬行动物"""
        __tablename__ = 'dog' # 会创建dog 表
        id = db.Column(db.Integer, db.ForeignKey('animal.id'), primary_key=True)
        dog_name = db.Column(db.String(255))
        __mapper_args__ = {
            'polymorphic_identity': 'dog',
        }

测试数据::

    >>> a=models.Animal()
    >>> a.name='animal1'
    >>> db.session.add(a)
    >>> c=models.Cat()
    >>> c.name='animal2'
    >>> c.cat_name='cat1'
    >>> db.session.add(c)
    >>> d=models.Dog()
    >>> d.cat_name='dog1'
    >>> d.name='animal3'
    >>> db.session.add(d)
    >>> db.session.commit()

执行完之后，数据库的数据是这样的。

.. list-table:: Animal Table
    :widths: 10 20 20
    :header-rows: 1

    *   - id
        - name
        - type
    *   - 1
        - animal1
        - animal
    *   - 2
        - animal2
        - cat
    *   - 3
        - animal3
        - dog


.. list-table:: Cat Table
    :widths: 10 20
    :header-rows: 1

    *   - id
        - cat_name
    *   - 2
        - cat1


.. list-table:: Dog Table
    :widths: 10 20
    :header-rows: 1

    *   - id
        - dog_name
    *   - 3
        - dog1

Single Table Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

这种继承类是不会体现在具体表中，其特点：

    - 只会创建基类表，一张表
    - 拥有基类和继承类的所有字段
    - 继承类拥有基类的所有字段

具体做法：

    * 基类的 __mapper_args__ 需要配置下面两个参数
        - polymorphic_identity 表示是基类数据的类别，字符串就可以
        - polymorphic_on 类别字段的名称
    * 继承类需要配置__mapper_args__的参数：
        - polymorphic_identity 表示是数据的类别
    * 继承类不能加 __tablename__ 属性，否则会报错

例子：

.. code-block:: python

    class Animal(db.Model):
    """动物基类"""
    __tablename__ = 'animal' # 会创建animal 表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(20))
    __mapper_args__ = {
        'polymorphic_identity': 'animal',
        'polymorphic_on': type
    }


    class Cat(Animal):
        """爬行动物"""
        cat_name = db.Column(db.String(255))
        __mapper_args__ = {
            'polymorphic_identity': 'cat',
        }

    class Dog(Animal):
        """爬行动物"""
        dog_name = db.Column(db.String(255))
        __mapper_args__ = {
            'polymorphic_identity': 'dog',
        }

同样的测试语句::

    >>> a=models.Animal()
    >>> a.name='animal1'
    >>> db.session.add(a)
    >>> c=models.Cat()
    >>> c.name='animal2'
    >>> c.cat_name='cat1'
    >>> db.session.add(c)
    >>> d=models.Dog()
    >>> d.cat_name='dog1'
    >>> d.name='animal3'
    >>> db.session.add(d)
    >>> db.session.commit()

数据库的数据：

.. list-table:: Animal Table2
    :widths: 10 20 20 20 20
    :header-rows: 1

    *   - id
        - name
        - type
        - cat_name
        - dog_name
    *   - 1
        - animal1
        - animal
        - NULL
        - NULL
    *   - 2
        - animal2
        - cat
        - cat1
        - NULL
    *   - 3
        - animal3
        - dog
        - NULL
        - dog1

Concrete Table Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

这种继承只是语言上的继承，数据层不会有任何的关系，特点：

    - 继承表会有基类的所有字段
    - 基类的方法继承类不会继承
    - 基类建表与否都没有关系
    - 继承表之间也没有关系

具体做法：

#. 使用 *mapper.concrete* 参数

    .. warning::

        这种的话查询基类的时候是不会查询到继承类的。

    * 基类不需要特殊设置
    * 继承类需要在 __mapper_args__ 添加下面参数

        - concrete 设置为 ``True``

    一个例子::

        class Employee(db.Model):
            __tablename__ = 'employee'

            id = Column(Integer, primary_key=True)
            name = Column(String(50))

        class Manager(Employee):
            __tablename__ = 'manager'

            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            manager_data = Column(String(50))

            __mapper_args__ = {
                'concrete': True
            }

.. _concretebase:

#. 使用 *ConcreteBase* 作为基类的基类

    .. warning::

        这种方式的话，查询基类会连带继承类一起查询，基类没有的字段的值为 None,表之间的数据用union all连接起来
        查询得到的对象是基类的对象


    - 基类继承 ConcreteBase以及Base类
    - 基类和继承类对的 __mapper_args__ 属性都需要添加下面内容

        - polymorphic_identity 类别区分
        - concrete 必须设置为 True

    官方给的例子::

        from sqlalchemy.ext.declarative import ConcreteBase

        class Employee(ConcreteBase, db.Model):
            __tablename__ = 'employee'
            id = Column(Integer, primary_key=True)
            name = Column(String(50))

            __mapper_args__ = {
                'polymorphic_identity': 'employee',
                'concrete': True
            }

        class Manager(Employee):
            __tablename__ = 'manager'
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            manager_data = Column(String(40))

            __mapper_args__ = {
                'polymorphic_identity': 'manager',
                'concrete': True
            }

        class Engineer(Employee):
            __tablename__ = 'engineer'
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            engineer_info = Column(String(40))

            __mapper_args__ = {
                'polymorphic_identity': 'engineer',
                'concrete': True
            }

.. _abstract__:

#. 使用 __abstract__  属性

    .. warning::

        - 这种继承 与  :ref:`ConcreteBase <concretebase>` 唯一不同的就是查询基类时会得到得到的是基类和继承类对象的列表
        - 并且基类是不能有 __tablename__属性，也就是 基类是没有数据表的


    - 只需要在基类中添加 __abstract__ 属性就行了
    - 继承类中也需要在  __mapper_args__ 添加参数：

        -  polymorphic_identity

    官方例子::

        class Employee(db.Model):
            __abstract__ = True

        class Manager(Employee):
            __tablename__ = 'manager'
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            manager_data = Column(String(40))

            __mapper_args__ = {
                'polymorphic_identity': 'manager',
            }

        class Engineer(Employee):
            __tablename__ = 'engineer'
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            engineer_info = Column(String(40))

            __mapper_args__ = {
                'polymorphic_identity': 'engineer',
            }

#. 使用 AbstractConcreteBase 类

    .. warning::

        - 这种同 :ref:`__abstract__ <abstract__>` 差不多，唯一不同的是 基类也是可以建表的，只要给了 __tablename__ 属性
        - 这个类继承了  ConcreteBase 类

    - 基类继承 AbstractConcreteBase
    - 继承类的 __mapper_args__ 需要下面参数

        - polymorphic_identity
        - concrete = True

    官方给的例子::

        from sqlalchemy.ext.declarative import AbstractConcreteBase

        class Employee(AbstractConcreteBase, db.Model):
            pass

        class Manager(Employee):
            __tablename__ = 'manager'
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            manager_data = Column(String(40))

            __mapper_args__ = {
                'polymorphic_identity': 'manager',
                'concrete': True
            }

        class Engineer(Employee):
            __tablename__ = 'engineer'
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            engineer_info = Column(String(40))

            __mapper_args__ = {
                'polymorphic_identity': 'engineer',
                'concrete': True
            }