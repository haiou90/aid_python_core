while True:
    state = "奇数" if int(input("请输入一个整数：")) % 2 else "偶数"
    print(state)

    if input("请输入y继续:") != "y":
        break