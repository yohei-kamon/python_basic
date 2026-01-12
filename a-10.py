import random


def dice(list):
    result = random.choice(list)
    return result


list = [1, 2, 3, 4, 5, 6]

print(dice(list))  # 1から6の整数をランダムに出力する
