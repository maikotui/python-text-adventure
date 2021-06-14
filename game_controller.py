import views

class Controller:
    def __init__(self, view) -> None:
        if(isinstance(view, views.View)):
            self._display = view
        else:
            raise TypeError

    def start_game(self):
        pass