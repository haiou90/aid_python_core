"""在终端中录入一个年份，
如果是闰年为变量day赋值29 否则赋值28。
闰年条件：
年份能被4整除但不能被100整除
或者能被400整除.
"""
# year = int(input("请输入一个年份:"))
#
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     day = 29
# else:
#     day = 28
#
# print(day)

year = int(input("请输入一个年份:"))
day = 29 if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 28
print(day)