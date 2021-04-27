import src
from time import sleep
from getpass import getpass

conn, cursor, sqlerror = src.Establish_Connection() # Establishing connection to the database

def Change_Password(roll_no):
    """This function gets the new password and changes the password in the database"""
    pass_1 = getpass("Enter your new Password: ") # Getting new Password
    pass_2 = getpass("Enter your new Password Again: ")

    if pass_1 == pass_2: # checking if both the passwords match
        try:
            #Sending the data to the database 'medic'
            cursor.execute(f"UPDATE cadet_user SET password = '{pass_1}' WHERE roll_no = {roll_no}")
            conn.commit()

            print("\nYou have successfully changed your password") # Printing the success message
            sleep(1.5)

        except sqlerror: # Handling the MySql Exception
            print("\nAn Error Occurred while sending data to the database. Please Try Again")
            sleep(1.5)

    else: # Printing Error Message when passwords do not match
        print("\nThe entered passwords do not match. Please Try Again")
        sleep(1.5)


def Change_Cadet_Password_Main(roll_no):
    """This function authorizes user for changing password"""

    print("\n-- Change Password --\n") # Printing the heading
    print("First Prove your Identity to change your password\n")


    roll_list = src.Get_Roll_No_List()

    if roll_no in roll_list: # checking if the roll number exists in the database
        password = getpass("Enter your password: ")
        cadet_password = src.Get_Cadet_Password(roll_no)

        if password == cadet_password: # checking if the entered password matches with the database
            print("\nYou are authorized to change you password\n")
            sleep(1.5)
            Change_Password(roll_no)  # Authorizing user for changing password

        else: # Handling Invalid password Exception
            print("You have entered an invalid password. Please Try Again")
            sleep(1.5)

    else: # Handling Invalid Roll Number Exception
        print("The entered Roll Number does not exists. Please Try Again")
        sleep(1.5)
