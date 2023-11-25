import random
from functools import lru_cache

@lru_cache(maxsize=128)
def func1():
    print("xxx")
    # 生成一个文件，文件名为随机数
    file_name = random.randint(0, 1000)
    with open(f"{file_name}.log", "w") as file:
        file.write("xxxxxxxxxx")
    print("YYY")
    return "success"


if __name__ == '__main__':
    print(func1())
    print(func1())
    print(func1())
