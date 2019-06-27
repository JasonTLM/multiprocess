# coding=utf-8

def create_num(all_num):
    print("-----1-----")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("----2-----")
        yield a
        print("----3-----")
        a, b = b, a+b
        current_num += 1
        print("----4------")


if __name__ == '__main__':
    obj1 = create_num(5)
    obj2 = create_num(2)

    result1 = next(obj1)
    print("obj:",result1)

    result2 = next(obj2)
    print(result2)