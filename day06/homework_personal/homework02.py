""""
将列表中的数字累减
    list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    提示：初始为第一个元素
    """
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
list_subtraction = 5
for num in list02:
    list_subtraction -= num
print(list_subtraction)