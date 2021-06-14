import game_controller
import views
import command_parser

def main():
    """Main runner for game"""
    view = views.ConsoleView()
    controller = game_controller.Controller(view)
    controller.start_game()

    game_is_active = True
    while(game_is_active):
        print("type a command")
        response = input("> ")
        if(response == "stop"):
            game_is_active = False
        else:
            x = command_parser.simple_parse(response)
            print(x)

main()
