"""
5. 将列表中整数的个位不是5和3的数字存入另外一个列表
   list03 = [25, 63, 27, 75, 70, 83, 27]
   结果:[27, 70, 27]
"""
list03 = [25, 63, 27, 75, 70, 83, 27]
# list04 = []
# for num in list03:
#     if num % 10 == 3 or num % 10 == 5:
#         continue
#     list04.append(num)
# print(list04)

# list03 = [25, 63, 27, 75, 70, 83, 27]
# for num in list03:
#     if num % 10 == 3 or num % 10 == 5:
#        list03.remove(num)
# print(list03)
# #返回结果[63, 27, 70, 27]，为啥63没有删除

list03 = [25, 63, 27, 75, 70, 83, 27]
for i in range(len(list03)-1, -1, -1):
    if list03[i] % 10 == 3 or list03[i] % 10 == 5:
        del list03[i]
print(list03)
#返回结果[25, 63, 27, 75, 70, 83, 27] 全都没删除


# list04 = list03[:]
# for i in range(-len(list03), -1, -1):
#     if list03[i] % 10 == 3 or list03[i] % 10 == 5:
#         del list03[i]
#         print(list03)
