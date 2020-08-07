"""
     一张纸的厚度是0.01毫米
     请计算，对折多少次超过珠穆朗玛峰(8844.43米).
"""
# 数据：厚度  与 高度对比    次数
# 处理：累乘               累加
# thickness = 0.01 / 1000
# thickness = 0.00001
thickness = 1e-5
num = 0
# 厚度不超过珠穆朗玛峰则对折
sum_thickness = 0
while thickness < 8844.43:
    thickness *= 2  # 累计对折厚度(厚度翻倍)
    print(thickness)
    num += 1  # 累加对折次数
    print(num)
    # sum_thickness += thickness
    # if num == 10:
    #     print("对折10次" + str(sum_thickness))
    # if num == 20:
    #     print("对折20次" + str(sum_thickness))
    # if num == 30:
    #     print("对折20次" + str(sum_thickness))

print("对折" + str(num) + "次.")
