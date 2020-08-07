# 2. 定义函数，删除列表中所有重复的元素(重复元素只保留一个)。
# 输入：[4,35,7,35,64,7,35]
# 输出：[4, 35, 7, 64]
def delete_duplist(target):
    for r in range(len(target)-1,0,-1):
        #r = range(5,-1,-1) 5 4 3 2 1 0
        for c in range(r):
            #r = 5   c = 0~4 0 1 2 3 4
            if target[c] == target[r]:
                del target[r]
                break

def delete_duplist2(target):
    for r in range(len(target)-1,-1,-1):
        # target[0:r]切片 会产生新的列表 效率下降
        if target[r] in target[0:r]:
            del target[r]
# 16:02~16:12
list01 = [4,35,7,35,64,7,35]
delete_duplist2(list01)
print(list01)