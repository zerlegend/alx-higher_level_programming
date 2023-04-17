#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    a = Rectangle(100, 40)
    b = Rectangle(90, 110, 30, 10)
    c = Rectangle(20, 25, 110, 80)
    list_rectangles = [a, b, c]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
