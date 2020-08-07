"""--定义函数,将列表中奇数设置为1
    --定义函数,将列表中奇数删除
    测试数据:[3,7,5,6,7,8,9,13]
    结论:在列表中删除多个元素,倒序删除 """

def change_odd_number(list_target):
    for i in range(len(list_target)):
        if list_target[i] % 2 == 1:
            list_target[i] = 1

list_target = [3,7,5,6,7,8,9,13]
change_odd_number(list_target)
print(list_target)

def delete_odd_number(list_target):
    for i in range(len(list_target)-1,-1,-1):
        if list_target[i] % 2 == 1:
            del list_target[i]

list_target = [3,7,5,6,7,8,9,13]
delete_odd_number(list_target)
print(list_target)