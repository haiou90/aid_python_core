list01 = ["烤鸭", "火锅", "麻花"]
list02 = list01
list03 = list01[:]
list04 = list01[::-1]

list01 = ["烤鸭", "火锅", "麻花"]
list01[0] = ["豆汁"]
list01[1:2] = ["兔头"]
list03[::-1] = ["烤鸭", "火锅", "麻花"]
print(list01)
print(list02)
print(list03)
print(list04)