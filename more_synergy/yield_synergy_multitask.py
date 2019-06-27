# coding=utf-8
from time import sleep

def task_1():
    while True:
        print("-------1---------")
        sleep(0.2)
        yield


def task_2():
    while True:
        print("-------2---------")
        sleep(0.2)
        yield


def main():
    t1 = task_1()
    t2 = task_2()

    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()