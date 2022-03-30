class Figure:

    def __init__(self, area):
        self.area = area

    def add_area(self, shape):
        if not isinstance(shape, Figure):
            raise ValueError
        return self.area + shape.area
