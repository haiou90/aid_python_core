# 在终端中累加 0  1  2  3
# 在终端中累加 2  3  4  5  6
# 在终端中累加 1  3  5  7
# 在终端中累加 8  7  6  5  4
# 在终端中累加 -1  -2  -3  -4  -5


# count = 0
# result = 0
# while count < 4:
#     result += count
#     count += 1
# print(result)
#
# count = 2
# sum_value = 0
# while count < 7:
#     sum_value += count
#     count += 1
# print(sum_value)
#
# count = 1
# number = 0
# while count < 8:
#     number += count
#     count += 2
# print(number)
#
# count = 8
# number = 0
# while count >= 4:
#     number += count
#     count -= 1
# print(number)

"""
复习补充代码,演示累加过程中之前值和当前值的实际变化过程
"""
count = -1
number = 0
while count >= -5:
    number += count
    print(number)
    count -= 1
    print(count)
print(number)
