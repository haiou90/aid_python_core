"""
员工管理系统MVC
识别对象 EmployeeView  EmployeeController
"""

class EmployeeModel:
    """
    学生数据模型
    对员工具体信息进行抽象
    """
    def __init__(self, eid=0, did=0, name="", money=0.0, sid=0):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name  # 姓名
        self.money = money  # 薪资
        self.sid = sid

