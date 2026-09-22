# Imports
import random
import sys
import time
import keyboard

from food_obj import FoodObj
from snake_obj import SnakeObj

# Configuration Variables
grid_size = (30, 10)
time_limit = 15
frame_time = 0.1
snake_extra_length = 2

# Logic Variables
snake = SnakeObj(snake_extra_length, (random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1)))
food = FoodObj()
direction = (1, 0)
pending_direction = direction

# Input Threading Logic
def player_input(event):
    global pending_direction

    key_map = {
        'w': (0, -1),
        'a': (-1, 0),
        's': (0, 1),
        'd': (1, 0)
    }

    if event.name in key_map:
        new_direction = key_map[event.name]

        if new_direction[0] + direction[0] != 0 or new_direction[1] + direction[1] != 0:
            pending_direction = new_direction

# Game Start Logic
free_list = [(x, y) for y in range(grid_size[1]) for x in range(grid_size[0]) if (x, y) not in snake.coordinates]
food.pos = free_list[random.randrange(len(free_list))]
keyboard.on_press(player_input)

# Main Logic Updating Loop
for step in range(time_limit):
    # Input Logic
    direction = pending_direction

    # Dynamic Positioning and Food Logic
    new_head = (snake.head[0] + direction[0], snake.head[1] + direction[1])
    if direction[0] != 0:
        if 0 > new_head[0]:
            new_head = (grid_size[0] - 1, snake.head[1])
        elif new_head[0] >= grid_size[0]:
            new_head = (0, snake.head[1])
    else:
        if 0 > new_head[1]:
            new_head = (snake.head[0], grid_size[1] - 1)
        elif new_head[1] >= grid_size[1]:
            new_head = (snake.head[0], 0)
    if new_head == food.pos:
        snake.move(new_head, True)
        free_list = [(x, y) for y in range(grid_size[1]) for x in range(grid_size[0]) if (x, y) not in snake.coordinates]
        food.pos = free_list[random.randrange(len(free_list))]
    else:
        snake.move(new_head, False)
    if snake.head in snake.coordinates[1:]:
        print("Game ended by player action")
        sys.exit(0)

    # Rendering
    grid = [['.'] * grid_size[0] for _ in range(grid_size[1])]
    grid[food.pos[1]][food.pos[0]] = 'o'
    for i in range(len(snake.coordinates)):
        grid[snake.coordinates[i][1]][snake.coordinates[i][0]] = '#'
    row_strings = [''.join(row) for row in grid]
    frame_str = '\n'.join(row_strings)
    blank = '\n' * 2
    print(f"{blank}Snake head pos: {snake.head}\nFood pos: {food.pos}\nScore: {len(snake.coordinates)}\nStep {step + 1} out of {time_limit}:\n{frame_str}")

    # Frame Update
    time.sleep(frame_time)