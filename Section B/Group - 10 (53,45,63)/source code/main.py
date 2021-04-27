import os
import src

heading = """_____SAINIK SCHOOL KALIKIRI______
<<<<<-- ICC CRICKET DATABASE -->>>>>\n"""

menu = """\n>>>>> MAIN MENU <<<<<
Press (1) to see the format table
Press (2) to see the player stats
Press (3) to update the player stats
Press (4) to add a new player
Press (5) to delete a retired player
Press (6) to exit the program\n"""

menu_dict = {
    '1': src.see_format_table,
    '2': src.see_player_stats,
    '3': src.update_player_stats,
    '4': src.add_new_player,
    '5': src.delete_player,
    '6': src.exit_program
                    }


def main():
    os.system('cls')
    print(heading)

    while True:
        print(menu)

        user_input = input("Enter your choice from the above options : ")

        if user_input in menu_dict:
            menu_dict[user_input]()

        else:
            print("You have entered an invalid input. Please try again")
            continue


if __name__ == '__main__':
    main()
