class Figure:

    def add_area(self, shape):
        if not isinstance(shape, Figure):
            raise ValueError
        return self.get_area + shape.get_area
