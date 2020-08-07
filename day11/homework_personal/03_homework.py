"""
5. list01 = [6,2,3,4,5,6,7,3,2,4,8]
    定义函数,删除列表中重复元素.(不使用其他容器,自定义算法)
"""


def delete_repetion(list_target):
    for r in range(len(list_target)-1,0,-1):
        for c in range(r):
            if list_target[r] == list_target[c]:
                del list_target[r]
                break


list01 = [6, 2, 3, 4, 5, 6, 7, 3, 2, 4, 8]
delete_repetion(list01)
print(list01)