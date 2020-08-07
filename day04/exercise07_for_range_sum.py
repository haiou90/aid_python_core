
# 在终端中累加 0  1  2  3
# 在终端中累加 2  3  4  5  6
# 在终端中累加 1  3  5  7
# 在终端中累加 8  7  6  5  4
# 在终端中累加 -1  -2  -3  -4  -5
total = 0
for number in range(0, 4, 1):
    total += number
print(total)
"""
for 比while循环操作更简便代码更少，在while true以外尽量采用for循环
"""
# count = 0
# result = 0
# while count < 4:
#     result += count
#     count += 1
# print(result)

total = 0
for number in range(2, 7):
    total += number
print(total)

total = 0
for number in range(1, 8, 2):
    total += number
print(total)

total = 0
for number in range(8, 3, -1):
    total += number
print(total)

total = 0
for number in range(-1, -6, -1):
    total += number
print(total)
