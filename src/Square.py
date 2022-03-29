from src.Figure import Figure


class Square(Figure):

    def __init__(self, side):
        self.side = side
        self.name = 'square'
        self.perimeter = side * 4
        self.area = self.side ** 2
