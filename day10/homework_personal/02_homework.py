"""
5.创建技能类(技能名称,攻击比率,消耗法力,持续时间)
  保证数据范         0 - 2  0 - 80  0 - 120
"""


class Profession:
    def __init__(self, name, attack, cost, duration):
        self.name = name
        self.attack = attack
        self.cost = cost
        self.duration = duration

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if 0 <= value <= 2:
            self.__attack = value
        else:
            raise Exception("玩完了")

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if 0 <= value <= 80:
            self.__cost = value
        else:
            raise Exception("玩完了")

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if 0 <= value <= 120:
            self.__duration = value
        else:
            raise Exception("玩完了")

pro01 = Profession("一阳指", 2, 50, 100)
print(pro01.name)
