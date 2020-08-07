"""
7. 判断一个字符串是否是回文
    例如：上海自来水来自海上
         山西运煤车煤运西山
    思路：正序与倒序相同
    提示：反向切片[::-1]
"""
list01 = "上海自来水车来自海上"
# list02 = "山西运煤车煤运西山"
# list03 = list01[::-1]
# for i in range(len(list01)):
#     if list01[i] != list03[i]:
#         print("不是回文")
#         break
# else:
#     print("回文")

if list01 == list01[::-1]:
    print("是回文")
else:
    print("不是回文")

