class Dog:
    def __init__(self, type, name, age, weight):
        self.type = type
        self.name = name
        self.age = age
        self.weight =weight

    def eat(self):
        print(self.type,"eat")

    def yell(self):
        print(self.type,"yell")



d01 = Dog("金毛","毛毛",3,30)
d02 = Dog("牧羊","壮壮",2,100)
# d01.type = "泰迪"
d01.eat()
d02.yell()