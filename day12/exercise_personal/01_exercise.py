message = int(input("请输入："))
# if message != "": # 输入的不是空
# if message != 0:
if message:  # bool(message) 输入的有值
    print("您输入的是:" + message)
else:
    print("您没有输入")
