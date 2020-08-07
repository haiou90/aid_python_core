"""
4. 使用封装数据的思想
    创建员工类/部门类,修改实现下列功能.
        (1). 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
        (2). 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
        (3). 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
        (4). 定义函数,查找薪资最少的员工
        (5). 定义函数,根据薪资对员工列表升序排列

    # 员工列表
    list_employees = [
        {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
        {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
        {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
        {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
        {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
    ]

    # 部门列表
    list_departments = [
        {"did": 9001, "title": "教学部"},
        {"did": 9002, "title": "销售部"},
    ]
"""
class Employee:
    def __init__(self, eid=None, did=None, name=None, money=None, ):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

list_employees = [
        Employee(1001, 9002, "师父", 60000),
        Employee(1002, 9001, "孙悟空", 50000),
        Employee(1003, 9002, "猪八戒", 20000),
        Employee(1004, 9001, "沙僧", 30000),
        Employee(1005, 9001, "小白龙", 15000),
    ]

class Departemnt:
    def __init__(self, did=None, title=None):
        self.did = did
        self.title = title

list_departments = [
        Departemnt(9001,"教学部") ,
        Departemnt(9002,"销售部")
    ]

def single_print(emp):
    print(f'{emp.name}的员工编号是{emp.eid},部门编号是{emp.did},月薪{emp.money}元')


#定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_emp_infos():
    for emp in list_employees:
       single_print(emp)

print_emp_infos()

#定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_emp_lt_2w():
    for emp in list_employees:
       if emp.money > 20000:
           single_print(emp)

print_emp_lt_2w()

#定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
def print_emp_dep_infos():
    for emp in list_employees:
        for dep in list_departments:
            if emp.did == dep.did:
                print(f'{emp.name}的部门是{dep.title},月薪{emp.money}元')

print_emp_dep_infos()

#定义函数,查找薪资最少的员工
def get_min_money_emp():
    min_emp = list_employees[0]
    for emp in list_employees:
        if min_emp.money > emp.money:
            min_emp = emp
    return min_emp

result = get_min_money_emp()
print(f'薪资最少的员工是:{result.name}')

#定义函数,根据薪资对员工列表升序排列
def asceding_emp_list():
    for r in range(len(list_employees)-1):
        for c in range(r+1,len(list_employees)):
            if list_employees[r].money > list_employees[c].money:
                list_employees[r].money,list_employees[c].money =list_employees[c].money,list_employees[r].money
    return list_employees
asceding_emp_list()
for item in list_employees:
    print(item.__dict__)