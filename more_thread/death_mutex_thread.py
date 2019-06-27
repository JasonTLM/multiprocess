# coding=utf-8

import threading
from time import sleep


class MyThread1(threading.Thread):
    def run(self):
        # 对mutexA上锁
        mutexA.acquire()

        # mutexA上锁后，延时一秒，等待其他线程，把mutexB上锁
        print(self.name + '-------do--1-----up----')
        sleep(1)

        mutexB.acquire()
        print(self.name + '-------do--1-----down----')
        mutexB.release()

        # 对mutexA解锁
        mutexA.release()


class MyThread2(threading.Thread):
    def run(self):
        # 对mutexB上锁
        mutexB.acquire()

        # mutexB上锁之后，延迟1秒，等待另一个线程吧mutexA上锁
        print(self.name + '-------do--2-----up----')
        sleep(1)

        # 此时产生堵塞，因为这个mutexA已经被另外一个线程抢险上锁了
        mutexA.acquire()
        print(self.name + '-------do--2-----down----')
        mutexA.release()

        # 对mutexB解锁
        mutexB.release().release()
        # 对mutexB解锁mutexB.r


if __name__ == "__main__":
    mutexA = threading.Lock()
    mutexB = threading.Lock()
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()

