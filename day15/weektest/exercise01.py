"""
1. 创建函数，生成指定行数的杨辉三角。
   杨辉三角：
   每行端点与结尾的数为1，每个数是它左上方和右上方的数的和
   输入：6
   输出：
        [
                   [1],
                  [1, 1],
                 [1, 2, 1],
                [1, 3, 3, 1],
              [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1]
        ]

"""
# def creat_pascal_triangle(count):
#     list_triangel = [[1],[1,1]]
#     for r in range(2,count):
#         list_add = [1,1]
#         for i in range(1,r):
#             list_add.insert(i,list_triangel[r-1][i-1] + list_triangel[r-1][i])
#         list_triangel.append(list_add)
#     return list_triangel
#
#
# print(creat_pascal_triangle(5))

# def creat_pascal_triangle(count):
#     list_triangel = [[1]]
#     for r in range(1,count):
#         list_add = [1,1]
#         for i in range(1,r):
#             list_add.insert(i,list_triangel[r-1][i-1] + list_triangel[r-1][i])
#         list_triangel.append(list_add)
#     return list_triangel
#
# result = creat_pascal_triangle(5)
# for item in result:
#     print(item)
#     print()

def creat_pascal_triangle(count):
    list_triangel = []
    for r in range(count):
        list_add = [None]*(r+1)
        list_add[0] = 1
        list_add[-1]= 1
        for i in range(1,r):
            list_add[i] = list_triangel[r-1][i-1] + list_triangel[r-1][i]
        list_triangel.append(list_add)
    return list_triangel

result = creat_pascal_triangle(5)
for item in result:
    print(item)
    print()