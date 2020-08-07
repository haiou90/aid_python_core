"""
功能1:
运行程序后,按1键显示所有房源信息.
提示:创建View调用Controller中的属性,返回__list_houses
"""
from bll import HouseManagerController
from model import HouseModel


class HouseView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):   #显示菜单
        print("1 显示所有房源信息")
        print("2 删除所有房源信息")
        print("3 显示最高房价房源")
        print("4 显示最低房价房源")
        print("5 显示户型种类")
    def __select_menu(self):
        selection =input("请输入选项:")
        if selection == "1":
            self.__show_house()                   #alt+ENTER创建
        elif selection == "2":
            self.__delte_house()
        elif selection == "3":
            self.__show_max_price()
        elif selection == "4":
            self.__show_min_price()
        elif selection == "5":
            self.__show_house_type()
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __show_house(self):
        house = HouseModel()
        for house in self.__controller.list_houses:
            # print(f"{house.title}的房源编号是{house.id}社区是{house.community}"
            #       f"楼龄是{house.years}房屋类型是{house.house_type}房屋面积是{house.area}"
            #       f"楼层是{house.floor}描述是{house.description}总价是{house.total_price}"
            #       f"单价是{house.unit_price}关注{house.follow_info}")
            print(house.__dict__)

    def __delte_house(self):
        id = int(input("请输入要删除的房源编号"))
        if self.__controller.delete_house(id):
            print("删除成功")
        else:
            print("删除失败")
    def __show_max_price(self):
        print(self.__controller.calculate_max_price().__dict__)

    def __show_min_price(self):
        print(self.__controller.calculate_min_price().__dict__)

    def __show_house_type(self):
        for k,v in self.__controller.calculate_house_type().items():
            print(k,v)


view = HouseView()
view.main()

