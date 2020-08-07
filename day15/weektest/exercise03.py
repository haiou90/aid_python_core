"""二分查找
定义函数，在有序数字列表中找到目标值，并返回其索引。
如果目标值不在列表中，返回它可以按顺序插入的索引。
输入：[1,2,6,8,9]  8
输出：3

输入：[1,2,6,8,9]  5
输出：2"""

def find_half(list_init,target):

    if list_init[len(list_init)//2] == target:
        return len(list_init) // 2
    elif target < list_init[len(list_init)//2]:
        for i in range(len(list_init)//2):
            if list_init[i] == target:
                return i
            elif target not in list_init:
                for i in range(len(list_init) // 2):
                    if target < list_init[i]:
                     return i
    elif target > list_init[len(list_init)//2]:
        for i in range(len(list_init) // 2,len(list_init)):
            if list_init[i] == target:
                return i
            elif target not in list_init:
                for i in range(len(list_init) // 2, len(list_init)):
                    if target < list_init[i]:
                        return i


# print(find_half([1, 2, 6, 8, 9], 8))
print(find_half([1,2,6,8,9], 5))


def search_insert_index(num_list,target):
    left = 0
    right = len(num_list)-1
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == target:
            return mid
        elif num_list[mid] < target:
            left = mid +1
        else:
            right = mid - 1

    return left