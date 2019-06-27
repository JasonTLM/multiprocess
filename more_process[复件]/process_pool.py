# coding=utf-8
from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0～1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕， 耗时为%0.2f" % (t_stop - t_start))


def main():
    po = Pool(3)
    for i in range(10):
        # Pool().apply_async(要调用的目标， (传递给目标的参数元组,))
        # 每次循环将会用空闲出来的子进程取调用目标
        po.apply_async(worker, (i, ))
    print("--------start--------")
    # 子进程结束后，调用close关闭，减少资源的浪费
    po.close()
    """
    由于进程池中，主进程不会等待子进程结束后再往下执行（多进程，多线程时主进程会等待子进程结束后才结束，以保证程序的正常运行）
    故需要调用join(), 使主进程阻塞等待子进程结束后再往下执行
    """
    po.join()
    print("--------end---------")


if __name__ == '__main__':
    main()