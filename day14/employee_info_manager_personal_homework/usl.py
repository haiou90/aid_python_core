"""
员工管理系统MVC
识别对象 EmployeeView  EmployeeController
"""
from bll import EmployeeController
from model import EmployeeModel


class EmployeeView:
    """
    #主要功能,display select input show delete adjust 提供入口功能
    员工视图：负责界面逻辑
    """
    def __init__(self):
        self.__controller = EmployeeController()
    def __display_menu(self):   #显示菜单
        print("1 添加员工信息")
        print("2 显示员工信息")
        print("3 删除员工信息")
        print("4 修改员工信息")
    def __select_menu(self):
        selection =input("请输入选项:")
        if selection == "1":
            self.__input_employee()  #因为实例方法必须用self对象调用
        elif selection == "2":
            self.__show_employee()                   #alt+ENTER创建
        elif selection == "3":
            self.__delte_employee()
        elif selection == "4":
            self.__adjust_employee()
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
    def __input_employee(self):
        """获取信息后向业务方传递，以一个封装对象传递，封装数据；数据模型装终端输入的多个数据信息"""
        employee = EmployeeModel() #输入的数据封装成数据模型,包装后传递给业务
        employee.eid = self.judge("请输入员工编号：")
        employee.did = int(input("请输入部门编号："))
        employee.name = input("请输入员工姓名：")
        employee.money = int(input("请输入员工薪资："))
        self.__controller.add_employee(employee)

    def __show_employee(self):
        for employee in self.__controller.list_employee:
            print(f"{employee.name}的员工编号是{employee.eid}部门编号是{employee.did}")

    def __delte_employee(self):
        sid = int(input("请输入要删除的标识码"))
        if self.__controller.delete_employee(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __adjust_employee(self):
        new_employee = EmployeeModel()
        eid = int(input("请输入员工原编号："))
        new_employee.eid = int(input("请输入员工编号："))
        new_employee.did = int(input("请输入部门编号："))
        new_employee.name = input("请输入员工姓名：")
        new_employee.money = int(input("请输入员工薪资："))
        self.__controller.adjusted_employee(eid,new_employee)

    def judge(self,judgement):
        while True:
            try:
                number = int(input(judgement))
                return number
            except:
                print("输入错误请重输")

