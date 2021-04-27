import src
from time import sleep
from prettytable import PrettyTable


def List_Of_Cadet_Login():
    print("-- List of Cadets' Logins --")
    conn, cursor, sqlerror = src.Establish_Connection()
    rollno = input("Enter the Roll Number to see Log Ins : ")
    try:
        rollno = int(rollno)
        try:

            table = PrettyTable()
            table.field_names = ['Roll No', 'Name', 'Class', 'Timestamp']
            cursor.execute(
                f"SELECT cadet_log.roll_no, name ,class, timestamp from cadet_log,cadet WHERE cadet_log.roll_no = {rollno} and cadet.roll_no = cadet_log.roll_no ORDER BY timestamp desc")
            data = cursor.fetchall()

            for row in data:
                table.add_row(row)
            print(table)
            print("\n")
            sleep(1.5)

        except sqlerror:
            print("\nAn Error Occurred while parsing the data. Please Try Again")
            sleep(1.5)
    except ValueError:
        print("\n<{rollno}> is invalid. Please Try Again")
        sleep(1.5)
    conn.close()


def List_Of_Cadets_Logins():
    conn, cursor, sqlerror = src.Establish_Connection()
    query = "select cadet_log.roll_no, cadet.name, count(cadet_log.roll_no) as 'Logged in Times', cadet.class, cadet.section, cadet.house from cadet_log natural join cadet group by cadet_log.roll_no"
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ['Roll No', 'Name',
                             'No of Times logged in', 'Class', 'Section', 'House']
        for row in data:
            table.add_row(row)

        print(table)
        print("\n")
        sleep(1.5)

    except sqlerror:
        print("\nAn Error Occurred while parsing the data. Please Try Again")
        sleep(1.5)
    conn.close()


def Cadet_Medications():
    print("-- Cadet Medications --")
    rollno = input("Enter the roll no : ")
    conn, cursor, sqlerror = src.Establish_Connection()
    try:
        rollno = int(rollno)
        cursor.execute(f"SELECT * FROM cadet WHERE roll_no = {rollno}")
        cadet_data = cursor.fetchone()
        try:
            cursor.execute(
                f"select * from issue_medicine where roll_no = {rollno}")
            medicine_data = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ['Roll No', 'Cause', 'medicine',
                                 'quantity', 'timestamp', 'end_date', 'status']
            if len(cadet_data) == 0:
                print('The entered roll no does not exists. Please Try Again')
                conn.close()
                return None
            print("-------------------------")
            print(f"Roll No : {cadet_data[0]}")
            print(f"Name : {cadet_data[1]}")
            print(f"Class : {cadet_data[2]}")
            print(f"Section : {cadet_data[3]}")
            print(f"House : {cadet_data[4]}")
            print("-------------------------")
            if medicine_data == []:
                print("Nothing to show. No data is found for the cadet.")
                conn.close()
                return None
            for row in medicine_data:
                table.add_row(row)
            print(table)
            sleep(1.5)
        except sqlerror:
            print("An Error Occurred while parsing the Data. Please Try Again")
            sleep(1.5)

    except ValueError:
        print("You have entered an invalid roll no. Please Try Again")
        sleep(1.5)
    conn.close()


def Cadet_Admissions():
    conn, cursor, sqlerror = src.Establish_Connection()
    rollno = input("Enter the Roll Number to see the Admissions : ")
    try:
        rollno = int(rollno)
        cursor.execute(f"SELECT * FROM cadet WHERE roll_no = {rollno}")
        cadet_data = cursor.fetchone()
        if len(cadet_data) == 0:
            print(f"<{rollno}> does not exists. Please Try Again")
            conn.close()
            return None
        print("-------------------------")
        print(f"Roll No : {cadet_data[0]}")
        print(f"Name : {cadet_data[1]}")
        print(f"Class : {cadet_data[2]}")
        print(f"Section : {cadet_data[3]}")
        print(f"House : {cadet_data[4]}")
        print("-------------------------")
        try:
            cursor.execute(f"select * from admission where roll_no = {rollno}")
            data = cursor.fetchall()
            table = PrettyTable()
            table.field_names = [
                'Roll No', 'Cause', 'Discharge Date', 'Timestamp', 'Status', 'Discharge Timing']
            for row in data:
                table.add_row(row)

            print(table)
            print('\n')
            sleep(1.5)

        except sqlerror:
            print("An Error Occurred while parsing the data. Please Try Again")
            sleep(1.5)

    except ValueError:
        print(f"<{rollno}> is an invalid input. Please Try Again")
        sleep(1.5)
    conn.close()


def Cadet_Log_Main():
    src.Cls()

    while True:

        print("-------- Cadet Log Menu --------\n")
        print("Press (1) to see List of Cadets' Login")
        print("Press (2) to see List of Cadet Login")
        print("Press (3) to see Cadet Medications")
        print("Press (4) to see Cadet Admissions/Discharges")
        print("Press (5) to go to Admin Menu")
        print("Press (6) to Exit the Program\n")

        cadet_log_dict = {'1': List_Of_Cadets_Logins,
                          '2': List_Of_Cadet_Login,
                          '3': Cadet_Medications,
                          '4': Cadet_Admissions,
                          '6': src.Exit}

        cadet_log_input = input("Enter your input from the above options: ")

        if cadet_log_input in cadet_log_dict:
            # Calling the function based on the dictionary
            cadet_log_dict[cadet_log_input]()

        elif cadet_log_input == '5':  # Taking to Admin Menu
            print("\nYou chose to go the Admin Menu")
            sleep(1.5)
            break

        else:
            print("\nYou have entered an Invalid Input. Please Try Again")
            continue
