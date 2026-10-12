import threading
import keyboard

from game.utilities.game_utilities import GameUtils


class InputHandler:
    def __init__(self):
        self._lock = threading.Lock()
        self.input_direction = (1, 0)
        self.pending_direction = (1, 0)
        self.game_input_key_map = {
            'w': (0, -1),
            'a': (-1, 0),
            's': (0, 1),
            'd': (1, 0)
        }
        self.interactions_input_key_map = {
            'k'
        }

    def commit_direction(self):
        with self._lock:
            self.input_direction = self.pending_direction
            return self.input_direction

    def player_input(self, event):
        with self._lock:
            if event.name in self.interactions_input_key_map:
                if event.name == 'k':
                    GameUtils.exit_game()
            elif event.name in self.game_input_key_map:
                new_direction = self.game_input_key_map[event.name]
                if new_direction[0] + self.input_direction[0] != 0 or new_direction[1] + self.input_direction[1] != 0:
                    self.pending_direction = new_direction

    def keyboard_listen(self):
        keyboard.on_press(self.player_input)