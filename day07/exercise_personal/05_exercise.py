# list_max = list_all[0]
# for i in range(1, len(list_all)):
#     if list_max < list_all[i]:
#         list_max = list_all[i]
# print(list_max)

dict_commodity_infos = {
1001: {"name": "屠龙刀", "price": 10000},
1002: {"name": "倚天剑", "price": 10000},
1003: {"name": "金箍棒", "price": 52100},
1004: {"name": "口罩", "price": 20},
1005: {"name": "酒精", "price": 30},
}

list_orders = [
{"cid": 1001, "count": 1},
{"cid": 1002, "count": 3},
{"cid": 1005, "count": 2},
]
# assume = list_orders[0]["count"]
# for order in list_orders:
#     if assume < order["count"]:
#         assume = order["count"]
#         cid = order["cid"]
#         commodity = dict_commodity_infos[cid]
# print("商品编号%d,商品名称%s" %(order["cid"],commodity["name"])

max_value = list_orders[0]
for i in range(1, len(list_orders)):
    if max_value["count"] < list_orders[i]["count"]:
        max_value = list_orders[i]
print(max_value)
