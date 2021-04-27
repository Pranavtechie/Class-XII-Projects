import src
from time import sleep

# Establishing connection to the database
conn, cursor, sqlerror = src.Establish_Connection()


def Update_Medicine_Name(med_name):
    print("\n-- Update Medicine Name --\n")
    new_med_name = input("Enter the New Medicine Name: ")

    try:
        cursor.execute(
            f"UPDATE medicine SET medicine_name = '{new_med_name}' WHERE medicine_name = '{med_name}'")
        conn.commit()

        print("\nYou have successfully updated the name of the medicine.")
        sleep(1.5)

    except sqlerror:
        print(
            "\nAn Error Occurred while sending data. Please check the Medicine Name Again.")
        sleep(1.5)


def Update_Usage(med_name):
    print("\n-- Update Medicine Usage / Indication --\n")

    new_usage = input("Enter the New Usage / Indication: ")

    try:
        cursor.execute(
            f"UPDATE medicine SET usage = '{new_usage}' WHERE medicine_name = '{med_name}'")
        conn.commit()

        print("\nYou have successfully updated the Usage / Indication of the Medicine")
        sleep(1.5)

    except sqlerror:
        print("An Error occurred while sending the data to the database. Please Try Again")
        sleep(1.5)


def Update_Quantity(med_name):
    print("\n-- Update Quantity --\n")
    quantity = input("Enter the Updated quantity: ")

    try:
        quantity = int(quantity)

        try:
            cursor.execute(
                f"UPDATE medicine SET quantity = {quantity} WHERE medicine_name = '{med_name}'")
            conn.commit()

            print("\nYou have successfully updated the quantity")
            sleep(1.5)

        except sqlerror:
            print(
                "\nAn Error occurred while sending data to the database. Please Try Again")
            sleep(1.5)

    except ValueError:
        print("\nYou have entered an invalid value for quantity. Please Try Again")
        sleep(1.5)


def Update_Expiry(med_name):
    print("\n-- Updated Expiry Date --\n")
    print("Enter the new Expiry Date")
    new_date = src.Input_Date()
    try:
        cursor.execute(
            f"UPDATE medicine SET expiry = '{new_date}' WHERE medicine_name = '{med_name}'")
        conn.commit()

        print("\nYou have successfully updated the expiry date")
        sleep(1.5)

    except sqlerror:
        print("\nAn Error occurred while sending data to the database. Please Try Again")
        sleep(1.5)


def Update_Medicine(med_name):

    while True:
        print("\n-- Update Medicine --\n")
        print("Press (1) to Update the Medicine Name")
        print("Press (2) to Update the Usage / Indication")
        print("Press (3) to Update the Quantity")
        print("Press (4) to Update the Expiry Date")
        print("Press (5) to go back to Manage Medicine Menu")
        print("Press (6) to Exit the Program\n")

        update_dict = {'1': Update_Medicine_Name,
                       '2': Update_Usage,
                       '3': Update_Quantity,
                       '4': Update_Expiry}

        update_input = input("Enter a valid input from the Above Options: ")

        if update_input in update_dict:
            update_dict[update_input](med_name)

        elif update_input == '5':
            print("\nYou chose to go to the Manage Medicine Menu")
            sleep(1.5)
            break

        elif update_input == '6':
            src.Exit()

        else:
            print("\nYou have entered an invalid option. Please Try Again")
            sleep(1.5)
