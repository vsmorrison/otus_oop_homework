from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = 'triangle'
        self.perimeter = side_1 + side_2 + side_3
        self.semiperimeter = self.perimeter / 2
        self.area = (self.semiperimeter * (self.semiperimeter - side_1) *
                     (self.semiperimeter - side_2) *
                     (self.semiperimeter - side_3)) ** 0.5

    def check_triangle_to_exist(self):
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
