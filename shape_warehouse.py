from rectangle import Rectangle
from square import Square
from circle import Circle
import random

SHAPE_TYPES = ['rectangle', 'square', 'circle']
COLOR_LIST = ['white', 'black', 'blue', 'red', 'green', 'yellow']

class ShapeWarehouse:
    """
       A class used to store and manage a collection of randomly generated shapes.

       Shapes can be rectangles, squares, or circles, and are randomly assigned colors from a predefined list.
       """
    def __init__(self):
        """
                Initializes a ShapeWarehouse object with an empty list of shapes.

                :return: None
                :rtype: None
                """
        self.shape_list = []


    def create_new_shape(self):
        """
                Creates a new shape (rectangle, square, or circle) with random dimensions and a random color.

                :return: A new randomly generated shape.
                :rtype: Shape
                """
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
        """
                Generates and stores a given number of random shapes in the warehouse.

                :param num: The number of shapes to generate.
                :type num: int
                :return: A list of generated shapes.
                :rtype: list of Shape
                """
        for i in range(num):
            new_shape = self.create_new_shape()
            self.shape_list.append(new_shape)

        return self.shape_list


    def sum_areas(self):
        """
                Calculates the total area of all the shapes in the warehouse.

                :return: The sum of the areas of all shapes.
                :rtype: float
                """
        sum_areas = 0
        for shape in self.shape_list:
            sum_areas += shape.get_area()
        return sum_areas

    def sum_perimeters(self):
        """
                Calculates the total perimeter of all the shapes in the warehouse.

                :return: The sum of the perimeters of all shapes.
                :rtype: float
                """
        sum_perimeter = 0
        for shape in self.shape_list:
            sum_perimeter += shape.get_perimeter()
        return sum_perimeter

    def count_colors(self):
        """
                Counts the occurrence of each color across all shapes in the warehouse.

                :return: A dictionary with the count of each color.
                :rtype: dict
                """
        colors_dict = {'white':0,
        'black':0,
        'blue':0,
        'red':0,
        'green':0,
        'yellow':0}

        for shape in self.shape_list:
            colors_dict[shape.color]+=1

        return colors_dict


# Test with asserts
if __name__ == "__main__":
    # Create warehouse
    warehouse = ShapeWarehouse()

    # Generate shapes
    warehouse.generate(10)

    # Assert that shapes have been generated
    assert len(warehouse.shape_list) == 10, "Shape list should contain 10 shapes."

    # Test sum_areas
    areas_sum = warehouse.sum_areas()
    assert areas_sum > 0, "The total area should be greater than zero."

    # Test sum_perimeters
    perimeters_sum = warehouse.sum_perimeters()
    assert perimeters_sum > 0, "The total perimeter should be greater than zero."

    # Test count_colors
    colors_count = warehouse.count_colors()
    total_shapes = sum(colors_count.values())
    assert total_shapes == 10, f"The total count of shapes should be 10, got {total_shapes}."

    print("All asserts passed!")
