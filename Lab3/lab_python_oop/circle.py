import math

from lab_python_oop.color import Color
from lab_python_oop.figure import Figure


class Circle(Figure):
    FIGURE = "Circle"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color()
        self.color.value = color

    def calc_area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{0}: Radius = {1} Color = {2} Area = {3}".format(self.name, self.radius, self.color.value,
                                                                 self.calc_area())
