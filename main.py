from time import gmtime

from shape import Shape
from shape import Rectangle
from shape import Square
from shape import Circle
from shape_warehouse import ShapeWarehouse


def add_square_and_rectangle(square, rectangle):
    area = square.get_area() + rectangle.get_area()
    perimeter = square.get_perimeter() + rectangle.get_perimeter()
    new_shape = Shape(area= area, perimeter= perimeter)
    return new_shape

def add_two_shapes(shape1,shape2):
    area = shape1.get_area() + shape2.get_area()
    perimeter = shape1.get_perimeter() + shape2.get_perimeter()
    new_shape = Shape(area=area, perimeter=perimeter)
    return new_shape

def main():
    square = Square(5)
    rectangle = Rectangle(6, 2)
    add_square_and_rectangle(square, rectangle)

    my_container = ShapeWarehouse()
    my_container.generate(100)
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())

if __name__ == '__main__':
    main()
