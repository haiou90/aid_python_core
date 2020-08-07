class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

list_employee = [
    EmployeeModel(1001, 9003, "林玉玲", 13000),
    EmployeeModel(1002, 9003, "王荆轲", 16000),
    EmployeeModel(1003, 9003, "刘岳浩", 11000),
    EmployeeModel(1004, 9003, "冯舜禹", 17000),
    EmployeeModel(1005, 9003, "曹海欧", 15000),
    EmployeeModel(1006, 9003, "魏鑫珑", 12000),
]

# 1. 定义函数,在list_employee中查找薪资大于等于15000的所有员工
# 2. 定义函数,在list_employee中查找员工编号为1005的员工
# def find_max():
#     for emp in list_employee:
#         if emp.money > 15000:
#             yield emp
#
# for emp in find_max():
#     print(emp.__dict__)
#
#
# def find_eid():
#     for emp in list_employee:
#         if emp.eid == 1005:
#             return emp
#
# print(find_eid())

class EmployeeController:
    def find_eid(self,target_eid):
        for emp in list_employee:
            if emp.eid == target_eid:
                return emp

class EmployeeView:
    def __init__(self):
        self.controller = EmployeeController()

    def main(self):
        while True:
            self.input()

    def input(self):
        emp = EmployeeModel()
        emp.eid = int(input("请输入要查找的编号:"))
        print(self.controller.find_eid(emp.eid).__dict__)

view = EmployeeView()
view.main()