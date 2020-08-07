def get_score():
    while True:
        try:
            score = float(input("请输入成绩:"))
            return score
        except:
            print("输入错误请重输")
        # else:
        #     return score


print(get_score())
