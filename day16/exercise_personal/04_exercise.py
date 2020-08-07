# class RangeInterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = -1
#
#     def __next__(self):
#         self.index += 1
#         if self.index < len(self.data):
#             return self.data[self.index]
#         else:
#             raise StopIteration
#
# class MyRange:
#     def __init__(self):
#         self.all_range = []
#         self.num = -1
#     def add_range(self, range):
#         while True:
#             self.num += 1
#             if self.num < range:
#                 self.all_range.append(self.num)
#             else:
#                 break
#     def __iter__(self):
#         return RangeInterator(self.all_range)
#
# range = MyRange()
# # range.add_range(0)
# # range.add_range(1)
# # range.add_range(2)
# # range.add_range(3)
# range.add_range(6)
# # for item in MyRange(5):
# #     print(item)
#
#
# iterator = range.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break


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

    def __iter__(self):
        return MyRangeInterator(self.end)

for item in MyRange(5):  # 0~4
    print(item)
