"""
6. (选做)2048 游戏核心算法
# 全局变量
list_merge = [2, 0, 2, 0]

# (1)定义零元素向后移动的函数　zero_to_end()
     思想：从后向前判断，如果是0则删除,在末尾追加.
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]

# (2)定义合并函数　merge()
    核心思想：零元素后移，判断是否相邻相同。如果是则合并.
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]

"""
list_merge = [4,0,2,2]
def zero_to_end():
    for i in range(len(list_merge)-1,-1,-1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)

# zero_to_end()
# print(list_merge)

def merge():
    zero_to_end()
    for i in range(len(list_merge)-1):
        # zero_to_end()
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)
            # list_merge[i+1] = 0

merge()
print(list_merge)


def merge():
    for i in range(len(list_merge)-1):
        zero_to_end()
        if list_merge[i] == list_merge[i+1]:
            list_merge[i] += list_merge[i+1]
            list_merge[i+1] = 0