# coding=utf-8
from threading import Thread
import time

g_num = 100
# globals(g_num)

def work1():
    global g_num
    for i in range(5):
        g_num += 1

    print("------in work1, g_num is %d---"%g_num)


def work2():
    global g_num
    print("------in work2, g_num is %d---"%g_num)


print("-------线程创建之前g_num is %d---"%g_num)

if __name__ == "__main__":
    t1 = Thread(target=work1)
    t1.start()
    time.sleep(1)

    t2 = Thread(target=work2)
    t2.start()


