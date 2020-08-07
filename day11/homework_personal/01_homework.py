"""
通过属性限制数据范围,体会属性的继承
    父类：车(品牌，速度)
                 0-280
    创建子类：电动车(电池容量,充电功率)
                  0 - 50000  200 - 250
"""
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 280:
            self.__speed = value
        if value < 0:
            self.__speed = 0
        if value > 280:
            self.__speed = 280

class ElectricCar(Car):
    def __init__(self, brand, speed, capacity, power):
        super().__init__(brand, speed)
        self.capacity = capacity
        self.power = power
        # super().speed 调用父类对象尽量采用super,不建议采用self.speed

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if 0 <= value <= 50000:
            self.__capacity = value
        else:
            raise Exception("超容量了")

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if 200 <= value <= 250:
            self.__power = value
        else:
            raise Exception("超功率了")

tesla = ElectricCar("tesla",200,10000,220)
print(tesla.brand)
print(tesla.speed)
print(tesla.capacity)
print(tesla.power)