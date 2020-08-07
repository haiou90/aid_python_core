# 5.质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
#     定义函数，获取指定范围内的所有质数。
# 输入：2,20
# 输出：[2, 3, 5, 7, 11, 13, 17, 19]

#5  (234)
#8  (234567)
#n  (2~n-1)
def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            #不是质数
            return False
    return True
# print(is_prime(5))

def get_prime(begin,end):
    return [num for num in range(begin,end+1) if is_prime(num)]
    # result_list = []
    # for num in range(begin,end+1):
    #     if is_prime(num):
    #         result_list.append(num)
    # return result_list
print(get_prime(2,20))