Model 轻松转 dict 和 json
--------------------------------

.. code-block:: python

    # coding:utf-8
    from __future__ import absolute_import, unicode_literals
    from flask_sqlalchemy import SQLAlchemy, Model, BaseQuery
    from sqlalchemy.ext.declarative import DeclarativeMeta
    import json


    class JsonModel(Model):
        __exclude__ = ['id']  # to_dict 排除字段
        __include__ = []  # 包含字段
        __exclude_foreign__ = True  # 排除外键

        def dict(self):
            data = {}
            for field in self.__fields__():
                value = getattr(self, field)  # value
                if isinstance(value.__class__, DeclarativeMeta):
                    data[field] = value.dict()
                elif not hasattr(value, '__func__') and not isinstance(value, BaseQuery):
                    try:
                        data[field] = value
                    except TypeError:
                        data[field] = None
            return data

        def json(self):
            data = {}
            for field in self.__fields__():
                value = getattr(self, field)  # value
                if isinstance(value.__class__, DeclarativeMeta):
                    data[field] = value.dict()
                elif not hasattr(value, '__func__') and not isinstance(value, BaseQuery):
                    try:
                        json.dumps(value)
                        data[field] = value
                    except TypeError:
                        try:
                            data[field] = str(value)
                        except Exception as e:
                            data[field] = None
            return json.dumps(data)

        def __foreign_column__(self):
            data = []
            for column in self.__table__.columns:
                if getattr(column, 'foreign_keys'):
                    data.append(column.key)
            return data

        def __fields__(self):
            fields = set(dir(self))
            if self.__exclude_foreign__:
                fields = fields - set(self.__foreign_column__())
            fields = fields - set(self.__exclude__)
            fields = set(list(fields) + self.__include__)
            return [f for f in fields if
                    not f.startswith('_') and not f.endswith('_id') and f not in ['metadata', 'query', 'query_class',
                                                                                  'dict', 'json']]


    db = SQLAlchemy(model_class=JsonModel)


