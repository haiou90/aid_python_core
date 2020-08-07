# 斐波那契数列：从第3项开始，每一项都等于前两项之和。
#     1, 1, 2, 3, 5, 8, 13, 21..
# 定义函数，根据长度获取斐波那契数列。
def get_fib(length):#length = 6
    #保存数列前两项内容
    #[1,1]  1+1 = 2
    #[1,1,2] 1+2 = 3
    #[1,1,2,3] 2+3 = 5
    #[1,1,2,3,5] 3+5 = 8
    seq = [1, 1]
    if length <=2:
        return seq
    for i in range(length-2):# i = 0 1 2 3
        # seq.append(seq[i]+seq[i+1])
        seq.append(seq[-1]+seq[-2])
    return seq

print(get_fib(10))
