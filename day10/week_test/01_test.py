"""
1,1,2,3,5,8,13,21
"""

def fibonacci_sequence(count):
    sum_seq = [1,1]
    # sum = 0
    for i in range(2,count):
        sum = sum_seq[i-1]+sum_seq[i-2]
        sum_seq.append(sum)
    # print(sum_seq)
    return sum_seq
# fibonacci_sequence(7)
print(fibonacci_sequence(7))

# def fibonacci_sequence(count):
#     sum_seq = [1,1]
#     for i in range(2,count): #count-2
#         sum = sum_seq[-1]+sum_seq[-2]  #最后两项加后的值新增
#         sum_seq.append(sum)
#     print(sum_seq)
# fibonacci_sequence(7)