
"""
    计算梯形面积
    在终端中获取上底,下底和高
    输出面积
    公式：(上底 + 下底) 乘以 高 除以 2
"""
bottom_up = float(input("请输入上底:"))
bottom_down = float(input("请输入下底:"))
height = float(input("请输入高:"))

area = (bottom_up + bottom_down) * height / 2

print("梯形面积"+ str(area))

