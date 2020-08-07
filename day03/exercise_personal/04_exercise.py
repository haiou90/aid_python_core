unit_price = float(input("请输入单价:"))
number = float(input("请输入数量:"))
pay = float(input("请输入金额:"))

if pay - unit_price * number >= 0:
    print("应找回:" + str(pay - unit_price * number) + "元")
else:
    print("金额不足")
