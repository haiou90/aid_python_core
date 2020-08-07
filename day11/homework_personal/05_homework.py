"""
7. (选做) 2048 核心算法
    3. 定义向左移动函数,改变list_map中的数据
       思路：将list_map每行赋值给list_merge
            调用合并函数(练习2)

    4. 定义向右移动函数,改变list_map中的数据
       思路：将list_map每行,反转,赋值给list_merge
            调用合并函数
            将list_merge反转后赋值给list_map

"""

# list_merge = [2, 0, 2, 0]
#
# # 1. 定义函数　zero_to_end()
# # [2,0,2,0]  -->  [2,2,0,0]
# # [2,0,0,2]  -->  [2,2,0,0]
# # [2,4,0,2]  -->  [2,4,2,0]
# def zero_to_end():
#     """
#         零元素向后移动
#         思想：从后向前判断，如果是0则删除,在末尾追加.
#     """
#     for i in range(len(list_merge) - 1, -1, -1):
#         if list_merge[i] == 0:
#             del list_merge[i]
#             list_merge.append(0)
#
#
# # 测试
# # zero_to_end()
# # print(list_merge)
#
# # 2. 定义合并函数(向左移动的核心算法)　merge()
# # [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# # [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# # [4,4,4,4]  -->  [8,8,0,0]
# # [2,0,4,2]  -->  [2,4,2,0]
# def merge():
#     """
#         合并
#           核心思想：零元素后移，判断是否相邻相同。如果是则合并.
#     """
#     zero_to_end()
#     # [4,4,4,4]
#     for i in range(len(list_merge) - 1):
#         if list_merge[i] == list_merge[i + 1]:
#             list_merge[i] += list_merge[i + 1]
#             del list_merge[i + 1]
#             list_merge.append(0)
#
#
# merge()
# print(list_merge)



list_merge = [2, 0, 2, 0]

def zero_to_end():
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)

list_map = [
    [2, 0, 2, 0],
    [2, 0, 0, 2],
    [4, 4, 4, 4],
    [2, 0, 4, 2]
]


# def move_to_left():
#     global list_merge
#     for line in list_map:
#         list_merge = line
#         merge()


# def move_to_right():
#     global list_merge
    # for item in list_map:
    #     item.reverse()
    #     list_merge = item   #item[::-1]
    #     merge()
    #     list_merge.reverse()
    #     item = list_merge

#     for line in list_merge:
#         list_merge = line[::-1]
#         merge()
#         line[::-1] = list_merge
#
# move_to_right()
# print(list_map)

def move_right():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in list_map:
        # 从右向左获取数据形成新列表
        list_merge = line[::-1]  # 反转列表 将右需求 转嫁给 左移
        # a = list_merge
        # 处理数据
        merge()
        # 将处理后的数据再从右向左还给map
        line[::-1] = list_merge

move_right()
print(list_map)