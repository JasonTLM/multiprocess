# coding=utf-8

import time


def say_Sorry():
    print("\tI am sorry, Dear.")
    time.sleep(0.5)
    print("-"*20)



if __name__ == "__main__":
    for i in range(5):
        say_Sorry()
