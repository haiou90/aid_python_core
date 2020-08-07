#老张开车去东北
#坐飞机
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,vehicle,postion):
        print(self.name,'去',postion)
        #多态   调用父类方法
        vehicle.transport()

#继承  隔离变化
class Vehicle:
    def transport(self):
        pass

class Car(Vehicle):
    #多态  重写父类内容
    def transport(self):
        print('小汽车滴滴滴')

class Airplane(Vehicle):
    def transport(self):
        print('飞机搜嗖嗖')

# laozhang = Person('老张')
# c1 = Car()
# p1 = Airplane()
# laozhang.go_to(p1,'东北')
# laozhang.go_to(c1,'东北')