class Dog:
    count = 0
    def __init__(self,color):
        self.color = color
        Dog.count += 1

    #方法
    def say(self):
        print('wangwangwang')

    @classmethod
    def total_count(cls):
        print(Dog.count)

#实例化
# taidi = Dog('yellow&white')
#设置对象的属性
# taidi.color = 'yellow&white'
#设置对象的方法(行为)
# taidi.say = say
# erha = Dog('black&white')
# print(taidi.color)
# taidi.say()

Dog.total_count()