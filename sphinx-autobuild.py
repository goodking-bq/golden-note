#!/root/anaconda3/bin/python
# coding:utf-8
from __future__ import absolute_import, unicode_literals
from sphinx_autobuild import main
import re
import sys

__author__ = "golden"
__date__ = '2017/8/11'

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
