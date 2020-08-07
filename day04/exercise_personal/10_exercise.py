"""
1. 在终端中录入一个内容,循环打印每个文字的编码值。
# 2. 循环录入编码值,打印文字.直到输入空字符串,停止。
"""
# while True:
#     code = input("请输入一个内容：")
#     print(ord(code))

while True:
    code = input("请输入一个数字：")
    if code == " ":
        break
    code = int(code)
    print(chr(code))