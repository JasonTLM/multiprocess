# coding=utf-8

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)


class TestThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            mess = "This's test " + self.name + ' @ ' + str(i)
            print(mess)


if __name__ == "__main__":
    print('---begin---:%s'%time.ctime())

    t = MyThread()
    te = TestThread()
    t.start()
    te.start()

    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为：%d'%length)
        if length <= 1:
            break

        time.sleep(0.5)
