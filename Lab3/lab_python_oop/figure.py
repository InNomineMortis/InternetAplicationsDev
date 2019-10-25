from abc import ABC, abstractmethod


class Figure(ABC):
    FIGURE = "figure class"

    def __init__(self):
        self._name = None

    @abstractmethod
    def calc_area(self):
        pass

    @property
    def name(self):
        return self.FIGURE

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name
