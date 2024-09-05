from shape import Shape


class Rectangle(Shape):
    """
        A class used to represent a rectangle, which is a subclass of Shape.

        :param length: The length of the rectangle.
        :type length: float
        :param width: The width of the rectangle.
        :type width: float
        :param color: The color of the rectangle (default is 'white').
        :type color: str
        :param area: The area of the rectangle (default is 0, will be calculated).
        :type area: float
        :param perimeter: The perimeter of the rectangle (default is 0, will be calculated).
        :type perimeter: float
        """
    def __init__(self, length, width, color = 'white', area = 0, perimeter = 0):
        """
                Initializes a Rectangle object with length, width, color, area, and perimeter.

                The area and perimeter are calculated based on the length and width.

                :param length: The length of the rectangle.
                :type length: float
                :param width: The width of the rectangle.
                :type width: float
                :param color: The color of the rectangle (default is 'white').
                :type color: str
                :param area: The area of the rectangle (default is 0, will be calculated).
                :type area: float
                :param perimeter: The perimeter of the rectangle (default is 0, will be calculated).
                :type perimeter: float
                """
        super().__init__(area, perimeter, color)
        self.length = length
        self.width = width

        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)

    def __add__(self, other):
        """
                Adds the area and perimeter of this rectangle to another shape.

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
    # Create two rectangle objects
    rect1 = Rectangle(length=5, width=3, color='red')
    rect2 = Rectangle(length=2, width=4, color='blue')

    # Assert area and perimeter of rect1
    assert rect1.get_area() == 15, f"Expected area of 15, but got {rect1.get_area()}"
    assert rect1.get_perimeter() == 16, f"Expected perimeter of 16, but got {rect1.get_perimeter()}"

    # Assert area and perimeter of rect2
    assert rect2.get_area() == 8, f"Expected area of 8, but got {rect2.get_area()}"
    assert rect2.get_perimeter() == 12, f"Expected perimeter of 12, but got {rect2.get_perimeter()}"

    # Test adding two rectangles
    combined_shape = rect1 + rect2

    # Assert combined area and perimeter
    assert combined_shape.get_area() == 23, f"Expected combined area of 23, but got {combined_shape.get_area()}"
    assert combined_shape.get_perimeter() == 28, f"Expected combined perimeter of 28, but got {combined_shape.get_perimeter()}"

    print("All asserts passed!")
