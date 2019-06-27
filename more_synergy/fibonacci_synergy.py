# coding=utf-8
def fibonacci(num):
    nums = list()
    a = 0
    b = 1
    x = 0
    while x < num:
        nums.append(a)
        a, b = b, a+b
        x += 1
    return nums

if __name__ == '__main__':
    num = int(input("请输入一个整数："))
    result = fibonacci(num)
    print(result)