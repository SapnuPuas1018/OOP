class Shape:
    """
    A class used to represent a geometric shape.

    :param color: The color of the shape (default is 'white').
    :type color: str
    :param area: The area of the shape (default is 0).
    :type area: float
    :param perimeter: The perimeter of the shape (default is 0).
    :type perimeter: float
    """
    def __init__(self, area, perimeter, color = 'white'):
        """
        Initializes a Shape object with area, perimeter and color.

        :param area: The area of the shape
        :type area: float
        :param perimeter: The perimeter of the shape
        :type perimeter: float
        :param color: The color of the shape (default is 'white').
        :type color: str
        """
        self.color = color
        self.area = area
        self.perimeter = perimeter

    def get_color(self):
        """
       Gets the color of the shape.

       :return: The color of the shape.
       :rtype: str
        """
        return self.color

    def set_color(self, new_color):
        """
       Sets a new color for the shape.

       :param new_color: The new color to set for the shape.
       :type new_color: str
       :return: None
       :rtype: None
        """
        self.color = new_color
        self.color = new_color


    def get_area(self):
        """
        Gets the area of the shape.

        :return: The area of the shape.
        :rtype: float
        """
        return self.area

    def get_perimeter(self):
        """
        Gets the perimeter of the shape.

        :return: The perimeter of the shape.
        :rtype: float
        """
        return self.perimeter


    def __str__(self):
        """
        Returns a string representation of the shape, including its color, area, and perimeter.

        :return: A string representing the shape.
        :rtype: str
        """
        return f'color:{self.color}, area: {self.area}, perimeter: {self.perimeter}'


if __name__ == "__main__":
    # Create a Shape object with initial values
    shape = Shape(area=20.5, perimeter=15.0, color='blue')

    # Assert the area and perimeter
    assert shape.get_area() == 20.5, f"Expected area 20.5, got {shape.get_area()}"
    assert shape.get_perimeter() == 15.0, f"Expected perimeter 15.0, got {shape.get_perimeter()}"

    # Assert the color
    assert shape.get_color() == 'blue', f"Expected color 'blue', got {shape.get_color()}"

    # Change the color and assert the new color
    shape.set_color('red')
    assert shape.get_color() == 'red', f"Expected color 'red', got {shape.get_color()}"

    print("All asserts passed!")