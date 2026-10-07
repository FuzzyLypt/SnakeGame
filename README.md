# 🐍 SnakeGame

A simple text-based Snake game played with the **WASD** keys and rendered directly in the terminal.

```
..............................
..............................
......o.......................
..............................
.........#######..............
..............................
```

## Gameplay

- `#` is the snake, `o` is the food and `.` is an empty cell.
- The edges of the board **wrap around**: leaving one side brings you back on the opposite side.
- Eating food grows the snake by one segment and spawns new food on a free cell.
- The game ends if the snake's head runs into its own body.
- You win when the snake fills the entire board.
- Each frame shows the head position, the food position, your score (food eaten) and the current step.

### Controls

| Key | Direction |
| --- | --------- |
| `W` | Up        |
| `A` | Left      |
| `S` | Down      |
| `D` | Right     |

The snake cannot reverse directly into itself, so pressing the opposite direction of the current movement is ignored. Press `Ctrl+C` in the terminal to quit.

## Requirements

- Python 3.12.x+
- [`keyboard`](https://pypi.org/project/keyboard/) library

Developed and tested on **Windows**. The `keyboard` library reads key presses system-wide, so the game also reacts to keys while the terminal is not focused. On Linux it requires root privileges, and macOS support is experimental.

## Installation

```bash
git clone https://github.com/FuzzyLypt/SnakeGame.git
cd SnakeGame

python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux / macOS

pip install -r requirements.txt
```

## Running the game

From the project root (the folder that contains `game/`):

```bash
python -m game
```

## Configuration

The game settings are defined at the top of `main()` in `game/game_modes/snake_game.py`:

| Variable            | Default    | Description                                   |
| ------------------- | ---------- | --------------------------------------------- |
| `initial_grid_size` | `(30, 10)` | Board size as `(width, height)`               |
| `starting_length`   | `7`        | Number of segments the snake starts with      |
| `frame_time`        | `0.1`      | Seconds between frames (lower is faster)      |
| `time_limit`        | `24000`    | Maximum number of steps before the game stops |

## Project structure

```
SnakeGame/
└── game/
    ├── __init__.py
    ├── __main__.py              # entry point (python -m game)
    ├── game_modes/
    │   ├── __init__.py
    │   └── snake_game.py        # main game loop
    ├── grid_maps/
    │   ├── __init__.py
    │   └── gridwrap_map.py      # wrap-around board: movement, food spawning, rendering
    ├── objects/
    │   ├── __init__.py
    │   ├── food_obj.py          # food position
    │   └── snake_obj.py         # snake body and movement
    └── controllers/
        ├── __init__.py
        └── input_handler.py     # keyboard input
```

## How it works

- **`SnakeObj`** stores the body as a list of coordinates with the head at index 0. `move(new_head, grew)` inserts the new head and removes the tail unless the snake just ate.
- **`GridWrapMap`** handles everything about the board itself: wrapping positions with modulo, choosing a random free cell for new food, and drawing the frame. It knows nothing about snakes beyond the coordinates it is given.
- **`InputHandler`** listens for key presses through `keyboard.on_press`. The key callback runs on a separate thread, so a `threading.Lock` protects the direction state shared with the game loop, and the snake can never be turned back onto itself by a quick double key press.
- **`snake_game.py`** ties these together. The objects don't depend on each other, so new maps, controllers or game modes can be added without changing them.

## Ideas for the future

- A dedicated game window instead of printing frames in the terminal
- More game modes, such as multiplayer
- AI-controlled snakes and an AI playground
- Other map types, such as walls instead of wrap-around
