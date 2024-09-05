from shape import Shape
import math


class Circle(Shape):
    """
        A class used to represent a circle, which is a subclass of Shape.

        :param radius: The radius of the circle.
        :type radius: float
        :param color: The color of the circle (default is 'white').
        :type color: str
        :param area: The area of the circle (default is 0, will be calculated).
        :type area: float
        :param perimeter: The perimeter (circumference) of the circle (default is 0, will be calculated).
        :type perimeter: float
        """
    def __init__(self, radius, color = 'white', area = 0, perimeter = 0):
        """
               Initializes a Circle object with radius, color, area, and perimeter.

               The area and perimeter are calculated based on the radius.

               :param radius: The radius of the circle.
               :type radius: float
               :param color: The color of the circle (default is 'white').
               :type color: str
               :param area: The area of the circle (default is 0, will be calculated).
               :type area: float
               :param perimeter: The perimeter (circumference) of the circle (default is 0, will be calculated).
               :type perimeter: float
               """
        super().__init__(area, perimeter, color)
        self.radius = radius

        self.area = math.pi * self.radius ** 2
        self.perimeter = 2 * math.pi * self.radius


# Test with asserts
if __name__ == "__main__":
    # Create a circle object
    circle = Circle(radius=3, color='red')

    # Calculate expected area and perimeter
    expected_area = math.pi * 3 ** 2  # 28.274333882308138
    expected_perimeter = 2 * math.pi * 3  # 18.84955592153876

    # Assert area and perimeter calculations
    assert math.isclose(circle.get_area(), expected_area, rel_tol=1e-9), f"Expected area of {expected_area}, but got {circle.get_area()}"
    assert math.isclose(circle.get_perimeter(), expected_perimeter, rel_tol=1e-9), f"Expected perimeter of {expected_perimeter}, but got {circle.get_perimeter()}"

    print("All asserts passed!")