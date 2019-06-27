# coding=utf-8

from greenlet import greenlet
from time import sleep

def test1():
    while True:
        print("-----A------")
        gr2.switch()
        sleep(0.1)


def test2():
    while True:
        print("-----B------")
        gr1.switch()
        sleep(0.1)


if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    # gr1.switch()
    gr2.switch()