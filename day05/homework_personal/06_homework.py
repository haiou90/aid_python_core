"""
8. 在终端中录入疫情地区名称，如果输入空字符串，则停止。
   最后倒序打印所有省份名称(一行一个)
   要求：录入的名称已经存在不要再次添加.
   提示： in
"""
list_region = ["香港", "内蒙古", "四川"]
list_print = []
while True:
    type_in = input("请录入省份:")
    if type_in == " ":
        break

    if type_in not in list_region:
        print("超出范围")
        continue
    list_print.append(type_in)

for i in range(len(list_print) - 1, -1, -1):
    print(list_print[i])


""" 课程答案 """
list_region = []
while True:
    type_in = input("请录入省份:")
    if type_in == " ":
        break

    if type_in in list_region:
        print("已经存在")
        continue
    list_region.append(type_in)

for i in range(len(list_region) - 1, -1, -1):
    print(list_region[i])
