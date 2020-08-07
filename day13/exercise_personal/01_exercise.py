class GraphicManger:
    def __init__(self):
        self.all_graphic = []
    def add_graphic(self,graphic):
        self.all_graphic.append(graphic)

    def calculate_total_area(self):
        total_area = 0
        for graphic in self.all_graphic:
            total_area += graphic.calculate_area()
        return total_area


class GraphicLibrary:
    def calculate_area(self):
        pass

class Circle(GraphicLibrary):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        circle_area = 3.14 * self.radius **2
        return circle_area

class Rectangle(GraphicLibrary):
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        rectangle_area = self.length * self.width
        return rectangle_area


manager = GraphicManger()
manager.add_graphic(Circle(5))
manager.add_graphic(Rectangle(6,8))
manager.add_graphic(Circle(8))
print(manager.calculate_total_area())




