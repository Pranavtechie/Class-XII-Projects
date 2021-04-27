import src
from time import sleep
from medicine import Medicine_Main
from admission_discharge import Admit_Discharge_Main
from issue_medicine import Issue_Medicine_Main
from cadet_log import Cadet_Log_Main
from admin_password import Admin_Password_Main


def Admin_Main():
    """This function prints the main menu for the admin user"""
    src.Cls()
    src.Main_Heading()

    while True:
        # Printing the Menu
        print("\n--------- Admin Menu ---------\n")
        print("Press (1) to Manage Medicines")
        print("Press (2) to Manage Admissions/Discharges")
        print("Press (3) to Issue Medicines")
        print("Press (4) to See the Cadets' Data")
        print("Press (5) to Change your Password")
        print("Press (6) to Go to the Main Menu")
        print("Press (7) to Exit the Program\n")

        # Admin Menu Dictionary to Navigate to specific Modules
        admin_menu_dict = {'1': Medicine_Main,
                           '2': Admit_Discharge_Main,
                           '3': Issue_Medicine_Main,
                           '4': Cadet_Log_Main,
                           '5': Admin_Password_Main,
                           '7': src.Exit}

        # Taking the input from the User
        admin_menu_input = input("Enter your input from the above options: ")

        if admin_menu_input in admin_menu_dict:
            # Calling the function based on the dictionary
            admin_menu_dict[admin_menu_input]()

        elif admin_menu_input == '6':
            print("\nYou chose to go to the Main Menu")
            sleep(1)
            break

        else:
            print("\nYou have entered an Invalid Input. Please Try Again")
            sleep(1.5)
            continue
