# coding=utf-8
from time import sleep
from collections import Iterator
from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            result = self.names[self.current_num]
            self.current_num += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("Jason")
    classmate.add("Bourne")
    classmate.add("Jax")
    classmate.add("包青天")
    classmate.add("厂长")

    print("判断classmate是否是一个可迭代对象：", isinstance(classmate, Iterable))
    classmate_iterator = iter(classmate)
    print("判断classmate_iterator是否是一个迭代器", isinstance(classmate_iterator, Iterator))

    for name in classmate:
        print(name)
        sleep(1)
