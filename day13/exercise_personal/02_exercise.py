"""
创建员工管理器
    1.记录多个员工 （程序员、测试员）
    2.提供计算总薪资的方法

程序员：底薪10000+项目分红*10%
测试员：底薪5000+Bug数 ×5
 三大特征
        封装：创建EmployeeManager、Programmer、Tester
        继承：创建Employee薪资计算方式(抽象/统一/隔离 具体薪资)
        多态:EmployeeManager调用Employee
            Programmer、Tester重写Employee
            向EmployeeManager添加Programmer、Tester对象
EmployeeSalary
    六大原则：
        开闭：增加新员工,员工管理器不变.
        单一职责：EmployeeManager：管理所有员工
                Programmer：计算程序员工资
                Tester：计算测试员工资
        依赖倒置：EmployeeManager使用父Employee
                不使用Programmer、Tester
        组合复用：EmployeeManager 与员工薪资算法
        里氏替换：使用时语法层面的规则。
                Programmer、Tester重写时先调用父类方法
        迪米特法则：
            Employee隔离EmployeeManager与Programmer、Tester低耦合
"""

class EmployeeManager:
    def __init__(self):
        self.all_employees = []
    def add_employee(self,employee):
        self.all_employees.append(employee)

    def calculate_total_salary(self):
        total_salary = 0
        for employee in self.all_employees:
            total_salary += employee.calculate_salary()
        return total_salary
class Employee():
    def calculate_salary(self):
        pass

class Programmer(Employee):
    def __init__(self, base=None, kpi=None):
        self.base = base
        self.kpi = kpi
    def calculate_salary(self):
        super().calculate_salary()
        return self.base + self.kpi

class Tester(Employee):
    def __init__(self, base=None, bug_num=None):
        self.base = base
        self.bug_num = bug_num
    def calculate_salary(self):
        super().calculate_salary()
        return self.base + self.bug_num * 5

manager = EmployeeManager()
manager.add_employee(Programmer(10000,15000))
manager.add_employee(Tester(5000,2000))
print(manager.calculate_total_salary())
