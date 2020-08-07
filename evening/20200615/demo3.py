class GParent:
    pass

class Parent(GParent):
    def __init__(self,atk,hp):
        self.atk = atk
        self.hp = hp

    def attack(self,target):
        pass

    def damage(self,value):
        pass


#玩家攻击敌人   敌人受伤,还可能死亡

class Player(Parent,GParent):
    def attack(self,target):
        print('黑虎掏心')
        target.damage(self.atk)

    def damage(self,value):
        print('小样你敢打我!')
        self.hp -= value
        if self.hp <= 0:
            print('太菜了')


class Enemy(Parent):
    def attack(self,target):
        print('普通攻击第一式')
        target.damage(self.atk)

    def damage(self,value):
        print('玩家打人啦')
        self.hp -= value
        if self.hp <= 0:
            print('a~~~~')
            print('爆装备')

p1 = Player(50,100)
e1 = Enemy(10,100)
p1.attack(e1)
e1.attack(p1)
e1.attack(p1)
e1.attack(p1)
e1.attack(p1)
p1.attack(e1)
