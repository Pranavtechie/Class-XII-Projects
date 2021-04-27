import src
from time import sleep
from getpass import getpass

# Establishing connection to the database
conn, cursor, sqlerror = src.Establish_Connection()


def Change_Password(username):
    """This function helps the admin user to change his password"""
    new_pass_1 = getpass("Enter your new password: ")
    new_pass_2 = getpass("Please Enter you new password Again: ")

    if new_pass_1 == new_pass_2:
        try:
            cursor.execute(
                f"UPDATE admin_user SET password = '{new_pass_1}' WHERE username = '{username}'")
            conn.commit()

        except sqlerror:
            print(
                "\nAn Error occurred while sending data to the database. Please Try Again")
            sleep(1.5)

    else:
        print("\nThe Entered Passwords Do Not Match. Please Try Again.")
        sleep(1.5)


def Admin_Password_Main():
    """This function verifies if the user is authorized to change his password"""
    print("\n-- Change Password --\n")
    print("First Prove your Identity to change your password")

    username = input("Enter your Username: ")
    username_list = src.Get_Admin_Username_List()
    if username in username_list:
        password = getpass("Enter your Password: ")
        table_password = src.Get_Admin_User_Password(username)

        if password in table_password:
            print("\nYou are authorized to change you password\n")
            sleep(1.5)
            Change_Password(username)

        else:
            print("Incorrect Password was Entered. Please Try Again.")

    else:
        print("\nSorry. The Entered username does not exists. Please Try Again.")
        sleep(1.5)
