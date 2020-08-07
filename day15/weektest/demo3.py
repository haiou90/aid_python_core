# 3. 二分查找
#     定义函数，在有序数字列表中找到目标值，并返回其索引。
#     如果目标值不在列表中，返回它可以按顺序插入的索引。
#     输入：[1,2,6,8,9]  8
#     输出：3
#
#     输入：[1,2,6,8,9]  5
#     输出：2

def search_insert_index(num_list,target):
    left = 0
    right = len((num_list))-1
    while left <= right:
        mid = (left + right) // 2
        if num_list[mid] == target:
            print('找到%d' % target)
            return mid
        elif num_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print('未找到%d,可以在索引值%d位置插入' % (target,left))
    return left

search_insert_index([1,2,6,8,9],8)
search_insert_index([1,2,6,8,9],5)