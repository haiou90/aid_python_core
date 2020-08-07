"""
    函数返回结果:
        return 数据  -- 单个
        yield 数据   -- 多个
"""
class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0.0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

list_employee = [
    EmployeeModel(1001, 9003, "林玉玲", 13000),
    EmployeeModel(1002, 9005, "王荆轲", 16000),
    EmployeeModel(1003, 9007, "刘岳浩", 11000),
    EmployeeModel(1004, 9005, "冯舜禹", 17000),
    EmployeeModel(1005, 9003, "曹海欧", 15000),
    EmployeeModel(1006, 9005, "魏鑫珑", 12000),
]

# 1. 定义函数,在list_employee中查找薪资大于等于15000的所有员工
# def find01():
#     for emp in list_employee:
#         if emp.money > 15000:
#             yield emp
# for item in find01():
#     print(item.__dict__)
#
# # 2. 定义函数,在list_employee中查找员工编号为1005的员工
# def find02():
#     for emp in list_employee:
#         if emp.did == 9005:
#             return emp
# employee = find02()
# print(employee.__dict__)
#
def condition01(item):
     return item.money >= 15000


def condition02(item):
    return item.did == 9005

def find01(a):
    for emp in list_employee:
        # if emp.money > 15000:
        if a(emp):
            yield emp
for item in find01(condition01):
    print(item.__dict__)

import common.iteralbe_tool

def condition02(item):
    return item.did == 9005
for item in IterableHelper.find(list_employee,condition02)