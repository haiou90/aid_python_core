"""
    common/
        iterable_tools.py
    可迭代对象工具
"""


class IterableHelper:
    """
        可迭代对象助手
    """

    @staticmethod
    def find_all(iterable, func):
        for item in iterable:
            if func(item):
                yield item

    @staticmethod
    def find_single(iterable, func):
        for emp in iterable:
            if func(emp):
                return emp

    @staticmethod
    def select(iterable, func):
        for emp in iterable:
            yield func(emp)

    @staticmethod
    def delete_all(iterable, func):
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            # if iterable[i].money < 15000:
            # $调用传入的函数lambda
            if func(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, func):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            # if max_value.money < iterable[i].money:
            # if xx(max_value) < xx(iterable[i]):
            if func(max_value) < func(iterable[i]):    #两次调用同一个函数
                max_value = iterable[i]
        return max_value

    @staticmethod
    def ascending_order(iterable, func):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                # if iterable[r].money > iterable[c].money:
                if func(iterable[r]) > func(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

# def xx(item):          item 代替max_value
#     return item.money
# def yy(item):          item 代替iterable[i]，两个函数是一个方法
#     return item.money
# 做的时候替换为lambda
# lambda item:item.money
