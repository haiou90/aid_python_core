"""\在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
   提示：使用字典存储数据
   """
dict_color = {"R":"红色", "G":"绿色", "B":"蓝色","A":"透明度"}
color_print = input("请输入颜色：")
if color_print in dict_color:
    print(dict_color[color_print])
else:
     print("颜色不存在")

# for key, value in dict_color.items():
#     color_print = input("请输入颜色：")
#     if color_print in dict_color:
#         print("%s -> %s" % (key, value))
#     else:
#         print("颜色不存在")


# for color_print, value in dict_color.items():
#     color_print = input("请输入颜色：")
#     print("%s -> %s" % (color_print, value))
# else:
#     print("颜色不存在")
# for key in dict_color:
# for value in dict_color.values():
# for key, value in dict_color.values():