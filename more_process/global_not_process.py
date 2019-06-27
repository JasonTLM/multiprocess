# coding=utf-8

import multiprocessing
from os import getpid
from time import sleep

nums = [11, 22, 33]
def test1():
    nums.append(44)
    print("在进程中1中nums=%s"%str(nums))
    sleep(1)


def test2():
    print("在进程2中nums=%s"%str(nums))


def main():
    print("----in 主进程 pid=%d---父进程pid=%d---"%
          (getpid(), getpid()))
    p1 = multiprocessing.Process(target=test1)
    p1.start()

    p1.join()

    p2 = multiprocessing.Process(target=test2)
    p2.start()


if __name__ == '__main__':
    main()