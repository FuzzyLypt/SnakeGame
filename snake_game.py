# Imports
import random
import sys
import time

from gridwrap_map import GridWrapMap
from input_handler import InputHandler
from food_obj import FoodObj
from snake_obj import SnakeObj

# Configuration Variables
initial_grid_size = (30, 10)
time_limit = 24000
frame_time = 0.1
starting_length = 7

# Logic Variables
grid = GridWrapMap(initial_grid_size)
snake = SnakeObj(starting_length, (random.randint(starting_length - 1, grid.grid_size[0] - 1), random.randint(0, grid.grid_size[1] - 1)))
food = FoodObj()
input_system = InputHandler()

# Game Start Logic
food.pos = grid.food_spawn(snake.coordinates)
input_system.keyboard_listen()

# Main Logic Updating Loop
for step in range(time_limit):
    # Input Logic
    direction = input_system.commit_direction()

    # Dynamic Positioning and Food Logic
    new_head = grid.move_wrap(snake.head, direction)
    if new_head == food.pos:
        snake.move(new_head, True)
        food.pos = grid.food_spawn(snake.coordinates)
        if food.pos is None:
            print("You've won the snake game!")
            sys.exit(0)
    else:
        snake.move(new_head, False)
    if snake.collided_with_self():
        print("Game ended by player action")
        sys.exit(0)

    # Rendering
    frame_str = grid.render_grid(snake.coordinates, food.pos)
    blank = '\n' * 2
    print(f"{blank}Snake head pos: {snake.head}\nFood pos: {food.pos}\nScore: {len(snake.coordinates) - starting_length}\nStep {step + 1} out of {time_limit}:\n{frame_str}")

    # Frame Update
    time.sleep(frame_time)