# coding=utf-8
import threading
import time


def say_Sorry():
    print("Dear, I am so sorry!")
    time.sleep(1)
    print("test!!!")


if __name__ == "__main__":
    for i in range(5):
        # 注意Thread中target传入的不是函数
        t = threading.Thread(target=say_Sorry)
        t.start()
