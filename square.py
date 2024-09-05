from shape import Shape


class Square(Shape):
    """
        A class used to represent a square, which is a subclass of Shape.

        :param side: The length of the side of the square.
        :type side: float
        :param color: The color of the square (default is 'white').
        :type color: str
        :param area: The area of the square (default is 0, will be calculated).
        :type area: float
        :param perimeter: The perimeter of the square (default is 0, will be calculated).
        :type perimeter: float
        """
    def __init__(self, side, color = 'white', area = 0, perimeter = 0 ):
        """
                Initializes a Square object with side length, color, area, and perimeter.

                The area and perimeter are calculated based on the side length.

                :param side: The length of the side of the square.
                :type side: float
                :param color: The color of the square (default is 'white').
                :type color: str
                :param area: The area of the square (default is 0, will be calculated).
                :type area: float
                :param perimeter: The perimeter of the square (default is 0, will be calculated).
                :type perimeter: float
                """
        super().__init__(area, perimeter, color)
        self.side = side

        self.area = self.side ** 2
        self.perimeter = 4 * self.side

    def __add__(self, other):
        """
                Adds the area and perimeter of this square to another shape.

                :param other: The other shape to add (must implement get_area and get_perimeter).
                :type other: Shape
                :return: A new Shape with combined area and perimeter.
                :rtype: Shape
                """
        area = self.get_area() + other.get_area()
        perimeter = self.get_perimeter() + other.get_perimeter()
        new_shape = Shape(area=area, perimeter=perimeter)
        return new_shape


# Test with asserts
if __name__ == "__main__":
    # Create two square objects
    square1 = Square(side=4, color='blue')
    square2 = Square(side=3, color='green')

    # Assert area and perimeter of square1
    assert square1.get_area() == 16, f"Expected area of 16, but got {square1.get_area()}"
    assert square1.get_perimeter() == 16, f"Expected perimeter of 16, but got {square1.get_perimeter()}"

    # Assert area and perimeter of square2
    assert square2.get_area() == 9, f"Expected area of 9, but got {square2.get_area()}"
    assert square2.get_perimeter() == 12, f"Expected perimeter of 12, but got {square2.get_perimeter()}"

    # Test adding two squares
    combined_shape = square1 + square2

    # Assert combined area and perimeter
    assert combined_shape.get_area() == 25, f"Expected combined area of 25, but got {combined_shape.get_area()}"
    assert combined_shape.get_perimeter() == 28, f"Expected combined perimeter of 28, but got {combined_shape.get_perimeter()}"

    print("All asserts passed!")
