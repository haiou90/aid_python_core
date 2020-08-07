class Car:
    def __init__(self, brand, speed):
        self.brand =brand
        self.speed =speed

class ElectricityCar(Car):
    def __init__(self, brand, speed, capacity, power):
        super().__init__(brand,speed)
        self.capacity = capacity
        self.power = power

ec01 = ElectricityCar("TESLA",500,700,200)
ca01 = Car("BYD",450)
print(ec01.brand)
print(ec01.speed)
print(ec01.capacity)
print(ec01.power)
print(ca01.brand)

