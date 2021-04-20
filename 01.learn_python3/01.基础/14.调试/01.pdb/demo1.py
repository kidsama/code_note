# 以
import random
import pdb

num_dict = {"key1": "中国", "key2": "英国", "key3": "德国", "key4": "日本", "key5": "中国", "key6": "英国", "key7": "德国",
            "key8": "日本", "key9": "德国", "key10": "日本"}


def check_double(num):
    tem_key = f"key{num}"
    num_dict[tem_key] = "changed"


def check_three(num):
    tem_key = f"key{num}"
    num_dict[tem_key] = "changed"


if __name__ == '__main__':
    pdb.set_trace()  # 设置断点
    num1 = random.randint(1, 10)
    print(num1)
    if num1 % 2 == 0:
        check_double(num1)
    elif num1 % 3 == 0:
        check_three(num1)
    else:
        check_three(num1)
