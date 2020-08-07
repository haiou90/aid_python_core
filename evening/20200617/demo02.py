#手雷爆炸 可能伤害玩家/敌人
class Grenade:
    def __init__(self,atk=50):
        self.atk = atk
    def explode(self,target):
        target.damage(self.atk)


class AttackTarget:
    def damage(self,value):
        pass
# 休息19:57~20:05
class Player(AttackTarget):
    def __init__(self,hp=100):
        self.hp = hp

    def damage(self,value):
        self.hp -= value
        print('a~~~玩家受伤啦')


class Enemy(AttackTarget):
    def __init__(self,hp=50):
        self.hp = hp

    def damage(self,value):
        self.hp -= value
        print('敌人受伤啦')

g1 =  Grenade()
g1.explode(Player())
g1.explode(Enemy())