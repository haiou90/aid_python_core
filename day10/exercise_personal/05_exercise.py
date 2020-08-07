class Mouse:
    def __init__(self, brand, price, weight, color):
        self.brand = brand
        self.price = price
        self.weight = weight
        self.color = color
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if len(value) <= 6:
            self.__brand = value
        else:
            raise Exception("不行")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if 0 <= value <= 10000:
            self.__price = value
        else:
            raise Exception("不行")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 0 <= value <= 10000:
            self.__weight = value
        else:
            raise Exception("不行")


m01 = Mouse("罗技", 200, 142, "黑色")
print(m01.price)
