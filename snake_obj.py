class SnakeObj:
    def __init__(self, extra_length, head_coordinate):
        self.coordinates = [head_coordinate]
        for _ in range(extra_length):
            new_head = (head_coordinate[0] + 1, head_coordinate[1])
            self.move(new_head, True)

    @property
    def head(self):
        return self.coordinates[0]

    @head.setter
    def head(self, value):
        self.coordinates[0] = value

    def move(self, new_head, grew):
        self.coordinates.insert(0, new_head)
        if not grew:
            self.coordinates.pop()

    def collided_with_self(self):
        return self.head in self.coordinates[1:]
