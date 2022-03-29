class Figure:

    def __init__(self, name, area, perimeter):
        self.name = name
        self.area = area
        self.perimeter = perimeter

    def add_area(self, shape):
        if not isinstance(shape, Figure):
            raise ValueError
        return self.area + shape.area
