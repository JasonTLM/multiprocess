# coding=utf-8
import gevent
from time import sleep

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        sleep(0.5)
        # gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


if __name__ == '__main__':
    print("------1-------")
    g1 = gevent.spawn(f1, 5)
    print("------2-------")
    g2 = gevent.spawn(f2, 5)
    print("------3-------")
    g3 = gevent.spawn(f3, 5)
    print("------3-------")
    g1.join()
    g2.join()
    g3.join()
