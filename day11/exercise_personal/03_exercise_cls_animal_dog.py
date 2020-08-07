class Animal:
    def eat(self):
        print("吃饭")


class Dog(Animal):
    def run(self):
        self.eat()
        print("跑了")

class Bird(Animal):
    def fly(self):
        print("飞")

dog1 = Dog()
bird1 = Bird()
dog1.eat()
dog1.run()
animal1 = Animal()
animal1.eat()

print(isinstance(dog1,Dog))
print(isinstance(dog1,Animal))
print(isinstance(dog1,Bird))
print(isinstance(animal1,Dog))

print(issubclass(Dog,Dog))
print(issubclass(Dog,Animal))
print(issubclass(Dog,Bird))
print(issubclass(Animal,Bird))

print(type(dog1) == Dog)
print(type(dog1) == Animal)
print(type(dog1) == Bird)
print(type(animal1) == Bird)