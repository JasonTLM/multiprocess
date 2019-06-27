# coding=utf-8

"""
创建锁： mutex = threading.Lock()
锁定： mutex.acquire
释放： mutex.release
be careful:
如果这个锁之前是没有上锁的，那么acquire不会堵塞
如果在调用acquire对这个锁上锁之前 它已经被 其他线程上了锁，那么此时acquire会堵塞，直到这个锁被解锁为止
"""

import threading
from time import sleep

g_nums = 0

def test1(num):
    global g_nums
    for i in range(num):
        mutex.acquire()
        g_nums += 1
        mutex.release()

    print("----test1----g_nums=%d"%g_nums)


def test2(num):
    global g_nums
    for i in range(num):
        mutex.acquire()
        g_nums += 1
        mutex.release()

    print("----test2----g_nums=%d"%g_nums)


if __name__ == "__main__":
    print("----begin----")
    mutex = threading.Lock()
    p1 = threading.Thread(target=test1, args=(1000000,))
    p1.start()



    p2 = threading.Thread(target=test2, args=(1000000,))
    p2.start()

    # 等待计算完成
    while len(threading.enumerate()) != 1:
        sleep(1)

    print("两个线程对同一个全局变量操作之后的最终结果为：%s"%g_nums)
