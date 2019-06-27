# coding=utf-8

from time import sleep


def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a
        a, b = b, a+b
        current_num += 1

    return "ojbk"


if __name__ == '__main__':
    obj = create_num(30)
    while True:
        try:
            result = next(obj)
            print(result)
            sleep(0.5)
        except Exception as result:
            print(result.value)
            break
