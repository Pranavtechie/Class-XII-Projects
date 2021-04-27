import src
from time import sleep
from cadet_password import Change_Cadet_Password_Main
from prettytable import PrettyTable
from basic_medical_data import Basic_Medical_Data_Main

# Establishing connection to the database
conn, cursor, sqlerror = src.Establish_Connection()


def Leaderboard(roll_no):
    """This function prints the leaderboard"""
    try:
        cursor.execute(
            f"SELECT house,total_points  FROM fit_house ORDER BY total_points desc")
        table = PrettyTable()
        table.field_names = ['Rank', 'House Name', 'Points']

        for i in range(1, 5):
            house, points = cursor.fetchone()
            if points is None:
                points = 0
            table.add_row([i, house, points])

        print(table)
        print("\n")
        sleep(1.5)

    except sqlerror:
        pass


def Check_Logs(roll_no):
    try:
        cursor.execute(
            f"SELECT timestamp FROM cadet_log WHERE roll_no = {roll_no} ORDER BY timestamp desc")
        data = cursor.fetchall()
        entries = 0
        log_table = PrettyTable()
        log_table.field_names = ['Time Stamp']

        for a in data:
            log_table.add_row([a])
            entries += 1

        print(log_table)
        print(f"\nYou have logged in {entries} Times")
        sleep(1.5)

    except sqlerror:
        print("\nAn Error Occurred while reading the data. Please Try Again")
        sleep(1.5)


def Cadet_Main(roll_no):
    """This function prints the Cadet Menu"""
    src.Cls()
    src.Main_Heading()

    while True:
        print("\n-------- Cadet Menu --------\n")
        print("Press (1) to check your Logs")
        print("Press (2) to See Fit House Championship Leaderboard")
        print("Press (3) to Edit you Basic Medical Data")
        print("Press (4) to Change Your Password")
        print("Press (5) to go to the Main Menu")
        print("Press (6) to exit the Program\n")

        cadet_main_dict = {'1': Check_Logs,
                           '2': Leaderboard,
                           '3': Basic_Medical_Data_Main,
                           '4': Change_Cadet_Password_Main}

        cadet_main_input = input("Enter your input from the above options: ")

        if cadet_main_input in cadet_main_dict:
            # Calling the function based on the dictionary
            cadet_main_dict[cadet_main_input](roll_no)

        elif cadet_main_input == '5':
            print("\nYou chose to go the Main Menu")
            sleep(1.5)
            src.Cls()
            break

        elif cadet_main_input == '6':
            src.Exit()

        else:
            print("\nYou have entered an Invalid Input. Please Try Again")
