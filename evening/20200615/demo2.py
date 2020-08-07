class MyWife:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if 20>value or value>30:
            raise ValueError('我不要')
        self.__age = value


wife1 = MyWife('翠花',20)
# 规范用户使用
# 20<age<30 休息20:00~20:10
wife2 = MyWife('小乔',2000)
# wife2.age = 2000
