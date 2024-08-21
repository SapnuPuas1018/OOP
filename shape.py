import math


class Shape:
    def __init__(self, color = (0,0,0), area = 0, perimeter = 0):
        self.color = color
        self.area = area
        self.perimeter = perimeter

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color


    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class Rectangle(Shape):
    def __init__(self, color, area, perimeter, length, width):
        super().__init__(color, area, perimeter)
        self.length = length
        self.width = width

        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter


class Square(Shape):
    def __init__(self, color, area, perimeter, side):
        super().__init__(color, area, perimeter)
        self.side = side

        self.area = self.side ** 2
        self.perimeter = 4 * self.side

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter

class Circle(Shape):
    def __init__(self, color, area, perimeter, radius):
        super().__init__(color, area, perimeter)
        self.radius = radius

        self.area = math.pi * self.radius ** 2
        self.perimeter = 2 * math.pi * self.radius

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter
