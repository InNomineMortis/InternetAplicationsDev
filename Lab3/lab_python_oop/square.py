from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE = "Square"

    def __init__(self, size, color):
        super().__init__(size, size, color)

    def __repr__(self):
        return "{0}: Size = {1} Color = {2} Area = {3}".format(self.name, self.width, self.color.value,
                                                               self.calc_area())
