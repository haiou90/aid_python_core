class Grenades:
    def explode(self,victim):
        print("手雷爆炸")
        victim.damage()

class Victim:
    def damage(self):
        pass

class Player(Victim):
    def damage(self):
        print("玩家受伤,流血")

class Enemy(Victim):
    def damage(self):
        print("敌人受伤,碎屏")

gre = Grenades()
player = Player()
enemy = Enemy()
gre.explode(player)
gre.explode(enemy)