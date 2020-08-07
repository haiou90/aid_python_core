# 2.  "水仙花数":各位数字幂次方和等于该数本身
#     定义函数，根据位数计算水仙花数
#     输入：3
#     输出：[153, 370, 371, 407]
#     153 = 1**3+5**3+3**3
#     '153'

def check_num(num):
    '''
    判断数字num是不是水仙花数
    :param num: 数字
    :return: 布尔值
    '''
    str_number = str(num)#153  -->  '153'
    power = len(str_number)# 3
    sum = 0
    for item in str_number:
        sum += int(item) ** power #sum = 1**3+5**3+3**3
    return sum == num


def get_list(n):
    '''
    获取指定位数的水仙花数列表
    :param n: 位数 整数
    :return: 列表
    '''
    # res = []
    # for i in range(10**(n-1),10**n):
    #     if check_num(i):
    #         res.append(i)
    return [num for num in range(10**(n-1),10**n) if check_num(num)]

res = get_list(3)
print(res)

# res = check_num(153)
# print(res)