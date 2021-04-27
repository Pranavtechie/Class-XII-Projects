from db_connect import est_conn
import os
from time import sleep
from getpass import getpass
from admin_main import admin_menu
from customer_main import customer_menu
from the_exit import exit_program


def clear_main_screen():
    os.system('cls')
    print("--------------------------- VSR Mobiles --------------------------")
    print("----------------------- Mobile Phone Store -----------------------")
    print("--------------------- SAINIK SCHOOL KALIKIRI ---------------------\n\n")

conn, cursor = est_conn()

def username_list():
    cursor.execute("SELECT username FROM admin_users")
    data = cursor.fetchall()
    users_list = [row[0] for row in data]

    return  users_list


def get_help():
    os.system('help.pdf')
    print("\n Thank you for using our help service")
    sleep(4)



def match_password(user,user_password):
    cursor.execute(f"SELECT password FROM admin_users WHERE username = '{user}'")
    table_password = cursor.fetchone()[0]
    evaluation = user_password == table_password

    if evaluation:
        return True

    else:
        return False


def customer_login_process():
    print("\nYou are now logging in as customer\n")
    name = input("Enter you name: ")
    cursor.execute(f"INSERT INTO customer_users VALUES ('{name}',CURRENT_TIMESTAMP())")
    conn.commit()

    print("You are logged in as customer\n")
    sleep(1)

    customer_menu()


def admin_login_process():
    username = input("Enter your username: ")
    users_list = username_list()

    if username in users_list:
        password = getpass(prompt="Enter the password : ")
        result = match_password(username, password)

        if result:
            admin_menu()

        else:
            print("\nThe entered password does not match with the given username. Please try again")
            sleep(1.5)

    else:
        print("\nThe entered username does not exists. Please try again")
        sleep(1.5)



def the_main():

    while True:
        clear_main_screen()

        print("\nYou are in the Main Menu")
        print("\nPress (1) to Login as Admin")
        print("Press (2) to Login as Customer")
        print("Press (3) to get help")
        print("Press (4) to exit the program")

        check_dict = {'1' : admin_login_process, '2' : customer_login_process, '3' : get_help, '4' : exit_program}

        getting_input = input("Enter an input from the available options: ")

        if getting_input in check_dict:
            check_dict[getting_input]()

        else:
            print("\nYou have entered an invalid input please try again")
            sleep(2)
            continue


if __name__ == '__main__':
    the_main()
