"""
        如果是vip客户,消费小于等于500,享受85折
                    消费大于500,享受8折
        如果不是vip客户,消费大于等于800,享受9折
                      消费小于800,原价
        在终端中输入账户类型,消费金额,计算折扣.
"""


# account_type = input("请输入账户类型:")
# consumption_amount = float(input("请输入消费金额:"))
#
# if account_type == "vip":
#     if consumption_amount <= 500:
#         print("折扣为85折")
#     else:
#         print("折扣为8折")
# else:
#     if consumption_amount >= 800:
#         print("折扣为9折")
#     else:
#         print("原价")

def calculate_discount(account_type, consumption_amount):
    """
    计算购买商品折扣
    :param account_type:账户类型，是否vip
    :param consumption_amount: 消费金额
    :return: 返回折扣数
    """
    # if account_type == "vip":
    #     if consumption_amount <= 500:
    #         return 0.85
    #     return 0.8
    # else:
    #     if consumption_amount >= 800:
    #         return 0.9
    #     return 1

    if account_type == "vip":
        return 0.85 if consumption_amount <= 500 else 0.8
    return 0.9 if consumption_amount >= 800 else 1

result = calculate_discount("vip", 1000)
print(result)


