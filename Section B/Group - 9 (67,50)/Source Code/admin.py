import src
from os import system


def admin_menu():
    print("\n----- ADMIN MENU -----\n")
    print("Press (1) to see the cars table")
    print("Press (2) to see the bikes table")
    print("Press (3) to manage cars data")
    print("Press (4) to manage bikes data")
    print("Press (5) to return to main menu")
    print("Press (6) to exit the program")


def manage_cars_menu():
    while True:

        print("\n----- MANAGE CARS MENU -----\n")
        print("Press (1) to update a CAR in the table")
        print("Press (2) to delete a CAR from the table")
        print("Press (3) to add a new CAR to the table")
        print("Press (4) to go to admin menu")
        print("Press (5) to exit the program")

        update_cars_dict = {
            '1': src.update_cars_main,
            '2': src.delete_car_main,
            '3': src.add_car_main,
            '5': src.exit_program}

        update_cars_input = input(
            "\nEnter your choice from the above options : ")

        if update_cars_input in update_cars_dict:
            update_cars_dict[update_cars_input]()

        elif update_cars_input == '4':
            print("You chose to go the the manage menu")
            break

        else:
            print(f"<{update_cars_input}> is not a valid input. Please try again")
            continue


def manage_bikes_menu():
    while True:

        print("\n----- MANAGE  BIKES MENU -----\n")
        print("Press (1) to update a BIKE in the table")
        print("Press (2) to delete a BIKE from the table")
        print("Press (3) to add a new BIKE to the table")
        print("Press (4) to go to manage menu")
        print("Press (5) to exit the program")

        update_cars_dict = {
            '1': src.update_cars_main,
            '2': src.delete_car_main,
            '3': src.add_car_main,
            '5': src.exit_program}

        update_cars_input = input(
            "\nEnter your choice from the above options : ")

        if update_cars_input in update_cars_dict:
            update_cars_dict[update_cars_input]()

        elif update_cars_input == '4':
            print("You chose to go the the manage menu")
            break

        else:
            print(f"<{update_cars_input}> is not a valid input. Please try again")
            continue


def admin_main(name):
    system('cls')
    print(f"Welcome {name}\n")
    admin_dict = {
        '1': src.print_cars_table,
        '2': src.print_bikes_table,
        '3': manage_cars_menu,
        '4': manage_bikes_menu,
    }
    while True:

        admin_menu()
        admin_input = input("\nPlease Enter your choice from the options : ")

        if admin_input in admin_dict:
            admin_dict[admin_input]()

        elif admin_input == '5':
            print(f"\nYou chose to go the main menu")
            return None

        elif admin_input == '6':
            src.exit_program()

        else:
            print(f"\n<{admin_input}> is an invalid input. Please Try Again")
            continue
