class FoodObj:
    def __init__(self):
        self.coordinates = None

    @property
    def pos(self):
        return self.coordinates

    @pos.setter
    def pos(self, new_coordinates):
        self.coordinates = new_coordinates