import threading

class GameUtils:
    exit_requested = threading.Event()

    @staticmethod
    def exit_game():
        GameUtils.exit_requested.set()
