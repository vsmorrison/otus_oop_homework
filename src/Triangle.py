from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = 'triangle'

    @property
    def existance(self):
        if self.side_1 + self.side_2 > self.side_3:
            if self.side_1 + self.side_3 > self.side_2:
                if self.side_2 + self.side_3 > self.side_1:
                    return True
                else:
                    return None
            else:
                return None
        else:
            return None

    @property
    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    @property
    def get_semiperimeter(self):
        return self.get_perimeter / 2

    @property
    def get_area(self):
        return (self.get_semiperimeter *
                (self.get_semiperimeter - self.side_1) *
                (self.get_semiperimeter - self.side_2) *
                (self.get_semiperimeter - self.side_3)) ** 0.5
