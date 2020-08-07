"""
    列表内存分配
"""
# list01 = [10, 20, 30]
# 变量list02得到的是变量list01存储的列表地址
# list02 = list01
# 变量list03得到的是新列表的地址
# list03 = list01[:]
# 变量list04得到的是第一个列表的第一个元素记录的数据(10)地址
# list04 = list01[0]
"""
list01 = ["烤鸭", "火锅", "麻花"]
list02 = list01
list03 = list01[:]
list04 = list01[::-1]

list01 = ["烤鸭", "火锅", "麻花"]
# 通过索引修改,第一个元素指向列表
list01[0] = ["豆汁"]
# 通过切片修改,第二个元素指向列表的元素
list01[1:2] = ["兔头"]
list03[::-1] = ["烤鸭", "火锅", "麻花"]
print(list03)# ['麻花', '火锅', '烤鸭']"""

list01 = [10, 30, [10, 20]]
print(list01)
# 变量list02得到的是变量list01存储的列表地址
list02 = list01
print(list02)
# 变量list03得到的是新列表的地址
list03 = list01[:]
print(list03)
# 变量list04得到的是第一个列表的第一个元素记录的数据(10)地址
list04 = list01[0]
print(list04)


list01[0:1] = ["100"]
list01[1] = "[兔头]"
list01[2][1] = [200]
list03[1] = "wangb"
list03[2][0] = [100]
print(list01)
print(list02)
print(list03)
print(list04)