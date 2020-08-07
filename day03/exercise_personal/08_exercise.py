"""
在终端中获取月份，打印相应的天数.
1 3 5 7 8 10 12 有 31天
2有28天
4 6 9 11 有 30天
输入的月份有误
"""
month = int(input("请输入月份:"))
li1 = [1, 3, 5, 7, 8, 10, 12 ]
li2 = [2]
li3 = [4, 6, 9, 11]
if month in li1:
    print("31天")
elif month in li2:
    print("28天")
elif month in li3:
    print("30天")
else:
    print("输入月份有误")