# coding=utf-8
from time import sleep
from collections import Iterable
from collections import Iterator


class Classmate(object):

    def __init__(self):
        self.names = list()
        self.current_nums = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        if self.current_nums < len(self.names):
            return ClassIterator(self)
        else:
            raise StopIteration
        # return ClassIterator(self)


class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            result = self.obj.names[self.current_num]
            self.current_num += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("Jason")
    classmate.add("Jax")
    classmate.add("Bourne")
    classmate.add("Marin")

    print("判断classmate是否是可以迭代的对象：",
          isinstance(classmate, Iterable))
    classmate_iterator = iter(classmate)
    print("判断classmate_iterator是否是迭代器：",
          isinstance(classmate_iterator, Iterator))
    print(next(classmate_iterator))
    print(next(classmate_iterator))
    print(next(classmate_iterator))
    print(next(classmate_iterator))
    # print(next(classmate_iterator))
    print("---------------------------------------------")

    for name in classmate:
        print(name)
        sleep(1)