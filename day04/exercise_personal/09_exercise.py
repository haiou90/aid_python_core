# count = 0
# sum_number = 0
# while count < 5:
#     number = int(input("请输入一个数字："))
#     sum_number += number
#     count += 1
# print(sum_number)

count = 0
sum_number = 0
for __ in range(5):
    number = int(input("请输入一个数字："))
    sum_number += number
print(sum_number)

sum_number = 0
while True:
    number = input("请输入一个数字：")
    if number == " ":
        break
    sum_number += int(number)
print(sum_number)