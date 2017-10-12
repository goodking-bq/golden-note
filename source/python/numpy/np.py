# coding:utf-8
from __future__ import absolute_import, unicode_literals

__author__ = "golden"
__date__ = '2017/9/2'

import numpy as np

p_type = np.dtype({'names': ['name', 'age', 'sex'],
                   'formats': ['S30', 'i', 'S1']}, align=True)
a = np.array([('golden', 30, 'b'), ('gg', 20, 'g')], dtype=p_type)
print(a.dtype)
