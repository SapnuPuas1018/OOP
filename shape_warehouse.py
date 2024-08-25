from shape import Shape
from shape import Rectangle
from shape import Square
from shape import Circle
import random

SHAPE_TYPES = ['rectangle', 'square', 'circle']
COLOR_LIST = ['white', 'black', 'blue', 'red', 'green', 'yellow']

class ShapeWarehouse:
    def __init__(self):
        self.shape_list = []


    def create_new_shape(self):
        shape_type = random.choice(SHAPE_TYPES)
        color = random.choice(COLOR_LIST)


        if shape_type == 'rectangle':
            length = random.randint(1,10)
            width = random.randint(1,10)
            new_shape = Rectangle(length, width, color)
        elif shape_type == 'square':
            side = random.randint(1, 10)
            new_shape = Square(side, color)
        else:
            radius = random.randint(1,10)
            new_shape = Circle(radius, color)

        return new_shape


    def generate(self, num):
        for i in range(num):
            new_shape = self.create_new_shape()
            self.shape_list.append(new_shape)

        return self.shape_list


    def sum_areas(self):
        sum_areas = 0
        for shape in self.shape_list:
            sum_areas += shape.get_area()
        return sum_areas

    def sum_perimeters(self):
        sum_perimeter = 0
        for shape in self.shape_list:
            sum_perimeter += shape.get_perimeter()
        return sum_perimeter

    def count_colors(self):
        colors_dict = {'white':0,
        'black':0,
        'blue':0,
        'red':0,
        'green':0,
        'yellow':0}

        for shape in self.shape_list:
            colors_dict[shape.color]+=1

        return colors_dict
