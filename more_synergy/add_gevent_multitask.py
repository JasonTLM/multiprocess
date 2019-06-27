# coding=utf-8
from gevent import getcurrent
from time import sleep
from gevent import monkey
from gevent import spawn


def f1(n):
    for i in range(n):
        print(getcurrent(), i)
        sleep(0.5)


def f2(n):
    for i in range(n):
        print(getcurrent(), i)
        sleep(0.5)


def f3(n):
    for i in range(n):
        print(getcurrent(), i)
        sleep(0.5)


if __name__ == '__main__':
    print("---------1----------")
    g1 = spawn(f1, 5)
    print("---------2----------")
    g2 = spawn(f2, 5)
    print("---------3----------")
    g3 = spawn(f3, 5)
    print("---------4----------")
    g1.join()
    g2.join()
    g3.join()


