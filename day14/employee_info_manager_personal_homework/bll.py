"""
员工管理系统MVC
识别对象 EmployeeView  EmployeeController
"""


class EmployeeController:
    def __init__(self):
        self.__list_employee = []
        self.__start_sid = 1001
    @property
    def list_employee(self):
        return self.__list_employee
    def add_employee(self,employee):
        employee.sid = self.__start_sid
        self.__start_sid += 1
        self.__list_employee.append(employee)

    def delete_employee(self, sid):
        for employee in self.__list_employee:
            if employee.sid == sid:
                self.__list_employee.remove(employee)
                return True
        return False

    def adjusted_employee(self, eid, new_employee):
        for employee in self.__list_employee:
            if employee.eid == eid:
                employee.eid = new_employee.eid
                employee.did = new_employee.did
                employee.name = new_employee.name
                employee.money = new_employee.money



