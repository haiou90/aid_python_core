"""
11.
    (1).在终端中录入秒数,  80
       计算几分钟零几秒存入列表[分,秒]   [1,20]

    (2).将第一步重复3次,将每个列表再存入列表
        请输入秒：80
        请输入秒：90
        请输入秒：100
        [[1, 20], [1, 30], [1, 40]]

    (3).打印第二步所有时间,一行一个,格式:x分零x秒
        1分零20秒
        1分零30秒
        1分零40秒
"""
list_second = []
list_print = []
for i in range(3):
    total_seconds = int(input("请录入秒数:"))
    minute = total_seconds // 60
    second = total_seconds % 60
    #每次循环产生一个新列表
    list_second = [minute, second]
    list_print.append(list_second)
for list_second in list_print:
    print("%.2d分零%.2d秒" % (list_second[0], list_second[1]))
    # print(f"{list_second[0]}分零{list_second[1]}秒" % (minute[0], second[1]))