"""
10.(选做)彩票模拟器
    双色球：
        红球：6个,1-33之间（包含）,不能重复
        蓝球：1个,1--16之间（包含）
    提示：列表就是彩票(前六个元素就是红球)
        -- 创建随机彩票(一个列表,前六个是红球,最后一个是蓝球)
        -- 在终端中购买彩票(提示：号码已经存在,号码超过范围)
"""

import random

red_ball = random.randint(1,33)
blue_ball = random.randint(1,16)

list_lottery = [red_ball, red_ball, red_ball, red_ball, red_ball, red_ball, blue_ball]
print(list_lottery)
# list_buy =[]
# for i in range(list_lottery):
#     ball_number = input("请输入一个号码:")
#     if ball_number in list_buy:
#         print("号码已存在")
#         continue
#     if ball_number > 33:
#         print("超出范围")
#         continue
#     list_buy.append(ball_number)

list_buy =[]
while len(list_buy)<6
    number = random.randint(1,33)
    if number not in list_buy:
        list_buy.append(number)