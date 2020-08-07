# 1. 创建函数，生成指定行数的杨辉三角。
#     杨辉三角：
#     每行端点与结尾的数为1，每个数是它左上方和右上方的数的和
#     输入：6
#     输出：
#          [
#                     [1],
#                    [1, 1],
#                   [1, 2, 1],
#                  [1, 3, 3, 1],
#                [1, 4, 6, 4, 1],
#              [1, 5, 10, 10, 5, 1]
#          ]

#  1 yanghui[2][0]  yanghui[2][1]
#  3  yanghui[3][1]
#  yanghui[3][0]   yanghui[3][1]
#  4 yanghui[4][1]

# yanghui[row-1][i-1]+yanghui[row-1][i]
# yanghui[row][i]
def get_yang_hui(row_count):#row_count = 6
    yanghui = []
    for row_index in range(row_count):#row_index 0~5
        row = [None] * (row_index+1)
        #设置每一行的内容
        #设置首尾
        row[0],row[-1] = 1,1
        #设置中间元素
        for i in range(1,row_index):
            row[i] = yanghui[row_index-1][i-1] + yanghui[row_index-1][i]
        yanghui.append(row)
    return yanghui

print(get_yang_hui(6))