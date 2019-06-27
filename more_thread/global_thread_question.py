# coding=utf-8
import threading
import time


g_num = 0

def work1(num):
    global g_num
    for i in range(num):
        g_num += 2
    print("----in this work1, g_num is %d----"%g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 2
    print("----in this work2, g_num is %d----"%g_num)


if __name__ == "__main__":
    print("-----线程创建之前g_num is %d----"%g_num)

    t1 = threading.Thread(target=work1, args=(1000000,))
    t1.start()

    t2 = threading.Thread(target=work2, args=(1000000,))
    t2.start()
