"""
  列表推导式 嵌套
"""
list01 = ["香蕉","苹果","哈密瓜"]
list02 = ["雪碧","可乐","牛奶","绿茶"]
# list_result = []
# for r in list01:
#     for c in list02:
#         list_result.append(r+c)
# print(list_result)
list_result = [r+c for r in list01 for c in list02]
print(list_result)

list_color = ["红桃","黑桃","方片","梅花"]
list_number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# list_poker = []
# for r in list_color:
#     for c in list_number:
#         list_poker.append((r,c))
# print(list_poker)

list_poker = [(r , c) for r in list_color for c in list_number]
print(list_poker)