#定义员工管理器 计算员工的薪资
#程序员 :底薪+项目分红
#测试: 底薪+bug数*5

class EmpManager:
    def __init__(self):
        self.__all_emp = []

    def add_emp(self,emp):
        self.__all_emp.append(emp)

    def calc_total_salary(self):
        total_salary = 0
        for emp in self.__all_emp:
            total_salary += emp.get_salary()
        return total_salary



class Employee:
    def get_salary(self):
        pass


class Programmer(Employee):
    def __init__(self,base_salary,bonus=0):
        self.base_salary = base_salary
        self.bonus = bonus

    def get_salary(self):
        return self.base_salary+self.bonus


class Tester(Employee):
    def __init__(self, base_salary, bug_count=0):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def get_salary(self):
        return self.base_salary + self.bug_count*5


manager = EmpManager()
manager.add_emp(Programmer(20000,100000))
manager.add_emp(Tester(10000,200))
manager.calc_total_salary()