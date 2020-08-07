class Enermy:
    def __init__(self,name,blood,attack,protect):
        self.name = name
        self.blood = blood
        self.attack = attack
        self.protect = protect

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self,value):
        if  value < 0:
            value = 0
        elif value >20:
            value = 20
        else:
            self.__blood = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if 1 <= value <= 30:
            self.__attack = value
        else:
            raise Exception("不行")

    @property
    def protect(self):
        return self.__protect

    @protect.setter
    def protect(self, value):
        if 0 <= value <= 20:
            self.__protect = value
        else:
            raise Exception("不行")





e01 = Enermy("王者",80,25,18)
print(e01.blood)