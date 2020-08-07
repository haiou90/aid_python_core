6.
# 商品列表
class Commodity:
    def __init__(self,cid,name,price):
        self.cid =cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001,"屠龙刀",10000),
    Commodity(1002,"倚天剑", 10000),
    Commodity(1003,"金箍棒", 52100),
    Commodity(1004,"口罩",20),
    Commodity(1005,"酒精",30),
]

def print_single_commodity(commodity):
    print(f'商品名称:{commodity.cid},商品单价:{commodity.name},数量:{commodity.price}')
def print_commodity_infos():
    for commodity in list_commodity_infos:
        print_single_commodity(commodity)

print_commodity_infos()

# --2.定义函数,打印商品单价小于2万的商品信息
def print_cid_price_lt_2w():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_single_commodity(commodity)

print_cid_price_lt_2w()


# --4.定义函数,查找最贵的商品(使用自定义算法,不使用内置函数)
def max_value_cmmodity():
    max_value = list_commodity_infos[0]
    for i in range(1,len(list_commodity_infos)):
        if max_value.price < list_commodity_infos[i].price:
            max_value = list_commodity_infos[i]

    print(f'商品编号:{max_value.cid},商品名称:{max_value.name},商品单价:{max_value.price}')
max_value_cmmodity()


# --5.定义函数,根据单价对商品列表升序排列
def asending_price_list():
    for r in range(len(list_commodity_infos)-1):
        for c in range(r+1,len(list_commodity_infos)):
            if list_commodity_infos[r].price < list_commodity_infos[c].price:
                list_commodity_infos[r],list_commodity_infos[c] =list_commodity_infos[c],list_commodity_infos[r]

asending_price_list()
print(list_commodity_infos)
print_commodity_infos()

# 订单列表
class Order:
    def __init__(self,cid, count):
        self.cid = cid
        self.count =count


list_orders = [
    Order(1001, 1),
    Order(1002, 3),
    Order(1005, 2)]

def print_info_in_order():
    for order in list_orders:
        for commodity in list_commodity_infos:
            if order.cid == commodity.cid:
                print(f'商品名称:{commodity.name},商品单价:{commodity.price},数量:{order.count}')
print_info_in_order()


# --3.定义函数,打印所有订单中的商品信息,
# --格式：商品名称xx,商品单价:xx,数量xx.