from shape import Shape


class Square(Shape):
    def __init__(self, side, color = 'white', area = 0, perimeter = 0 ):
        super().__init__(area, perimeter, color)
        self.side = side

        self.area = self.side ** 2
        self.perimeter = 4 * self.side

    def __add__(self, other):
        area = self.get_area() + other.get_area()
        perimeter = self.get_perimeter() + other.get_perimeter()
        new_shape = Shape(area=area, perimeter=perimeter)
        return new_shape
