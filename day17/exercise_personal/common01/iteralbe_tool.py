class IterableHelper:
    @staticmethod
    def find(iterable,func):
         for item in iterable:
            if func(item):
             yield item


class IterableHelper01:
    @staticmethod
    def find01(iterable,func):
        for emp in iterable:
            if func(emp):
                return emp
class IterableHelper02:
    @staticmethod
    def find02(iterable,func):
        for emp in iterable:
            yield func(emp)

class IterableHelper03:
    @staticmethod
    def find03(iterable,func):
        for emp in iterable:
            yield func(emp)