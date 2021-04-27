from time import sleep
import src
from prettytable import PrettyTable

# Establishing connection to the database
conn, cursor, sqlerror = src.Establish_Connection()


def Admit_Cadet():
    """This function lets the admin user to admit a cadet"""
    print("\n--- Admit Cadet ---\n")
    roll_no_input = input("Enter the Roll No of the Cadet: ")
    try:
        roll_no_input = int(roll_no_input)
        roll_no_check = src.Check_Roll_No(roll_no_input)

        if roll_no_check:
            reason = input("Enter the reason for Admission: ")
            print("Enter the Date of the Discharge")
            discharge_date = src.Input_Date()
            confirmation = input("\nPlease Confirm the admission (Y / N): ")

            if confirmation in ['Y', 'y']:

                database_confirmation = src.Check_If_Admitted(roll_no_input)

                if not database_confirmation:

                    try:
                        cursor.execute(
                            f"INSERT INTO admission VALUES ({roll_no_input},'{reason}','{discharge_date}',CURRENT_TIMESTAMP(),'Admitted',Null)")
                        conn.commit()
                        src.Add_Admission_Points(roll_no_input)
                        cursor.execute(
                            f"SELECT name FROM cadet WHERE roll_no = {roll_no_input}")
                        cadet_name = cursor.fetchone()[0]
                        print(f"\nYou have successfully admitted {cadet_name}")
                        sleep(1.5)

                    except sqlerror:
                        print(
                            "\nAn Error occurred while sending data to database.Please Try Again")
                        sleep(1.5)

                else:
                    print("\nThe cadet can't be admitted")
                    sleep(1.5)

            else:
                print("\nYou have cancelled the admission.\n")
                sleep(1.5)

        else:
            print("\nThe Entered Roll Number does not Exists. Please Try Again\n")
            sleep(1.5)

    except ValueError:
        print(
            "\nYou have not entered a correct value for the Roll Number. Please Try Again")
        sleep(1.5)


def Discharge_Cadet():
    """This function lets admin user to discharge a cadet"""
    print("\n-- Discharge Cadet --\n")

    try:
        cursor.execute(f"""SELECT admission.roll_no, cadet.name, admission.cause, admission.discharge_date  
                        FROM admission, cadet WHERE cadet.roll_no = admission.roll_no and admission.status = 'Admitted'""")
        data = cursor.fetchall()

        if data is None:
            print("No cadet is admitted. You can't discharge anyone.\n")
            sleep(1.5)

        else:
            table = PrettyTable()
            table.field_names = ['Roll No', 'Name', 'Cause', 'Discharge Date']
            roll_no_list = []
            for no, name, cause, date in data:
                table.add_row([no, name, cause, date])
                roll_no_list.append(no)

            print(table)

            roll_no = input(
                "Enter the Roll Number of the Cadet to Discharge: ")
            try:
                roll_no = int(roll_no)
                if roll_no in roll_no_list:

                    try:
                        cadet_name = src.Get_Cadet_Name(roll_no)
                        confirm = input(
                            f"Are you sure you want to discharge {cadet_name} (Y / N): ")

                        if confirm in ['y', 'Y']:
                            timestamp = src.Get_Latest_Timestamp(roll_no)

                            try:
                                cursor.execute(f"""UPDATE admission SET status = 'Discharged',
                                                discharge_timestamp = current_timestamp() WHERE roll_no = {roll_no} and 
                                                timestamp = '{timestamp}'""")
                                conn.commit()

                                print(
                                    f"\nYou have successfully discharged {cadet_name}")
                                sleep(1.5)

                            except sqlerror:
                                print(
                                    "\nAn Error occurred while updating the data. Please Try Again")
                                sleep(1.5)

                        else:
                            print(f"\nYou chose not to discharge {cadet_name}")
                            sleep(1.5)

                    except ValueError:
                        print(
                            "\nYou have entered an invalid value for Roll Number. Please Try Again")
                        sleep(1.5)

                else:
                    print(
                        "\nYou can't discharge the cadet as the cadet is not admitted.")
                    sleep(1.5)
            except ValueError:
                print("You have entered an invalid Roll No. Please Try Again")
                sleep(1.5)

    except sqlerror:
        print("\nAn Error Occurred while parsing the Admission Data. Please Try Again\n")
        sleep(1.5)


def Extend_Discharge_Confirmation():
    """This function takes the required input to extend the discharge date of the cadet"""
    print("\n-- Extend Discharge --\n")
    Active_Admissions()
    roll_no_input = input(
        "Enter the Roll Number of the cadet to extend Discharge: ")

    try:
        roll_no_input = int(roll_no_input)

        confirm = input("\nDo you want to extend the discharge date (Y / N): ")

        if confirm in ['y', 'Y']:
            Extend_Discharge(roll_no_input)

        else:
            print(f"You chose not to extend the discharge of the cadet")

    except ValueError:
        print("\nAn Error Occurred while evaluating roll number or connecting to the database. ")
        sleep(1.5)


def Extend_Discharge(roll_no):
    """This function extends the discharge date of a admitted cadet"""
    print("\nEnter the new data for discharge")
    new_date = src.Input_Date()
    timestamp = src.Get_Latest_Timestamp(roll_no)

    try:
        cursor.execute(f"""UPDATE admission SET discharge_date = '{new_date}' WHERE roll_no = {roll_no} AND
                        status = 'Admitted' and timestamp = '{timestamp}'""")
        conn.commit()

        print("\nYou have successfully updated the discharge date")

    except sqlerror:
        print("\nAn Error Occurred while sending the data. Please Try Again")
        sleep(1.5)


def Admission_Logs():
    """This function prints the admission logs to the admin user"""
    print("\n-- Admission Logs --\n")
    try:
        cursor.execute(f"""SELECT admission.*,cadet.name FROM admission,cadet WHERE admission.roll_no = cadet.roll_no
                        ORDER BY timestamp DESC""")
        data = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ['Roll No', 'Name', 'Cause',
                             'Discharge On', 'Admission Time', 'Status']

        for roll, cause, discharge, timestamp, status, discharge_time, name in data:
            table.add_row([roll, name, cause, discharge, timestamp, status])

        if data is None:
            print("\nThere are no admission Logs to display")
            sleep(1.5)

        else:
            print(table)
            print("\n")

    except sqlerror:
        print(
            "\nAn Error Occurred while receiving data from the database. Please Try Again")
        sleep(1.5)


def Discharge_Logs():
    """This functions prints all the discharge logs to the admin user"""
    print("\n-- Discharge Logs --\n")
    try:
        cursor.execute(f"""SELECT admission.*, cadet.name FROM admission, cadet WHERE admission.roll_no = cadet.roll_no
                        AND discharge_timestamp IS NOT NULL AND status = 'Discharged'
                        ORDER BY discharge_timestamp DESC""")
        data = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ['Roll No', 'Name', 'Cause',
                             'Discharge Date', 'Admission Time', 'Status', 'Discharged On']

        for roll, cause, discharge, timestamp, status, discharge_time, name in data:
            table.add_row([roll, name, cause, discharge,
                           timestamp, status, discharge_time])

        if data is None:
            print("\nThere are discharges to show")
            sleep(1.5)

        else:
            print(f"\n{table}")
            sleep(1.5)

    except sqlerror:
        print(
            "\nAn error occurred while receiving data from the database. Please Try Again")
        sleep(1.5)


def Active_Admissions():
    """This function prints all the active admissions to the admin user"""
    print("\n-- Active Admissions --")
    try:
        cursor.execute(f"""SELECT admission.roll_no, cadet.name, admission.cause, admission.discharge_date, 
                        admission.timestamp FROM admission, cadet WHERE cadet.roll_no = admission.roll_no and
                        status = 'Admitted'""")
        data = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ['Roll No', 'Name', 'Cause',
                             'Discharge Date', 'Time of Admission']

        for no, name, cause, discharge, time in data:
            table.add_row([no, name, cause, discharge, time])

        if data is None:
            print("\nThere are No Active Admissions")
            sleep(1.5)

        else:
            print(table)
            print('\n')

    except sqlerror:
        print("\nAn Error occurred while parsing the data. Please Try Again.")


def Admit_Discharge_Main():
    """This function prints the menu of the discharge to the admin user"""
    src.Cls()

    while True:
        print("\n---------- Admission/Discharge Menu ----------\n")
        print("Press (1) to Admit a Cadet")
        print("Press (2) to Discharge Cadet")
        print("Press (3) to Extend Discharge")
        print("Press (4) to see Admission Logs")
        print("Press (5) to see Discharge Logs")
        print("Press (6) to see Active Admissions")
        print("Press (7) to go to Admin Menu")
        print("Press (8) to Exit the Program\n")

        admit_dict = {'1': Admit_Cadet,
                      '2': Discharge_Cadet,
                      '3': Extend_Discharge_Confirmation,
                      '4': Admission_Logs,
                      '5': Discharge_Logs,
                      '6': Active_Admissions,
                      '8': src.Exit}

        admit_input = input("Enter a Valid input from the above options: ")

        if admit_input in admit_dict:
            # Calling the function based on the dictionary
            admit_dict[admit_input]()

        elif admit_input == '7':
            print("\nYou chose to go the Admin Menu")
            sleep(1.5)
            break

        else:
            print("\nYou have entered an Invalid Input. Please Try Again")
            sleep(1.5)
            continue
