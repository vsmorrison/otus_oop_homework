from src.Figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius
        self.name = 'circle'
        self.perimeter = 2 * radius * pi
        self.area = pi * radius ** 2
