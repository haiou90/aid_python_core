"""
    exercise06_type_conversion.py
    练习:使用lambda代替condtion0x函数
"""
from day18.common.iterable_tools import IterableHelper


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


list_employee = [
    EmployeeModel(1001, 9003, "林玉玲", 13000),
    EmployeeModel(1002, 9005, "王荆轲", 16000),
    EmployeeModel(1003, 9003, "刘岳浩", 11000),
    EmployeeModel(1004, 9007, "冯舜禹", 17000),
    EmployeeModel(1005, 9005, "曹海欧", 15000),
    EmployeeModel(1006, 9005, "魏鑫珑", 12000)
]



def find(func):
    for emp in list_employee:
        if func(emp):
            yield emp

def delete():
    count = 0
    for i in range(len(list_employee)-1,-1,-1):
        if list_employee[i].money == 15000:
            del list_employee[i]
            count += 1
    return count
# delete()
# for item in list_employee:
#     print(item.__dict__)

# IterableHelper.delete_all(list_employee,lambda emp:emp.did == 9005)
# for item in list_employee:
#     print(item.__dict__)
# for item in IterableHelper.delete(list_employee,lambda emp:emp.did == 9005):
#     print(item.__dict__)

# def find_max():
#     max_value = list_employee[0]
#     for r in range(len(list_employee)-1):
#         for c in range(r+1,len(list_employee)):
#             if max_value.money < list_employee[c].money:
#                max_value = list_employee[c]
#     return max_value
# result = IterableHelper.find_max(list_employee,lambda emp:emp.money)
# print(result.__dict__)
# result = IterableHelper.find_max(list_employee,lambda emp:emp.did)
# print(result.__dict__)

def ascending_employee():
    max_value = list_employee[0]
    for r in range(len(list_employee)-1):
        for c in range(r+1,len(list_employee)):
            if max_value.money < list_employee[c].money:
               max_value = list_employee[c]


def ascending_employee():
    max_value = list_employee[0]
    for r in range(len(list_employee)-1):
        for c in range(r+1,len(list_employee)):
            if max_value.eid < list_employee[c].eid:
               max_value = list_employee[c]


def ascending_employee(iterable,func):
    for r in range(len(iterable)-1):
        for c in range(r+1, len(iterable)):
            # if max_value.eid < iterable[c].eid:
            if func(iterable[r]) < func(iterable[c]):
               iterable[r],iterable[c]=iterable[c],iterable[r]
result = IterableHelper.ascending_employee(list_employee,lambda emp:emp.money)
for item in list_employee:
    print(item.__dict__)