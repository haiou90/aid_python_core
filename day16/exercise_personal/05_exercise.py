# class MyRange:
#     def __init__(self):
#         self.all_employee = []
#
#     def add_employee(self, emp):
#         self.all_employee.append(emp)
#     def __iter__(self):
#         print("1")
#         yield self.all_employee[0]
#         print("2")
#         yield self.all_employee[1]
#         print("3")
#         yield self.all_employee[2]
#
# manager = MyRange()
# manager.add_employee("老王")
# manager.add_employee("老李")
# manager.add_employee("老孙")
# iterator = manager.__iter__()
#
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break



class EmployeeManager:
    def __init__(self):
        self.all_employee = []

    def add_employee(self, emp):
        self.all_employee.append(emp)

    def __iter__(self):
        print("1")
        yield self.all_employee[0]
        print("2")
        yield self.all_employee[1]
        print("3")
        yield self.all_employee[2]
manager = EmployeeManager()
manager.add_employee("老王")
manager.add_employee("老李")
manager.add_employee("老孙")
# for item in manager:
# print(item)
iterator = manager.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break