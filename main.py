"""
author - Yuval Hayun
date   - 25/08/24
OOP shapes
"""

from rectangle import Rectangle
from square import Square
from shape_warehouse import ShapeWarehouse



def main():
    square = Square(5)
    rectangle = Rectangle(6, 2)
    print(square + square)
    print(square + rectangle)
    print(rectangle + square)

    my_container = ShapeWarehouse()
    my_container.generate(100)

    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())

if __name__ == '__main__':
    main()
