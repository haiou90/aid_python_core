"""
"水仙花数":各位数字幂次方和等于该数本身
定义函数，根据位数计算水仙花数
输入：3
输出：[153, 370, 371, 407]
"""
#
# for m in range(100,1000):
#     if (m%10)**3 + int((m/10)%10)**3+ int(m/100)**3  == m:
#         print(m)

# for m in range(100,10000):
#     if int(m/1)%10**4 + int(m/10)%10**4 + int(m/100)%10**4 + int(m/1000)%10**4 == m:
#         print(m)
# for m in range(100,1000000):
#     n = len(str(m))
#     digits = []
#     for i in range(n):
#         d = int(m/10**i)%10
#         digits.append(d)
#         if sum([d**n for d in digits]) == m:
#             print(m)

def check_num(num):
    str_num = str(num)
    power = len(str_num)
    sum = 0
    for item in str_num:
        sum += int(str_num) ** power
    return sum == num
def get_list(n):
    res = []
    for i in range(10**(n-1),10**n):
        if check_num(i):
            res.append()
    return res


print(get_list(3))
