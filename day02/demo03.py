"""
    问题：
        程序运行在哪里？  -- 内存
        程序在处理什么？  -- 数据

    变量
        定义：在内存中，操作数据。
        语法：
            变量名 = 数据
    练习:exercise03
"""
# name01 得到的是数据("刘陈方")地址
name01 = "刘陈方"
name02 = "闫艺锋"
name01 = "朱林旭"
print("您好：" + name01)# 您好：朱林旭

# name03得到的是变量name02存储的数据("闫艺锋")地址, name02调整时,name03未变化
name03 = name02
print(name03)
name02 = "王"
print(name02)
print(name03)
