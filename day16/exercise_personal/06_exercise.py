# class MyRangeInterator:
#     def __init__(self,stop):
#         self.number = 0
#         self.stop = stop
#
#     def __next__(self): #不能直接传递到函数要先传给类
#         self.number += 1
#         if self.number < self.stop:
#             return self.number
#         else:
#             raise StopIteration()


class MyRange:
    def __init__(self, end):
        self.end = end
        self.num = 0

    def __iter__(self):
        while self.num < self.end:
            yield self.num
            self.num += 1


for item in MyRange(5):  # 0~4
    print(item)