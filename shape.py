import math


class Shape:
    def __init__(self, color = 'white', area = 0, perimeter = 0):
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

    def __str__(self):
        return f'color:{self.color}, area: {self.area}, perimeter: {self.perimeter}'







