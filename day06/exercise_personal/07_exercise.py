"""\
dict01 = {number: number ** 2
for number in range(1, 11)
}

# dict01 = {}
# for number in range(1, 11):
# if number % 2 ==0:
# dict01[number] = number ** 2

dict01 = {number: number ** 2
for number in range(1, 11)
if number % 2 == 0}
print(dict01)

# 练习1：将两个列表，合并为一个字典
# 姓名列表["张无忌","赵敏","周芷若"]
# 房间列表[101,102,103]
# 练习2：颠倒练习1字典键值
"""
list_name = ["张无忌","赵敏","周芷若"]
list_room = [101,102,103]
dict01 = {}
for i in range(len(list_name)):
    dict01[list_room[i]] = list_name[i]
print(dict01)

dict01 ={v: k for k,v in dict01.items()}