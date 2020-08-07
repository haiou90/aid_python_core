"""
电梯设置规定：
如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，否则提示超载。
步骤:
终端中获取人数 / 总重量
显示电梯正常运行
电梯超载
"""
number_people = int(input("请输入人数:"))
weight_people = int(input("请输入重量:"))

if number_people <= 10 and weight_people <= 1000:
    print("电梯正常运行")
else:
    print("电梯超载")