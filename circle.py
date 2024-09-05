from shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius, color = 'white', area = 0, perimeter = 0):
        super().__init__(area, perimeter, color)
        self.radius = radius

        self.area = math.pi * self.radius ** 2
        self.perimeter = 2 * math.pi * self.radius
