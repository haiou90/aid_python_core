# list01 = [1,2,3,4]
# list02 = list01
# list03 = list01[:]
# print(list03)
# list03[0] = 100
# print(list03)
# print(list01)
# list01[:] = []#修改列表元素
# print(list03)
# print(list01)
# print(list02)

message = "to have people"
list01 = message.split(" ")[::-1]

print(" ".join(list01))