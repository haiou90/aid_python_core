MA = int(input("请输入心里年龄"))
CA = int(input("请输入实际年龄"))
iq = MA / CA * 100
if iq >= 140:
    print("天才")
elif 139 >= iq >= 120:
    print("超常")
elif 119 >= iq >= 110:
    print("聪慧")
elif 109 >= iq >= 90:
    print("正常")
elif 89 >= iq >= 80:
    print("迟钝")
else:
    print("低能")