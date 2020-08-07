"""
将列表中整数的十位不是3和7和8的数字存入另外一个列表
   list03 = [135, 63, 227, 675, 470, 733, 3127]
   结果:[63, 227, 3127]
   提示：将数字转换为字符串进行处理
"""

list03 = [135, 63, 227, 675, 470, 733, 3127]
list04 = []
list05 = []
for i in range(len(list03)):
    list04.append(str(list03[i]))
for item in list04:
    # print(item[-2])
    if item[-2] not in ("3", "7", "8"):
    # if item[-2] == 3:
    #     continue
        list05.append(item)
        print(list05)
        # list04.append(list03[i])
# print(list05)

