# 3. 定义函数，判断二维数字列表中是否存在某个数字
# 输入：二维列表、11
# 输出：True
def is_exists(double_list,target):
    for line in double_list:
        if target in line:
            return True
    return False


double_list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
print(is_exists(double_list,11))