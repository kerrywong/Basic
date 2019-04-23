#!/user/bin/env python3
# -*- coding: utf-8 -*-

'a test module'
__author__='WangKang'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello,World")
    elif len(args) == 2:
        print("Hello,%s!" % args[1])
    else:
        print("Two many arguments")


if __name__ == '__maim=__':
    test()
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


