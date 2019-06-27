# coding=utf-8

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)


def test():
    print('-----分隔符-----')
    for i in range(5):
        t = MyThread()
        t.start()
        time.sleep(2)
    while True:
        length = len(threading.enumerate())
        print(length)
        if length <= 1:
            break

if __name__ == "__main__":
    test()
