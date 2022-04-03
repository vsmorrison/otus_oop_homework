from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.name = 'rectangle'

    @property
    def get_perimeter(self):
        return (self.length + self.width) * 2

    @property
    def get_area(self):
        return self.length * self.width
