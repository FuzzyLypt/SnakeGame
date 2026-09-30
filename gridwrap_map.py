import random

class GridWrapMap:
    def __init__(self, initial_grid_size):
        self.grid_size = initial_grid_size

    def food_spawn(self, snake_coordinates):
        free_list = [(x, y) for y in range(self.grid_size[1]) for x in range(self.grid_size[0]) if (x, y) not in snake_coordinates]
        if not free_list:
            return None
        return free_list[random.randrange(len(free_list))]

    def move_wrap(self, head_pos, move_direction):
        return (head_pos[0] + move_direction[0]) % self.grid_size[0], (head_pos[1] + move_direction[1]) % self.grid_size[1]

    def render_grid(self, snake_coordinates, food_pos):
        grid = [['.'] * self.grid_size[0] for _ in range(self.grid_size[1])]
        grid[food_pos[1]][food_pos[0]] = 'o'
        for i in range(len(snake_coordinates)):
            grid[snake_coordinates[i][1]][snake_coordinates[i][0]] = '#'
        row_strings = [''.join(row) for row in grid]
        return '\n'.join(row_strings)