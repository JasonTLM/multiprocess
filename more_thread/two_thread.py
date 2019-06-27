# coding=utf-8

# 主线程会等待所有子线程结束后才结束

import threading
from time import sleep
from time import ctime


def sing():
    for i in range(5):
        print("sing now...%d"%i)
        sleep(0.5)


def dance():
    for i in range(5):
        print("dancing now...%d"%i)
        sleep(5)


if __name__ == "__main__":
    print("---starting---:%s"%ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()
    # sleep(5)
    print("---ending---%s"%ctime())

