from src.Figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius
        self.name = 'circle'

    @property
    def get_perimeter(self):
        return 2 * self.radius * pi

    @property
    def get_area(self):
        return pi * self.radius ** 2
