"""
使用面向对象思想,描述下列情景.
    -- (1)小明使用手机打电话
    -- (2)小明一次请多个保洁打扫卫生
          效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
          区别:保洁与保洁列表
    -- (3)玩家攻击(攻击力)多个敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
          区别:敌人与敌人列表
    -- (4)
        张无忌教赵敏九阳神功
        赵敏教张无忌玉女心经
        张无忌工作挣了5000元
        赵敏工作挣了10000元
        提示：张无忌与赵敏是数据不同
             行为相同
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self,telephone):
        print(self.name,"使用")
        telephone.call()

class Phone:
    def call(self):
        print("手机打电话")

xm = Person("小明")
iphone = Phone()
xm.use(iphone)
"""
小明一次请多个保洁打扫卫生
          效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
          区别:保洁与保洁列表
"""

class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self,phone):
        for telephone in phone:
            print(self.name, "使用")
            telephone.call()

class Phone:
    def __init__(self, name):
        self.name = name
    def call(self):
        print(self.name,"手机打电话")

xm = Person("小明")
phone = [Phone("apple"),
          Phone("huawei"),
          Phone("xiaomi"),
          Phone("vivo")]
xm.use(phone)

"""
玩家攻击(攻击力)多个敌人，敌人受伤(减血)后可能si亡(播放si亡动画)
          区别:敌人与敌人列表
"""
class Player:
    def __init__(self, atk = 50):
        self.atk = atk
    def attack(self,enemies):
        for enemy in enemies:
            print("攻击敌人")
            enemy.damage(self.atk)

class Enemy:
    def __init__(self, name,hp = 100):
        self.name = name
        self.hp = hp
    def damage(self,value):
        print(self.name,"受伤")
        self.hp -= value
        if self.hp <= 0:
            print("播放死亡东辉")

play01 = Player()
enemy = [Enemy("小怪兽1"),
        Enemy("小怪兽2"),
        Enemy("小怪兽3"),
        Enemy("小怪兽4"),
         ]
play01.attack(enemy)


"""
 张无忌教赵敏九阳神功
        赵敏教张无忌玉女心经
        张无忌工作挣了5000元
        赵敏工作挣了10000元
        提示：张无忌与赵敏是数据不同
             行为相同
"""
class Teacher:
    def __init__(self, teacher):
        self.teacher = teacher


    def teach(self,learner):
        print(self.teacher,"教")
        learner.learn()

    def work(self,earner):
        print(self.teacher,"工作")
        earner.earn()


class Learner:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def learn(self):
        print(self.name,self.type)


class MakeMoney:
    def __init__(self, money):
        self.money = money

    def earn(self):
        print("赚了",self.money)

teacher01 = Teacher("张无忌")
learner01 = Learner("赵敏","九阳神功")
teacher01.teach(learner01)
teacher02 = Teacher("赵敏")
learner02 = Learner("张无忌","玉女心经")
teacher02.teach(learner01)
maker01 = MakeMoney(5000)
teacher01.work(maker01)
maker02 = MakeMoney(10000)
teacher02.work(maker02)
