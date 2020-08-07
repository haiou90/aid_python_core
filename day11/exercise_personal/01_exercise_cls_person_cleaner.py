"""
小明请保洁打扫卫生
"""
class Person:
    def __init__(self, name=None):
        self.name = name

    def invite(self):
        print(self.name,"请")
        clean = Cleaner()
        clean.work()

class Cleaner:
    def work(self):
        print("保洁打扫卫生")

xm = Person("小明")
xm.invite()

class Person:
    def __init__(self, name=None):
        self.name = name
        self.clean = Cleaner()

    def invite(self):
        print(self.name,"请")
        self.clean.work()

class Cleaner:
    def work(self):
        print("保洁打扫卫生")

xm = Person("小明")
xm.invite()


class Person:
    def __init__(self, name=None):
        self.name = name


    def invite(self,clean):
        print(self.name,"请")
        clean.work()


class Cleaner:
    def work(self):
        print("保洁打扫卫生")

xm = Person("小明")
clean = Cleaner()
xm.invite(clean)