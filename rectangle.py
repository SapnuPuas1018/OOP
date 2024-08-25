from shape import Shape


class Rectangle(Shape):
    def __init__(self, length, width, color = 'white', area = 0, perimeter = 0):
        super().__init__(color, area, perimeter)
        self.length = length
        self.width = width

        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)

    def __add__(self, other):
        area = self.get_area() + other.get_area()
        perimeter = self.get_perimeter() + other.get_perimeter()
        new_shape = Shape(area=area, perimeter=perimeter)
        return new_shape
