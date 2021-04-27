import mysql.connector as sql
from mysql.connector import Error
from time import sleep
import os
import datetime
from prettytable import PrettyTable
from math import fabs

house_list = ['Godavari', 'Krishna', 'Penna', 'Tungabhadra']


def Establish_Connection():
    """This function establishes connection to mysql database"""
    connection = sql.connect(
        host='localhost', user='root', password='student', database='medic')
    mycursor = connection.cursor()

    return connection, mycursor, Error


# Establishing connection to the database
conn, cursor, sqlerror = Establish_Connection()


def Cls():
    """This function clears the clears the screen in the command prompt"""
    os.system('cls')


def Exit():
    """This function prints the Thank You message when a user exits the program"""
    print("Thank you for using the program")
    sleep(1.5)
    exit()


def Main_Heading():
    """This function prints the main heading"""
    print("---------- SAINIK SCHOOL KALIKIRI -----------")
    print("----------- Dispensary Management -----------\n")


def Get_Admin_Username_List():
    """This function returns the list of admin usernames"""

    cursor.execute("SELECT username FROM admin_user")
    username_data = cursor.fetchall()
    username_list = []

    for row in username_data:
        username_list.append(row[0])

    return username_list


def Get_Admin_User_Password(username):
    """This function returns the password of a given user"""
    cursor.execute(
        f"SELECT password FROM admin_user WHERE username = '{username}'")
    password = cursor.fetchone()[0]

    return password


def Get_Admin_Name(username):
    """This function returns the name of the admin user given the username"""
    cursor.execute(
        f"SELECT name FROM admin_user WHERE username = '{username}'")
    name = cursor.fetchone()[0]

    return name


def Get_Cadet_Name(roll_no):
    """This function returns the name of the cadet based on his roll number"""
    cursor.execute(f"SELECT name FROM cadet WHERE roll_no = {roll_no}")
    name = cursor.fetchone()[0]

    return name


def Get_Roll_No_List():
    """This function returns the list of roll no of the cadets"""
    roll_list = []
    cursor.execute("SELECT roll_no FROM cadet")
    data = cursor.fetchall()

    for row in data:
        roll_list += row

    return roll_list


def Get_Cadet_Password(roll_no):
    """This function returns the password for a given Roll Number"""
    cursor.execute(
        f"SELECT password FROM cadet_user WHERE roll_no = {roll_no}")
    password = cursor.fetchone()[0]

    return password


def Redirecting():
    """This function just prints redirecting on the screen"""
    print("\nRedirecting", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".")


def Input_Date():
    """This function inputs date and returns the date"""
    print("\nPlease do enter only integers for the date")

    while True:

        try:
            day_input = int(input("Enter the Day: "))
            month_input = int(input("Enter the Month: "))
            year_input = int(input("Enter the Year: "))

            the_date = datetime.date(year_input, month_input, day_input)

            return the_date

        except ValueError:
            print("\nYou have entered an invalid characters. Please Try Again")
            continue


def Check_Roll_No(roll_no):
    """This function checks whether the entered roll number
    exists in the data and returns True if matched"""
    roll_list = Get_Roll_No_List()

    if roll_no in roll_list:
        return True

    else:
        return False


def Get_Probable_Medicine(med_name):
    """This function return the probable list and table of medicines"""
    cursor.execute(
        f"SELECT medicine_name FROM medicine WHERE medicine_name like '%{med_name}%'")
    data = cursor.fetchall()

    med_list = []

    med_table = PrettyTable()
    med_table.field_names = ['Medicine Name']

    for med in data:
        med_table.add_row([med[0]])
        med_list.append(med[0])

    if len(med_list) == 0:
        return [], []

    else:
        return med_list, med_table


def Check_Expiry(med_name):
    """This function checks whether the given medicine in expired or not"""
    try:
        cursor.execute(
            f"SELECT expiry FROM medicine WHERE medicine_name = '{med_name}'")
        expiry_date = cursor.fetchone()[0]

        if expiry_date > datetime.date.today():
            return True

        else:
            return False

    except Error:
        return 'Error'


def Check_Quantity(med_name):
    """This function checks the quantity available to issue medicine"""
    cursor.execute(
        f"SELECT quantity FROM medicine WHERE medicine_name = '{med_name}'")
    aval_quantity = cursor.fetchone()[0]

    if aval_quantity > 0:
        return True

    else:
        return False


def Change_Medication_Status():
    """This function checks the end_date and updates the medical status of the cadet"""
    try:
        cursor.execute(
            "SELECT roll_no, timestamp, end_date, status FROM issue_medicine WHERE status = 'Under Medication'")
        data = cursor.fetchall()

        for roll_no, timestamp, end_date, status in data:
            if end_date < datetime.date.today():
                cursor.excecute(
                    f"UPDATE issue_medicine SET status = 'Healthy' WHERE roll_no = {roll_no} and timestamp = '{timestamp}'")
                conn.commit()

            else:
                pass

    except sqlerror:
        print("An Error Occurred while parsing and modifying the Status of the Cadet.")


def Scan_For_Expiry():
    """This function scans the entire medicines to check if any medicine expired"""
    expiry_table = PrettyTable()
    expiry_table.field_names = ['Medicine Name',
                                'Usage / Indication', 'Quantity', 'Expiry']
    expiry_list = []
    try:
        cursor.execute(f"SELECT medicine_name FROM medicine")
        data = cursor.fetchall()

        for medicine in data:
            check_value = Check_Expiry(medicine[0])

            if not check_value:
                cursor.execute(
                    f"SELECT * FROM medicine WHERE medicine_name = '{medicine[0]}'")
                name, usage, qty, exp = cursor.fetchone()
                expiry_list.append(name)
                expiry_table.add_row([name, usage, qty, exp])

            else:
                pass

        if len(expiry_list) == 0:
            return False, False

        else:
            return expiry_table, expiry_list

    except sqlerror:
        print("\nAn Error Occurred while scanning for expiry")


def Get_BMI_Status(bmi):
    """This function gets the bmi status based on the bmi value"""
    if bmi < 18.5 or bmi == 18.5:
        return 'Underweight'

    elif 18.5 < bmi < 24.9:
        return 'Healthy'

    elif 25 < bmi < 29.9:
        return 'Overweight'

    elif bmi > 30:
        return 'Obese'

    else:
        return "Can't Be Calculated"


def Update_BMI(roll_no):
    """This function updates BMI and BMI Status of a cadet"""
    try:
        import mysql.connector
        new = mysql.connector.connect(
            host='localhost', user='root', password='student', database='medic')
        new_cursor = new.cursor()
        new_cursor.execute(
            f"SELECT height, weight FROM medical_data WHERE roll_no = {roll_no}")
        height, weight = new_cursor.fetchone()

        if height and weight:
            height = height/100
            bmi = (weight / height**2)
            bmi = round(bmi, 2)
            bmi_status = Get_BMI_Status(bmi)

            new_cursor.execute(
                f"UPDATE medical_data SET BMI = {bmi}, BMI_status = '{bmi_status}' WHERE roll_no = {roll_no}")
            new.commit()
            return True

        else:
            return False

    except sqlerror:
        return False


def Input_Timing():
    """This function lets user to enter timing"""
    while True:
        hour_input = input("Enter the hour (24 Hour Format): ")
        minute_input = input("Enter the minutes: ")

        try:
            hour_input = int(hour_input)
            minute_input = int(minute_input)

            if 0 <= hour_input <= 23 and 0 <= minute_input <= 59:
                time = datetime.time(hour=hour_input, minute=minute_input)
                return time

            else:
                print("You input exceeded the limit. Please Try Again")
                sleep(1)
                continue

        except ValueError:
            print(
                "You have entered an invalid value for hours of minute. Please Try Again")
            sleep(1)
            continue


def Check_If_Admitted(roll_no):
    """This function checks whether a cadet is admitted or not"""
    try:
        cursor.execute(
            f"SELECT * FROM admission WHERE roll_no = {roll_no} and status = 'Admitted'")
        data = cursor.fetchone()

        if data is not None:
            print("\nYou can't Admit the Cadet. The cadet is already Admitted")
            print(f"Admitted Cause: {data[1]}")
            print(f"Admitted on: {data[3]}")
            print(f"Discharge Date: {data[2]}")
            return True

        else:
            return False

    except sqlerror:
        print("An Error Occurred while parsing data from the database. Please Try Again")
        sleep(1.5)


def Get_Latest_Timestamp(roll_no):
    """This function gets the latest admission timestamp of a cadet"""
    try:
        cursor.execute(
            f"SELECT timestamp FROM admission WHERE roll_no = {roll_no} and status = 'Admitted' ORDER BY timestamp DESC")
        timestamp = cursor.fetchall()[0][0]

        return timestamp

    except sqlerror:
        print("\nAn error occurred while getting admission data. Please Try Again")
        sleep(1.5)
        return False


def Calculate_Eye_Sight_Points():
    """This functions calculates the points for eye sight"""
    for house in house_list:
        cursor.execute(f"""SELECT medical_data.eye_l,medical_data.eye_r FROM medical_data,cadet 
                        WHERE cadet.house = '{house}' and cadet.roll_no = medical_data.roll_no""")
        data = cursor.fetchall()
        house_total = 0
        for eye_l, eye_r in data:
            if eye_l is None and eye_r is None:
                continue

            else:
                print("else is getting executed")
                eye_l = fabs(eye_l)
                eye_r = fabs(eye_r)
                eye_total = eye_l + eye_r
                house_total += eye_total

        else:
            cursor.execute(
                f"UPDATE fit_house SET eye_sight = {house_total} WHERE house = '{house}'")
            conn.commit()


def Calculate_BMI_Points():
    """This function calculates points based on BMI"""
    for house in house_list:
        cursor.execute(f"""SELECT medical_data.BMI FROM medical_data,cadet 
                        WHERE cadet.house = '{house}' and cadet.roll_no = medical_data.roll_no""")
        data = cursor.fetchall()
        house_bmi = 0
        for row in data:
            bmi = row[0]

            if bmi is None:
                continue

            else:
                house_bmi += bmi

        else:
            cursor.execute(
                f"UPDATE fit_house SET BMI = {house_bmi} WHERE house = '{house}'")
            conn.commit()


def Add_Admission_Points(roll_no):
    """This function adds points the the fit house table if a cadet is admitted"""
    cursor.execute(f"SELECT house FROM cadet WHERE roll_no = {roll_no}")
    house = cursor.fetchone()[0]

    cursor.execute(
        f"UPDATE fit_house SET admission = admission + 5 WHERE house = '{house}'")
    conn.commit()


def Calculate_Total_Points():
    """This function calculates the total points for the house"""
    for house in house_list:
        cursor.execute(
            f"UPDATE fit_house SET total_points = bmi + eye_sight + admission WHERE house = '{house}'")
        conn.commit()
