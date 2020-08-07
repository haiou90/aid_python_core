6.
# 商品列表
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

# --1.定义函数,打印所有商品信息,
# --格式：商品编号xx,商品名称xx,商品单价xx.
def print_cid_info():
    for info in list_commodity_infos:
        print(f'商品编号:{info["cid"]},商品名称:{info["name"]},商品单价:{info["price"]}')

print_cid_info()

# --2.定义函数,打印商品单价小于2万的商品信息
def print_cid_price_lt_2w():
    for info in list_commodity_infos:
        if info["price"] < 20000:
            print(f'商品编号:{info["cid"]},商品名称:{info["name"]},商品单价:{info["price"]}')

print_cid_price_lt_2w()

# --3.定义函数,打印所有订单中的商品信息,
# --格式：商品名称xx,商品单价:xx,数量xx.
def print_info_in_order():
    for emp in list_orders:
        for info in list_commodity_infos:
            if emp["cid"] == info["cid"]:
                print(f'商品名称:{info["name"]},商品单价:{info["price"]},数量:{emp["count"]}')
print_info_in_order()
# --4.定义函数,查找最贵的商品(使用自定义算法,不使用内置函数)
def max_value_cmmodity():
    max_value = list_commodity_infos[0]
    for i in range(1,len(list_commodity_infos)):
        if max_value["price"] < list_commodity_infos[i]["price"]:
            max_value = list_commodity_infos[i]

    print(f'商品编号:{max_value["cid"]},商品名称:{max_value["name"]},商品单价:{max_value["price"]}')
max_value_cmmodity()
# --5.定义函数,根据单价对商品列表升序排列
def asending_price_list():
    for r in range(len(list_commodity_infos)-1):
        for c in range(r+1,len(list_commodity_infos)):
            if list_commodity_infos[r]["price"] < list_commodity_infos[c]["price"]:
                list_commodity_infos[r],list_commodity_infos[c] =list_commodity_infos[c],list_commodity_infos[r]

asending_price_list()
print(list_commodity_infos)