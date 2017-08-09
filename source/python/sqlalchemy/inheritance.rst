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

.. _mapper_concrete__:

#. *mapper.concrete* 基本继承

    .. warning::

        基表和继承表什么关系也没有

            - 查询基类的时候是不会查询到继承类的。
            - 基类的字段也不会继承，所有继承类是没有基类的字段，引用会报错。
            - 基表没有 __tablename__ 也会建表

    * 基类不需要特殊设置
    * 继承类需要在 __mapper_args__ 添加下面参数

        - concrete 设置为 ``True`` 说明是具体的，与基表没有具体的关系

    一个例子::

        class Animal(db.Model):
            """动物基类"""
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(255))
            type = db.Column(db.String(20))

        class Cat(Animal):
            """爬行动物"""
            __tablename__ = 'animal_cat'
            id = db.Column(db.Integer, primary_key=True)
            cat_name = db.Column(db.String(255))
            __mapper_args__ = {
                'concrete': True
            }

        class Dog(Animal):
            __tablename__ = 'animal_dog'
            id = db.Column(db.Integer, primary_key=True)
            dog_name = db.Column(db.String(255))

            __mapper_args__ = {
                'concrete': True
            }




#. Polymorphic Loading - 多态加载继承

    .. hint::

        **多态** 意味着变量并不知道引用的对象是什么，根据引用对象的不同表现不同的行为方式。它在类的继承中得以实现，在类的方法调用中得以体现。

    .. _concretebase:
    * *ConcreteBase* 具体类基类？

        .. warning::

            之所以叫具体类，因为它会在数据库建表，对数据库来说是具体的。

            同 :ref:`mapper.concrete <mapper_concrete__>` 的区别是：

                - 查询基类会连带继承类一起查询，表之间的数据用union all连接起来
                - 查询得到的对象是各自的对象

        - 基类继承 ConcreteBase以及Base类
        - 基类和继承类对的 __mapper_args__ 属性都需要添加下面内容

            - polymorphic_identity 类别区分
            - concrete 必须设置为 True

        例子::

           class Animal(ConcreteBase, db.Model):
                """动物基类"""
                id = db.Column(db.Integer, primary_key=True)
                name = db.Column(db.String(255))

                @declared_attr
                def __mapper_args__(cls):
                    return {'polymorphic_identity': cls.__name__.lower(),
                            'concrete': True}

                def get_cat_name(self):
                    return self.cat_name

                def get_dog_name(self):
                    return self.dog_name


            class Cat(Animal):
                """爬行动物"""
                __tablename__ = 'animal_cat'
                id = db.Column(db.Integer, primary_key=True)
                cat_name = db.Column(db.String(255))


            class Dog(Animal):
                __tablename__ = 'animal_dog'
                id = db.Column(db.Integer, primary_key=True)
                dog_name = db.Column(db.String(255))

        测试::

            animal = Animal()
            animal.name = 'animal1'
            db.session.add(animal)
            db.session.commit()
            cat = Cat()
            # cat.name = 'animal2' # 具体基类的字段不能被继承，不能被赋值
            cat.cat_name = 'cat1'
            db.session.add(cat)
            db.session.commit()
            dog = Dog()
            # dog.name = 'animal2'
            dog.dog_name = 'dog1'
            db.session.add(dog)
            db.session.commit()
            animals = db.session.query(Animal).all()
            cats = Cat.query.all()
            dogs = Dog.query.all()
            print(animals)
            print(cats)
            print(cats[0].get_cat_name())
            print(dogs[0].get_dog_name())
            print(dogs[0].get_cat_name()) # Dog 有这个方法，带上没有 cat_name属性，所以报错。

            [<monitor.models.test.Animal object at 0x000000000AFA1F28>, <monitor.models.test.Cat object at 0x000000000E686080>, <monitor.models.test.Dog object at 0x000000000E6865F8>]
            [<monitor.models.test.Cat object at 0x000000000E686080>]
            cat1
            dog1

            Error
            Traceback (most recent call last):
              File "C:\Users\golden\Anaconda3\envs\flask\lib\unittest\case.py", line 329, in run
                testMethod()
              File "D:\quleduo_manager\test\models.py", line 246, in test_con
                print(dogs[0].get_cat_name())
              File "D:\quleduo_manager\monitor\models\test.py", line 23, in get_cat_name
                return self.cat_name
            AttributeError: 'Dog' object has no attribute 'cat_name'

#. Abstract Concrete Classes - 抽象具体类

    #. 使用 AbstractConcreteBase 类

        .. warning::

            - 基类默认建表，如果 __tablename__=None 则不建 ，但是也不能查询
            - 有字段会建表
            - 继承类会继承所有方法和字段

    - 基类继承 AbstractConcreteBase
    - 继承类的 __mapper_args__ 需要下面参数

        - polymorphic_identity
        - concrete = True

    官方给的例子::

        from sqlalchemy.ext.declarative import AbstractConcreteBase

        class Animal(AbstractConcreteBase, db.Model):
            """动物基类"""
            __tablename__ = None
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(255))

            @declared_attr
            def __mapper_args__(cls):
                return {'polymorphic_identity': cls.__name__.lower(),
                        'concrete': True} if cls.__name__ != "Animal" else {}

            def get_cat_name(self):
                return self.cat_name

            def get_dog_name(self):
                return self.dog_name


        class Cat(Animal):
            """爬行动物"""
            __tablename__ = 'animal_cat'
            cat_name = db.Column(db.String(255))


        class Dog(Animal):
            __tablename__ = 'animal_dog'
            dog_name = db.Column(db.String(255))


        cat = Cat()
        cat.name = 'animal2'
        cat.cat_name = 'cat1'
        db.session.add(cat)
        db.session.commit()
        dog = Dog()
        dog.name = 'animal2'
        dog.dog_name = 'dog1'
        db.session.add(dog)
        db.session.commit()
        animals = db.session.query(Animal).all()
        cats = Cat.query.all()
        dogs = Dog.query.all()
        print(animals)
        print(cats)
        print(cats[0].get_cat_name())
        print(dogs[0].get_dog_name())
        print(dogs[0].get_cat_name()) #报错

        [<monitor.models.test.Dog object at 0x000000000E6A00F0>, <monitor.models.test.Cat object at 0x000000000B0C4160>]
        [<monitor.models.test.Cat object at 0x000000000B0C4160>]
        cat1
        dog1

        Error
        Traceback (most recent call last):
          File "C:\Users\golden\Anaconda3\envs\flask\lib\unittest\case.py", line 329, in run
            testMethod()
          File "D:\quleduo_manager\test\models.py", line 246, in test_con
            print(dogs[0].get_cat_name())
          File "D:\quleduo_manager\monitor\models\test.py", line 23, in get_cat_name
            return self.cat_name
          File "C:\Users\golden\Anaconda3\envs\flask\lib\site-packages\sqlalchemy\orm\attributes.py", line 293, in __get__
            return self.descriptor.__get__(instance, owner)
          File "C:\Users\golden\Anaconda3\envs\flask\lib\site-packages\sqlalchemy\orm\descriptor_props.py", line 492, in __get__
            warn()
          File "C:\Users\golden\Anaconda3\envs\flask\lib\site-packages\sqlalchemy\orm\descriptor_props.py", line 480, in warn
            (self.parent, self.key, self.parent))
        AttributeError: Concrete Mapper|Dog|animal_dog does not implement attribute 'cat_name' at the instance level.  Add this property explicitly to Mapper|Dog|animal_dog.
