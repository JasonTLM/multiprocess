# coding=utf-8
from collections import Iterator
from collections import Iterable
from time import sleep


class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            results = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return results
        else:
            raise StopIteration


if __name__ == '__main__':
    nums = int(input("请输入一个整数："))
    result = Fibonacci(nums)
    print("查看result是否是一个迭代器：", isinstance(result, Iterator))
    nums_list = list()
    for num in result:
        # print(num)
        nums_list.append(num)
        # print("\r%s" %s(nums_list), end="")
        # sleep(1)
        # print(nums_list, end="")
        print(nums_list)
        sleep(1)
        # print(nums_list)

    # sleep(1)
