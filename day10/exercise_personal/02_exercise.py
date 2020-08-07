class Wife:
    count = 0
    @classmethod
    def print_count(cls):
        print(cls.count)

    def __init__(self, name=""):
        self.name= name
        Wife.count += 1


w01 = Wife("建宁")
w02 = Wife("双儿")
w03 = Wife("苏荃")
Wife.print_count() # 3

