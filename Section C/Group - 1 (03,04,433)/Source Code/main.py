import src
import admin_main as adm
import cadet_main as cdt
from time import sleep
from getpass import getpass
from issue_medicine import change_issued_medicine_status
# Establishing connection to the database
conn, cursor, sqlerror = src.Establish_Connection()


def Validate_Admin():
    """This functions validates whether the user is admin"""
    print("\nYou chose to login as admin\n")
    username_input = input("\nEnter your username: ")  # Username Input
    username_list = src.Get_Admin_Username_List()

    if username_input in username_list:  # Validating Username
        password_input = getpass("Enter you password: ")  # Password Input
        user_password = src.Get_Admin_User_Password(username_input)

        if password_input == user_password:  # Validating Password
            print("\nYou have logged in as Admin Successfully\n")
            src.Redirecting()
            src.Cls()

            adm.Admin_Main()    # Redirecting to Admin if user in authorized

        else:  # Handling the invalid password
            print(
                "\nYou have entered an invalid password. Access Denied, Please Try Again\n")
            sleep(1.5)

    else:   # Handling Exception if username is not there
        print("\nYou have entered an invalid username.Please Try Again\n")
        sleep(1.5)


def Validate_Cadet():
    """This function validates whether the user is admin"""
    roll_no_input = input(
        "\nEnter you Roll Number: ")  # Taking Roll Number Input

    try:
        # Converting the Roll Number to Integer
        roll_no_input = int(roll_no_input)
        roll_no_list = src.Get_Roll_No_List()

        if roll_no_input in roll_no_list:  # Validating Roll Number
            # Password Input(Using getpass to avoid echoing of password)
            password = getpass("Enter you password: ")
            user_password = src.Get_Cadet_Password(roll_no_input)

            if password == user_password:  # Validating password
                print("\nYou have successfully logged in as Cadet")

                try:
                    # Adding a Cadet Log to the Database
                    cursor.execute(
                        f"INSERT INTO cadet_log VALUES ({roll_no_input}, CURRENT_TIMESTAMP())")
                    conn.commit()
                    src.Redirecting()
                    # Redirecting the user to the Cadet Menu
                    cdt.Cadet_Main(roll_no_input)

                except sqlerror:  # Handling the Database Exception
                    print(
                        "\nAn Error while sending data to the Database. Please Try Again")
                    sleep(1.5)

            else:  # Handling Password Exception
                print("\nYou have entered an Invalid Password, Please Try Again")
                sleep(1.5)
        else:  # Handling Roll Number Exception
            print("\nYou have entered an Invalid Roll No, Please Try Again")
            sleep(1.5)

    except ValueError:
        print("\nYou have not entered a number. Please Enter a Number")
        sleep(1.5)


def Main():
    """The main definition to start the program"""

    src.Cls()
    src.Main_Heading()

    while True:  # To make the options visible everytime
        # Printing the Main Menu
        print("---------------- Main Menu ----------------\n")
        print("Press (1) to log in as Admin")
        print("Press (2) to log in as Cadet")
        print("Press (3) to exit the program")

        # Dictionary to navigate to the required functions
        admin_dict = {'1': Validate_Admin,
                      '2': Validate_Cadet,
                      '3': src.Exit}

        main_input = input("Enter a valid input from the above options: ")

        # Validating main_input if true it will be navigated to the function
        if main_input in admin_dict:
            # Calling the function based on the dictionary
            admin_dict[main_input]()

        else:  # To avoid Error and display invalid message
            print("\nYou have entered an invalid input, please try again")
            sleep(1.5)
            continue


if __name__ == '__main__':  # Running the program
    src.Calculate_BMI_Points()
    src.Calculate_Eye_Sight_Points()
    src.Calculate_Total_Points()
    change_issued_medicine_status()
    Main()
