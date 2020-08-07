"""
    以万物皆对象的思想，洞察你身边的客观事物,挑选2个创建类和对象.
    目标:使用计算机描述生活
    体会:现实事物  -抽象->  类  -具体-> 对象
"""
class Architecture():
    def __init__(self,type,area,price):
        self.type = type
        self.area = area
        self.price = price

    def buy(self):
        print("购买",self.type,self.price)

house01 = Architecture("两局","90平",1000000)
house01.buy()


class Car():
    def __init__(self,type,color,price):
        self.type = type
        self.color = color
        self.price = price

    def buy(self):
        print("购买",self.type,self.price)

private_car01 = Car("新能源","黑色",100000)
private_car01.buy()
print(private_car
01.color)