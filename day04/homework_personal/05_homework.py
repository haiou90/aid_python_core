"""
8. (选做)一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)
    -- 全过程总共移动多少米?
   提示:
       数据/运算
"""
height = 100
number = 0
total_height = 100
while height / 2 > 0.01:
    height /= 2
    number += 1
    total_height += 2 * height
print("总共弹起%d次,全过程总共移动%.2f米" % (number, total_height))