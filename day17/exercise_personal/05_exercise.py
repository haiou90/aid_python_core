from iteralbe_tool import IterableHelper

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
def condition02(item):
    return item.did == 9005
for item in IterableHelper.find(list_employee,condition02):
    print(item.__dict__)

