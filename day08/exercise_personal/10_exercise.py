"""
参照day07/demo02,
定义函数,对列表进行排序.
"""

# list01 = [43, 15, 5, 67, 87, 9]
#     for r in range(len(list01) - 1): # 0 1
#         for c in range(r + 1, len(list01)):
#             if list01[r] > list01[c]:
#                 list01[r], list01[c] = list01[c], list01[r]
# print(list01)

def rank_list(list_target):
    for r in range(len(list_target) - 1):  # 0 1
        for c in range(r + 1, len(list_target)):
            if list_target[r] > list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    # return list_target   #写法1,使用return
list01 = [43, 15, 5, 67, 87, 9]
# print(rank_list(list01)) #写法1,使用return
rank_list(list01)    #写法2,不使用return,修改实参列表
print(list01)        #写法2,不使用return,修改,不使用return,修改实参列表实参列表