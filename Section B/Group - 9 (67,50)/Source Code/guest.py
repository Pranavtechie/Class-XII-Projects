import src
from os import system


def guest_menu():
    print("\n----- GUEST MENU -----\n")
    print("Press (1) to see the cars table")
    print("Press (2) to see the bikes table")
    print("Press (3) to return to main menu")
    print("Press (4) to exit the program")


def guest_main(name):
    system('cls')
    print(f"Welcome {name}\n")
    while True:

        guest_menu()

        guest_input = input("\nPlease Enter your choice from the options : ")

        guest_dict = {
            '1': src.print_cars_table,
            '2': src.print_bikes_table
        }

        if guest_input in guest_dict:
            guest_dict[guest_input]()

        elif guest_input == '3':
            print(f"\nYou chose to go the main menu")
            return None

        elif guest_input == '4':
            src.exit_program()

        else:
            print(f"\n<{guest_input}> is an invalid input. Please Try Again")
            continue
