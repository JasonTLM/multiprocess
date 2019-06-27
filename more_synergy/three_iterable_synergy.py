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
        如果想要实现一个对象称之为可迭代对象，即为可使用for循环得到value值的对象
        则必须实现__iter__方法
        :return:
        """
        return ClassIterator(self)


class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        # try:
        result = self.obj.names[self.current_num]
        # except IndexError:
        #     pass

        self.current_num += 1
        return result


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("Jason")
    classmate.add("Bourne")
    classmate.add("Jax")
    """
    可使用isinstance()来判断创建的对象是否是可迭代的对象或者，是否为迭代器
    """
    print("判断classmate是否是可迭代对象：", isinstance(classmate, Iterable))
    classmate_iterator = iter(classmate)
    print("判断classmate是否是迭代器：", isinstance(classmate_iterator, Iterator))

    for name in classmate:
        # try:
        print(name)
        sleep(1)
        # except IndexError:
        #     break
