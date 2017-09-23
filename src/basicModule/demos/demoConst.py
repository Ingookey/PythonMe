# coding: utf-8

# Way1 直接使用类的成员变量


class Foo(object):
    CONST_NAME = "Name"
    CONST_AGE = 28

# Way2 使用 namedtuple进行构造


def getConstants2():
    from collections import namedtuple

    Constants = namedtuple("Constants", ['pi', 'e', 'package'])
    constants = Constants(3.14, 2.718, 'com.ingookey')
    # constants.pi = 78  # AttributeError: can't set attribute
    print("constants.package: {}".format(constants.package))
    pass


# Way3 使用开源库
'''
def getConstants():
    from named_constants import Constants

    class Colors(Constants):
        black = 0
        red = 1
        white = 15
        package = 'com.ingookey'

    print("Const: {}".format(Colors.package))
    pass
'''


def demoConst():
    # For way1
    print(2 * Foo.CONST_AGE)

    # For way2
    getConstants2()
    pass


if __name__ == '__main__':
    demoConst()
    pass
