# coding=utf-8
from time import sleep
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """
        如果要对一个对象称之为可迭代对象，即为可使用for循环获得的值，那么必须实现__iter__
        方法
        :return: ClassIterator()
        """
        return ClassIterator()


class ClassIterator(object):
    def __iter__(self):
        pass

    def __next__(self):
        return 'ojbk'


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("Jason")
    classmate.add("Bourne")
    classmate.add("jax")

    print("判断classmate是否是一个可迭代对象：", isinstance(classmate, Iterable))
    classmate_iterator = iter(classmate)
    print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))
    print(next(classmate_iterator))

    for name in classmate:
        print(name)
        sleep(1)
        names = list()
        names.append(name)
        if len(names) == 10:
            break