import game_display

class game_controller:
    def __init__(self, d) -> None:
        if(isinstance(d, game_display.game_display)):
            self._display = d
        else:
            raise TypeError

    def start_game(self):
        pass

if(__name__ == "__main__"):
    x = game_display.game_display()
    y = game_controller(x)
    print("success")