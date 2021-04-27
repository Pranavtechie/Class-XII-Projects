from os import system
import mysql.connector as sq
from getpass import getpass
from admin import admin_main
from guest import guest_main
import src


def heading():
    system('cls')
    print("<<<<< Garage Showcase >>>>>\n")


def main_menu():
    print("##### Main Menu #####\n")
    print("Press (1) to Login as Admin")
    print("Press (2) to Login as Guest")
    print("Press (3) to exit the program")


def admin_login():
    print("\nYou chose to login as admin")
    username_input = input("Please Enter your username : ")

    conn = sq.connect(host='localhost', user='root',
                      password='student', database='garage')
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT * FROM admin WHERE username = '{username_input.lower()}'")
    data = cursor.fetchone()
    if data is None:
        print("\nNo such username exists. Please Try Again")
        return None

    else:
        password_input = getpass("Please Enter your password : ")
        if username_input == data[1] and password_input == data[2]:
            print(f"You are authenticated.")
            admin_main(data[0])

        else:
            print(f"The entered password is invalid. Please Try Again")
            return None


def guest_login():
    print(f"\nYou chose to login as guest")

    name_input = input("\nPlease Enter your name : ")

    if name_input == '' or name_input == '\n':
        print("You have not entered any name. Please try again")
        return None

    else:
        guest_main(name_input)


heading()
while True:
    main_menu()

    user_dict = {
        '1': admin_login,
        '2': guest_login,
    }

    user_input = input("\nEnter your choice from the above options: ")

    if user_input in user_dict:
        user_dict[user_input]()

    elif user_input == '3':
        src.exit_program()

    else:
        print(f"<{user_input}> is an invalid input. Please Try Again")
        continue
