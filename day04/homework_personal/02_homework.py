"""
5. 在终端中循环录入年龄,如果录入空,则退出循环.
   最后打印平均年龄(总年龄除以人数)
"""
count = 0
sum_age = 0
while True:
    age = input("请输入年龄:")
    if age == " ":
        break
    sum_age += int(age)
    count += 1
print("平均年龄为%.1f" % (sum_age / count))