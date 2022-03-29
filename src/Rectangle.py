from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.name = 'rectangle'
        self.area = length * width
        self.perimeter = (length + width) * 2
