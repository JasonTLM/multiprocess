# coding=utf-8
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        result = yield a
        print(">>>>result>>>>", result)
        a, b = b, a+b
        current_num += 1


if __name__ == '__main__':
    obj = create_num(20)
    result = next(obj)
    print(result)

    result = obj.send("ojbk")
    print(result)