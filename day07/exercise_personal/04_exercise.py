""" 商品字典
dict_commodity_infos = {
1001: {"name": "屠龙刀", "price": 10000},
1002: {"name": "倚天剑", "price": 10000},
1003: {"name": "金箍棒", "price": 52100},
1004: {"name": "口罩", "price": 20},
1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
{"cid": 1001, "count": 1},
{"cid": 1002, "count": 3},
{"cid": 1005, "count": 2},
]

# 1.打印所有商品信息,
# 格式：商品编号xx,商品名称xx,商品单价xx.

# 2. 打印所有订单中的信息,
# 格式：商品编号xx,购买数量xx.
"""
dict_commodity_infos = {
1001: {"name": "屠龙刀", "price": 10000},
1002: {"name": "倚天剑", "price": 10000},
1003: {"name": "金箍棒", "price": 52100},
1004: {"name": "口罩", "price": 20},
1005: {"name": "酒精", "price": 30},
}

for cid, info in dict_commodity_infos.items():
    print("商品编号%d,商品名称%s,商品价格%d" %(cid, info["name"], info["price"]))
# print("商品编号%d,商品名称%s,商品单价%d." % (cid, info["name"], info["price"]))
#     print(f"商品编号{cid},商品名称{info['name']},商品单价{info['price']}")

list_orders = [
{"cid": 1001, "count": 1},
{"cid": 1002, "count": 3},
{"cid": 1005, "count": 2},
]
#
# for order in list_orders:
#     print("商品编号%d,购买数量%d" %(order["cid"],order["count"]))
#
# 3. 打印商品单价小于2万的商品信息
# 格式：商品编号xx,商品名称xx,商品单价xx.

for cid, info in dict_commodity_infos.items():
    if info["price"] < 20000:
        print("商品编号%d,商品名称%s,商品价格%d" %(cid, info["name"], info["price"]))
# 4. 打印所有订单中的商品信息,
# 格式：商品名称xx,商品单价:xx,数量xx.
for order in list_orders:
    cid = order["cid"] #字典中键 cid 对应的值
    commodity = dict_commodity_infos[cid] #订单中编号对应的商品
                                        # 字典的键 对应的值（仍是字典）
    print(commodity)
    # commodity["name"]
    # commodity["price"]
    # print("商品名称%s,商品编号%d,购买数量%d" %(commodity["name"], commodity["price"], order["count"]))
# for cid, info in dict_commodity_infos.items():
#     print("商品编号%d,商品名称%s,商品价格%d" %(cid, info["name"], info["price"]))

