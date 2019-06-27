# coding=utf-8

from time import sleep
from collections import Iterator
from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        return self.obj.names[0]


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("jason")
    classmate.add("Bourne")
    classmate.add("jax")

    for name in classmate:
        print(name)
        sleep(1)
