"""
1. 玩家攻击敌人,敌人受伤(播放动画)
2. 玩家(攻击力)攻击敌人(血量),
敌人受伤(播放动画,血量减少)
3. 敌人(攻击力)还能攻击玩家(血量),
玩家受伤(碎屏,血量减少)
"""

class Player:
    def __init__(self, name=None, attack_sp=None, blood=None):
        self.name = name
        self.attack_sp = attack_sp
        self.blood = blood

    def attack(self,against):
        print(self.name,"攻击敌人")
        against.injured()

class Enemy:
    def injured(self):
        print("敌人受伤(播放动画)")

player = Player("prayer")
enemy = Enemy()
player.attack(enemy)


class Player:
    # total_blood = 100
    # total_attack_sp = 100
    # @classmethod
    # def print_attack_sp(cls):
    #     print("剩余攻击力", cls.total_attack_sp)
    def __init__(self, attack_sp=None,blood=None):
        self.attack_sp = attack_sp
        self.blood = blood

    def attack(self,enemy):
        print("攻击敌人")
        enemy.damage(self.attack_sp)

    def damage(self, value):
        print("玩家受伤,血量减小(碎屏)")
        self.blood -= value
        print("玩家血量是", self.blood)

        # Player.total_blood -= 10
        # Player.total_attack_sp -= 10
        # Player.print_attack_sp()

class Enemy:
    # total_bloods = 100
    # @classmethod
    # def print_blood(cls):
    #     print("剩余血量",cls.total_bloods)
    def __init__(self,blood,attack_sp):
        self.blood = blood
        self.attack_sp = attack_sp
    def attack(self,player):
        print("敌人攻击玩家")
        player.damage(self.attack_sp)
    def damage(self,value):
        print("敌人受伤,血量减小(播放动画)")
        self.blood -= value
        print("敌人血量是", self.blood)
        # Enemy.total_bloods -= 10
        # Enemy.print_blood()

player = Player(500,50)
enemy = Enemy(100,10)
player.attack(enemy)
enemy.attack(player)
# Enemy.print_blood()
# Player.print_attack_sp()