"""
4. 在终端中循环录入5个人的年龄,
   最后打印平均年龄(总年龄除以人数)
"""
sum_age = 0
for __ in range(5):
    age = int(input("请输入年龄:"))
    sum_age += age
print("平均年龄为%.1f" % sum_age / 5)