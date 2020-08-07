"""
    智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
    天才：140以上（包含）
    超常：120-139之间（包含）
    聪慧：110-119之间（包含）
    正常：90-109之间（包含）
    迟钝：80-89之间（包含）
    低能：80以下
    根据心理年龄与实际年龄，打印智商等级。
"""
# ma = int(input("请输入你的心里年龄："))
# ca = int(input("请输入你的实际年龄："))
# iq = ma / ca * 100
#
# if iq >= 140:
#     print("天才")
# elif iq >= 120:
#     print("超常")
# elif iq >= 110:
#     print("聪慧")
# elif iq >= 90:
#     print("正常")
# elif iq >= 80:
#     print("迟钝")
# else:
#     print("低能")

def calculate_iq(ma,ca):
    """
    计算智商
    :param ma: 心里年龄
    :param ca: 实际年龄
    :return: 返回智商值
    """
    iq = ma / ca * 100
    if iq >= 140:
        return ("天才") #退出函数
    if iq >= 120:
        return("超常")
    if iq >= 110:
        return("聪慧")
    if iq >= 90:
        return("正常")
    if iq >= 80:
        return("迟钝")
    return("低能")
result = calculate_iq(100,80)
print(result)