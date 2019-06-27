# coding=utf-8

import multiprocessing
import os
from time import sleep


def test1():
    while True:
        print("----in 子进程1 pid=%d, 父进程的pid=%d---"%(os.getpid(),
              os.getpid()))
        sleep(1)


def test2():
    while True:
        print("----in 子进程2 pid=%d, 父进程的pid=%d---"%
              (os.getpid(), os.getpid()))
        sleep(1)


def main():
    print("----in 主进程 pid=%d---父进程pid=%d----"%
          (os.getpid(), os.getpid()))
    p1 = multiprocessing.Process(target=test1)
    p1.start()

    p2 = multiprocessing.Process(target=test2)
    p2.start()


if __name__ == '__main__':
    main()