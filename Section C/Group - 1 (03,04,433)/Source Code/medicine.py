import src
from time import sleep
from prettytable import PrettyTable
from update_medicine import Update_Medicine

# Establishing connection to the database
conn, cursor, sqlerror = src.Establish_Connection()


def Medicine_List():
    """This function prints the list of medicine table"""
    cursor.execute(f"SELECT * FROM medicine")  # Getting data from MySql
    medicine_data = cursor.fetchall()
    medicine_table = PrettyTable()  # Creating Table named medicine_table
    medicine_table.field_names = ['Medicine Name',
                                  'Usage / Indication', 'Quantity', 'Expiry Date']

    for a, b, c, d in medicine_data:  # Adding Data to the medicine_table
        medicine_table.add_row([a, b, c, d])

    print("\n")
    print(medicine_table, '\n')
    sleep(2)


def Add_Medicine_Confirmation():
    """This function handles the Prerequisites before adding the new medicine to the database"""
    print("\n-- Add Medicine --\n")
    med_name_input = input("Enter the Medicine Name to Add: ")
    probable_med_list, probable_med_table = src.Get_Probable_Medicine(
        med_name_input)

    if med_name_input in probable_med_list:
        print("\nThe medicine you want to enter already exists. Try Updating Them")
        sleep(1.5)

    elif probable_med_list:
        print("\nProbable Medicine Table\n")
        print(probable_med_table)
        print("If you medicine is not in the probable list you can add them")
        confirm_add = input(
            "Are you sure you want to add new medicine (Y / N): ")

        if confirm_add in ['y', 'Y']:
            Add_Medicine()

        else:
            print("\nYou chose not to add a new medicine")
            sleep(1.5)

    else:
        Add_Medicine()


def Add_Medicine():
    """This function gets required inputs and adds the new medicine to the database"""
    med_name = input("Please enter the medicine name again: ")
    usage = input("Enter the Usage / Indication of the Medicine: ")
    quantity = input("Enter the quantity of the Medicine: ")
    print("\nPlease Enter the Medicine Expiry Date Carefully")
    med_date = src.Input_Date()

    try:
        cursor.execute(
            f"INSERT INTO medicine VALUES ('{med_name}','{usage}',{quantity},'{med_date}')")
        conn.commit()

        print("\nYou have successfully added a new medicine to the Database.")
        sleep(1.5)

    except sqlerror:
        print("\nAn Error occurred while sending data to the medicine. Please Try Again")
        sleep(1.5)


def Update_Medicine_Confirmation():
    """This function manages the prerequisites before updating the medicine
    and redirects it the update_medicine module"""
    print("\n-- Update Medicine --")
    med_name = input("Enter the Medicine Name: ")
    probable_med_list, probable_med_table = src.Get_Probable_Medicine(med_name)

    if med_name in probable_med_list:
        Update_Medicine(med_name)

    elif probable_med_list:
        print("\nProbable Medicine Table\n")
        print(probable_med_table)
        print("If the medicine is not in the probable list you can update them")
        confirm_add = input(
            "Are you sure you want to add/update new medicine (Y / N): ")

        if confirm_add in ['Y', 'y']:
            print("\nPlease Enter the Medicine Name as in the Table")
            second_med_name = input("Please Enter the medicine as in Table: ")

            if second_med_name in med_name:
                Update_Medicine(second_med_name)

            else:
                print("\nYou have entered an Incorrect Medicine Name. Try Again")

        else:
            print("\nYou chose not to update the medicine.")
            sleep(1.5)

    else:
        print("\nWe did not find any probable medicine for your input. Please Try Again")
        sleep(1.5)


def See_Expiry():
    print("\n-- See Expiry --\n")
    medicine_table, expiry_list = src.Scan_For_Expiry()

    if medicine_table:
        print(medicine_table)
        sleep(1.5)

    else:
        print("\nNo Medicines have expired Till Date.")
        sleep(1.5)


def Delete_Expired_Medicine():
    print("-- Delete Expired Medicine")
    medicine_table, expiry_list = src.Scan_For_Expiry()

    if medicine_table:
        print(medicine_table)

        med_input = input("Enter the Medicine you want to delete: ")

        if med_input in expiry_list:
            cursor.execute(
                f"DELETE FROM medicine WHERE medicine_name = '{med_input}'")
            conn.commit()

            print(
                f"You have successfully deleted {med_input} from the database.")
            sleep(1.5)

        else:
            print(
                "You have entered an invalid medicine name to delete. Please Try Again.")
            sleep(1.5)

    else:
        print("There are no expired medicine. You don't need to delete any of them")
        sleep(1.5)


def Medicine_Main():
    """This function runs the Medicine Management Menu"""
    src.Cls()

    while True:
        print("\n-------- Medicine Management Menu --------\n")
        print("Press (1) to see the Medicine List")
        print("Press (2) to Add a Medicine")
        print("Press (3) to See Expired Medicines")
        print("Press (4) to Update a Medicine")
        print("Press (5) to Delete a Expired Medicine")
        print("Press (6) to go to Admin Menu")
        print("Press (7) to Exit the Program\n")

        medicine_dict = {'1': Medicine_List,
                         '2': Add_Medicine_Confirmation,
                         '3': See_Expiry,
                         '4': Update_Medicine_Confirmation,
                         '5': Delete_Expired_Medicine,
                         '7': src.Exit}

        medicine_input = input("Enter a valid input from the above options: ")

        if medicine_input in medicine_dict:
            # Calling the function based on the dictionary
            medicine_dict[medicine_input]()

        elif medicine_input == '6':  # To break the loop for Admin Menu
            print("\nYou chose to go to the Admin Menu")
            sleep(1.5)
            break

        else:   # Handling Invalid input exception
            print("You have entered an invalid input, Please Try Again")
            sleep(1.5)
            continue
