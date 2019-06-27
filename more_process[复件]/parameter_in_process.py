# coding=utf-8
import multiprocessing
from os import getpid
from time import sleep


def test(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

def main():
    print("-----in 主进程pid=%d----父进程pid=%d---"%
          (getpid(), getpid()))
    p = multiprocessing.Process(target=test,args=(11, 22, 33, 44,
                                                  55, 66, 77, 88,
                                                  99, 111),
                                kwargs={'mess':'ojbk'})
    p.start()


if __name__ == '__main__':
    main()