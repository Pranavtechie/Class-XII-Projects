import src
from time import sleep
from prettytable import PrettyTable

# Establishing connection to the database
conn, cursor, sqlerror = src.Establish_Connection()


def Issue_Medicine_Confirmation():
    print("\n --Issue Medicine --")
    i = 1
    roll_no = input("Enter the Roll Number: ")
    first_value = None
    second_value = None
    while True:

        try:
            roll_no = int(roll_no)
            med_name = input("Enter the Medicine Name: ")
            probable_medicine_list, probable_table = src.Get_Probable_Medicine(
                med_name)
            if med_name in probable_medicine_list:
                confirmation = input(
                    "\nAre you sure you want to issue the medicine (Y / N): ")
                if confirmation in ['Y', 'y']:
                    first_value = Expiry_Check(roll_no, med_name)

                else:
                    print("\nYou chose not to issue the medicine")
                    sleep(1.5)

            elif probable_medicine_list:
                print("\nProbable Medicine Table")
                print(probable_table)
                print(
                    "If the medicine is in the Probable list.Please Enter the Medicine Name as in the Table")

                new_med_name = input("Please Enter the medicine as in Table: ")
                if new_med_name in probable_medicine_list:
                    confirm_input = input(
                        "Are you sure you want to issue this medicine (Y / N): ")

                    if confirm_input in ['Y', 'y']:
                        second_value = Expiry_Check(roll_no, new_med_name)

                    else:
                        print("\nYou chose not to issue the medicine")
                        sleep(1.5)
                else:
                    print(
                        "\nYou have entered the medicine name wrong for two times.Try Again\n")
                    sleep(1.5)
                    break

        except ValueError:
            print("\nYou have entered an invalid value for Roll No.Please Try Again")
            sleep(1.5)

        if first_value or second_value:
            next_medicine = input(
                f"You have issued {i} Medicine(s) to Roll No {roll_no}.Do you want to issue more(Y / N): ")
            if next_medicine in ['Y', 'y']:
                i += 1
                continue

            else:
                print("\nYou have closed the issue medicine.\n")
                sleep(1.5)
                break
        else:
            print("\nYou have not issued any medicine yet! Try Again\n")
            sleep(1.5)
            break


def Expiry_Check(roll_no, med_name):

    check = src.Check_Expiry(med_name)

    if check:
        return Issue_Medicine(roll_no, med_name)

    else:
        print("\nThe medicine has expired. You cannot Issue the Medicine")
        sleep(1.5)
        return False


def Issue_Medicine(roll_no, med_name):
    qty = input(f"Enter the Quantity you want to Issue for '{med_name}': ")

    try:
        qty = int(qty)
        cause = input(f"Enter the Cause for Issuing Medicine '{med_name}': ")
        print("Enter the date by when the medicine should be consumed:")
        completion = src.Input_Date()

        try:

            cursor.execute(
                f"INSERT INTO issue_medicine VALUES ({roll_no},'{cause}','{med_name}',{qty},CURRENT_TIMESTAMP(),'{completion}', 'Under Medication')")
            conn.commit()
            cursor.execute(
                f"UPDATE medicine SET quantity = quantity - {qty} WHERE medicine_name = '{med_name}'")
            conn.commit()

            print(
                f"\nYou have successfully issued '{med_name}' to Roll No {roll_no}")
            sleep(1.5)
            return True

        except sqlerror:
            print(
                "\nAn Error occurred while sending data to the database. Please Try Again")
            sleep(1.5)
            return False

    except ValueError:
        print("\nYou have entered an invalid value for Quantity. Please Try Again")
        sleep(1.5)
        return False


def Under_Medication():
    print("-- Under Medication List --")
    try:
        cursor.execute("select issue_medicine.roll_no, cadet.name, cadet.class, issue_medicine.cause, medicine, quantity, timestamp, end_date, status from issue_medicine natural join cadet where issue_medicine.status = 'Under Medication'")
        data = cursor.fetchall()
        med_table = PrettyTable()
        med_table.field_names = ['Roll No', 'Name', 'Class', 'Cause',
                                 'Medicine', 'Qty', 'Timestamp', 'End Date', 'Status']
        for row in data:
            med_table.add_row(row)

        print(med_table)
        print('\n')

    except sqlerror:
        print("An Error occurred while fetching the data. Please Try Again")
        return None


def See_Issued_Medicine():
    print("\n-- Issued Medicine Table\n")

    try:
        cursor.execute("""SELECT issue_medicine.roll_no,name,class,cause,medicine,quantity,timestamp,end_date,status
        FROM issue_medicine, cadet WHERE cadet.roll_no = issue_medicine.roll_no ORDER BY timestamp desc""")
        data = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ['Roll No', 'Name', 'Class', 'Cause',
                             'Medicine', 'Qty', 'TimeStamp', 'End Date', 'Status']

        for roll_no, name, clas, cause, medicine, quantity, timestamp, end_date, status in data:
            table.add_row([roll_no, name, clas, cause, medicine,
                           quantity, timestamp, end_date, status])

        print(table)
        sleep(1.5)
        print('\n')

    except sqlerror:
        print("\nAn Error occurred while parsing the Data. Please Try Again.")
        sleep(1.5)


def change_issued_medicine_status():
    """This function changes the cadet's medication status as per End Date"""
    cursor.execute(
        "select * from issue_medicine where end_date < current_date() and status = 'Under Medication'")
    data = cursor.fetchall()

    if data == []:
        return None

    updated_entries = 0
    for row in data:
        time_id = row[4]
        print(type(time_id))
        status = 'Healthy'

        cursor.execute(
            f"UPDATE issue_medicine set status = 'Healthy' where timestamp = '{time_id}'")
        conn.commit()
        updated_entries += 1

    print("Number of updated Entries =", updated_entries)


def Issue_Medicine_Main():
    src.Cls()

    while True:
        print("------- Issue Medicine Menu -------\n")
        print("Press (1) to Issue Medicine")
        print("Press (2) to see list of Cadet's Under Medication")
        print("Press (3) to see the list of all Issued Medicines")
        print("Press (4) to go to Admin Menu")
        print("Press (5) to exit the Program\n")

        issue_dict = {'1': Issue_Medicine_Confirmation,
                      '2': Under_Medication,
                      '3': See_Issued_Medicine,
                      '5': src.Exit}

        issue_input = input("Enter a valid input from the available options: ")

        if issue_input in issue_dict:
            # Calling the function based on the dictionary
            issue_dict[issue_input]()

        elif issue_input == '4':
            print("\nYou chose to go the Admin Menu")
            sleep(1.5)
            break

        else:
            print("\nYou have entered an Invalid Input. Please Try Again\n")
            sleep(1.5)
            continue
