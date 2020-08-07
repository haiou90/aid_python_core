"""
    业务逻辑层
""" 
from dal import HouseDao
class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()
        self.max = self.__list_houses[0]
        self.dict_type_house = {}
        self.set_house =set()
    @property
    def list_houses(self):
        return self.__list_houses

    def delete_house(self, id):
        for item in self.__list_houses:
            if item.id == id:
                self.__list_houses.remove(item)
            return True
        return False

    def calculate_max_price(self):
        for i in range(len(self.__list_houses)):
            if self.max.total_price < self.__list_houses[i].total_price:
                self.max = self.__list_houses[i]
        return self.max

    def calculate_min_price(self):
        return min(self.__list_houses,key=lambda item: item.total_price)

    def calculate_house_type(self):
        for item in self.__list_houses:
            if item.house_type in self.dict_type_house:
                self.dict_type_house[item.house_type] += 1
            else:
                self.dict_type_house[item.house_type] = 1
        return self.dict_type_house

    # def calculate_house_old_type(self):
    #     for item in self.__list_houses:
    #         self.set_house.add(item.house_type)
    #     for item in self.set_house:
    #         self.dict_type_house.update({item:self.__list_houses.count(item)})
    #     return self.dict_type_house

