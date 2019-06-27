# coding=utf-8

import threading
from time import sleep
from time import ctime


def sing():
    for i in range(5):
        print("sing now...%d"%i)
        sleep(1)


def dance():
    for i in range(5):
        print("dancing now...%d"%i)
        sleep(1)


if __name__ == "__main__":
    print("---start---:%s"%ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()
    sleep(0.3)
    print("hello")

    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数为：%d"%length)
        if length <= 1:
            break

        sleep(0.5)
