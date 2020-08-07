"""
 老王很不幸,买了一箱有虫子(1只)的苹果
        虫子吃完一个苹果再吃另外一个苹果
        在终端中输入苹果数量(个),虫子吃苹果的速度(小时/个),经过时间(小时)
        请打印没有被虫子吃过的苹果数量（整数,最小也是0）
"""
apple = int(input("请输入苹果的数量:"))
insect_speed = float(input("请输入虫子吃苹果的速度(小时/个):"))
duration = float(input("请输入经过的时间:"))


# if duration % insect_speed == 0:
#     apple_left = apple - duration / insect_speed
#     if apple_left > 0:
#         print("剩余苹果" + str(apple_left))
#     else:
#         print("剩余苹果为0")
# else:
#     apple_left = int(apple - duration / insect_speed - 1)
#     if apple_left > 0:
#         print("剩余苹果" + str(apple_left))
#     else:
#         print("剩余苹果为0")


apple_left = int(apple - duration / insect_speed)
if apple_left > 0:
    print("剩余苹果" + str(apple_left))
else:
    print("剩余苹果为0")