class EmployeeInterator:
    def __init__(self,data):
        self.data = data
        self.index = -1
    def __next__(self):
        self.index += 1
        if self.index < len(self.data):
            return self.data[self.index]
        else:
            raise StopIteration

class EmployeeManager:
    def __init__(self):
        self.all_employee = []

    def add_employee(self, emp):
        self.all_employee.append(emp)

    def __iter__(self):
        return EmployeeInterator(self.all_employee)

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
