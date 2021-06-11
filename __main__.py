from os import system
import command_parser

def main():
    game_is_active = True;
    while(game_is_active):
        #system('cls')
        print("type a command")
        response = input("> ")
        if(response == "stop"):
            game_is_active = False
        else:
            x = command_parser.simple_parse(response)
            print(x)
main()
