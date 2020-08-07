"""
6. 模拟登录
    如果账号的密码错误3次，提示锁定账户，效果如下：
        请输入账号：qtx
        请输入密码：1234
        登录失败
        你还剩余 2 次机会
        请输入账号：Qtx
        请输入密码：1234
        登录失败
        你还剩余 1 次机会
        请输入账号：Qtx
        请输入密码：123456
        登录成功
"""
count = 0
while count < 3:#for count in range (3)
    account = input("请输入账号:")
    password = input("请输入密码:")
    if account == "Qtx" and password == "123456":
        print("登录成功")
        break
    else:
        print("登录失败")
        print("你还剩余%d次机会" % (2 - count))
        count += 1
else:
    print("锁定账户")