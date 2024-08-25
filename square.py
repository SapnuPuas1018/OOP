from shape import Shape


class Square(Shape):
    def __init__(self, side, color = 'white', area = 0, perimeter = 0 ):
        super().__init__(color, area, perimeter)
        self.side = side

        self.area = self.side ** 2
        self.perimeter = 4 * self.side