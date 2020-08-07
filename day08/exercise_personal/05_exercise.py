# amount = int(input("请输入两数:"))
# jin = amount // 16
# liang = amount % 16
# print(str(jin) + "斤零" + str(liang) + "两")

def computer_jin_liang(amount):
    """
    计算斤两
    :param amount:输入总重量
    :return: 返回斤两元组
    """
    jin = amount // 16
    liang = amount % 16
    return jin, liang

result = computer_jin_liang(30)
print(result)