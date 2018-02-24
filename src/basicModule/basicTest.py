# coding:utf-8

import time
import tensorflow as tf
import pip
import doctest
import unittest
import nose
from decorator import decorate
from _stat import filemode


def main():
    testLogging()
    # test_Decorate()
    # testDebug()
    # testTime()
    # testFile()
    # testDemo()
    # testList()
    # testString()
    pass


def testLogging():
    import logging
    print('testLogging begin.')
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='ingoo.log',
        filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logging.debug("Logging message for basicDemo.")
    for x in range(9):
        logging.debug('Current value: {}'.format(x))
    pass


def decorate_fun(fun):
    def new_fun(*args, **kwargs):
        print('initial parameters: {}, {}'.format(args, kwargs))
        print('this is the fun()"s start')
        fun(*args, **kwargs)
        print('this is the fun()"s end')
    return new_fun


@decorate_fun
def fun(number, start_number=0):
    for n in range(number):
        start_number += n
        print(n)
        time.sleep(1)
    print('the final number is {}'.format(start_number))


def test_Decorate():
    print(fun.__name__)  # new_fun
    fun(5, start_number=5)
    pass


def just_do_it(text):
    return text.capitalize()
    pass


def list_generator(number):
    '''
    >>> list_generator(4)
    [0, 1, 2, 3]
    '''
    return [n for n in range(number)]
    pass


def testFile():
    '''
    from os import path
    testPath = './config/config.xml'
    print(path.isfile(testPath), path.abspath(testPath), path.dirname(testPath))
    print(path.isdir(testPath), path.isdir(str(path.abspath(testPath))), path.isabs(testPath))
    print('parse end.')
    '''
    '''
    import os
    os.mkdir('testDir')
    #os.rmdir('testDir')
    print(os.listdir('./config'))
    print(os.getcwd())
    os.chdir('./config')
    print(os.getcwd(), os.curdir)
    '''
    '''
    import os, glob
    newDir = 'C:\Python27\include'
    os.chdir(newDir)
    print(os.getcwd())
    print(glob.glob('a?[dt]*'))
    '''
    '''
    import os, shutil
    print(shutil.copy('./config/config.xml', './config/config2.xml'))
    print(shutil.move('./config/config2.xml', './config/config3.xml'))
    '''
    pass


def testDemo():
    var = (('a1'), ('c2'))
    varDict1 = dict(var)
    print(varDict1, 'c' in varDict1, ('s' in varDict1))
    var2 = (('a', '10'), ('b', '3'))
    varDict2 = dict(var2)
    print(varDict2)

    varDict2.update(varDict1)
    print(varDict2, varDict2.get('b'), varDict2.get('b'), varDict2.get('d'),
          varDict2.keys(), varDict2.values(),
          varDict2.items())
    pass


def testList():
    stringList = "999123456789 jk"
    oldList = list(stringList)
    print(type(oldList), oldList)
    newList = oldList[0: 4: 2]
    print(type(newList), newList)
    verList = oldList[::-1]
    print(type(verList), verList)
    oldList[0: 2] = []
    print(type(oldList), oldList)
    del oldList[0: 1]
    print(type(oldList), oldList)
    pass


def testString():
    '''
    Test string.
    '''
    stringMy = "i am in mediatedk." * 2
    print(stringMy[3], stringMy, isinstance(stringMy, str))
    '''
    stringlist = stringMy.split(sep = " ")
    print(type(stringlist), stringlist)'''
    pass


class TestCap(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_word(self):
        text = 'duck'
        result = just_do_it(text)
        self.assertEqual(result, 'Duck')

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = just_do_it(text)
        self.assertEqual(result, 'A veritable flock of ducks')


if __name__ == '__main__':
    # print(pip.pep425tags.get_supported())
    main()
    # doctest.testmod()
    # unittest.main()
    pass
