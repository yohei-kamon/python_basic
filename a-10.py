import random


def dice():
    result = random.randint(1, 6)
    return result


print(dice())
# list = [1, 2, 3, 4, 5, 6]

# print(dice(list))  # 1から6の整数をランダムに出力する
