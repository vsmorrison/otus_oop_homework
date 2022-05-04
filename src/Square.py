from src.Figure import Figure


class Square(Figure):

    def __init__(self, side):
        self.side = side
        self.name = 'square'

    @property
    def get_perimeter(self):
        return self.side * 4

    @property
    def get_area(self):
        return self.side ** 2
