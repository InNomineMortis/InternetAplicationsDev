from lab_python_oop.color import Color
from lab_python_oop.figure import Figure


class Rectangle(Figure):
    FIGURE = "Rectangle"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color()
        self.color.value = color

    def calc_area(self):
        return self.width * self.height

    def __repr__(self):
        return "{0}: Width = {1} Height = {2} Color = {3} Area = {4}".format(self.name, self.width, self.height,
                                                                             self.color.value, self.calc_area())
