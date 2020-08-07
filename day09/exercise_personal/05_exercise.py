"""
    面向对象的思考步骤：
        现实事物  -抽象化->  类  -具体化-> 对象

    # int 类的对象
    a = 10
    # str 类的对象
    b = "悟空"
    # list 类的对象
    c = [1,2,3]

    语法：
    class 类名:　
        def __init__(self, 参数):
            self.数据 = 参数　

"""


class Wife:
    # 数据：名词性的描述
    def __init__(self, name, face_score, money=0.0):
        self.name = name
        self.money = money
        self.face_score = face_score

    # 行为：动词性的功能
    def work(self):
        print(self.name, "工作")

# 创建对象(自动调用__init__函数)
w01 = Wife("双儿",97,2000)
# 自动传递对象 work(w01)
w01.work()

class Phone:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.clolor = color

    def telephone(self):
        print("通话",[10])
phone01 =  Phone("苹果",5000,"深空灰")
phone02 =  Phone("华为",8000,"深空灰")

phone01.telephone()
phone02.telephone()
