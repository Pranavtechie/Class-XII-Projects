import src
from time import sleep

conn, cursor, sqlerror = src.Establish_Connection() # Establishing connection to the database

def Height_Update(roll_no):
    """This function shows and updates the height of the cadet"""
    try:
        cursor.execute(f"SELECT height FROM medical_data WHERE roll_no = {roll_no}")
        present_height = cursor.fetchone()[0]

        if present_height is None:
            update_input = 'Y'

        else:
            print(f"\nYour Height according to the database is : {present_height}")
            update_input = input(f"Do you want to change your height (Y / N): ")

        if update_input in ['y','Y']:
                print("\nYou chose to update your height")
                print("Example : 156.20")
                new_height = input("Enter you height in centimeters: ")

                try:
                    new_height = float(new_height)
                    new_height = round(new_height,2)
                    cursor.execute(f"UPDATE medical_data SET height = {new_height}  WHERE roll_no = {roll_no}")
                    conn.commit()

                    value = src.Update_BMI(roll_no)

                    if value:
                        print("\nYour BMI is updated")
                        sleep(1.5)

                    else:
                        print("\nYour BMI is not updated check your Weight")
                        sleep(1.5)

                except ValueError:
                    print("\nYou have entered an Invalid value for the height. Please Try Again")
                    sleep(1.5)

        else:
            print("\nYou chose not to update your height")
            sleep(1.5)

    except sqlerror:
        pass


def Weight_Update(roll_no):
    """This function shows and updates the weight of the cadet"""
    try:
        cursor.execute(f"SELECT weight FROM medical_data WHERE roll_no = {roll_no}")
        present_weight = cursor.fetchone()[0]

        if present_weight is None:
            update_input = 'Y'

        else:
            print(f"\nYour Weight according to the database is : {present_weight}")
            update_input = input(f"Do you want to change your weight (Y / N): ")

        if update_input in ['y', 'Y']:
            print("\nYou chose to update your weight")
            print("Example : 66.20")
            new_weight = input("Enter you weight in kilograms: ")

            try:
                new_weight = float(new_weight)
                new_weight = round(new_weight, 2)
                cursor.execute(f"UPDATE medical_data SET weight = {new_weight} WHERE roll_no = {roll_no}")
                conn.commit()

                value = src.Update_BMI(roll_no)

                if value:
                    print("\nYour BMI is updated")
                    sleep(1.5)

                else:
                    print("\nYour BMI is not updated check your Height")
                    sleep(1.5)

            except ValueError:
                print("\nYou have entered an Invalid value for the weight. Please Try Again")
                sleep(1.5)

        else:
            print("\nYou chose not to update your weight")
            sleep(1.5)

    except sqlerror:
        pass


def Eye_Sight_Confirm(roll_no):
    """This function confirms whether a cadet is having eye sight or not"""

    try:
        cursor.execute(f"SELECT eye_l, eye_r FROM medical_data WHERE roll_no = {roll_no}")
        left, right = cursor.fetchone()

        if left and right is None:
            print("\nYou have not entered you Eye Sight till now.Please Update")
            sleep(1)
            Eye_Sight_Update(roll_no)

        else:
            print("Your Present Eye Sight")
            print(f"Left Eye : {left}")
            print(f"Right Eye: {right}\n")

            confirmation = input("Do you want to update your Eye Sight (Y / N): ")
            if confirmation  in ['y','Y']:
                Eye_Sight_Update(roll_no)

            else:
                print("\nYou chose not to update your eye sight")
                sleep(1.5)

    except sqlerror:
        print("\nAn error occurred while parsing the data from the database. Please Try Again")
        sleep(1.5)

def Eye_Sight_Update(roll_no):
    """This function updates eye sight of the cadet"""
    confirm_input = input("Do you have Eye Sight (Y / N): ")

    if confirm_input in ['y','Y']:
        print("\nExample: -1.25, ")
        print("If you have perfect vision for an Eye. Please Enter Zero\n")
        r_eye = input("Enter your Left Eye Sight: ")
        l_eye = input("Enter your Right Eye Sight: ")

        try:
            cursor.execute(f"UPDATE medical_data SET eye_r = {r_eye}, eye_l = {l_eye} WHERE roll_no = {roll_no}")
            conn.commit()

            print("\nYou have successfully updated your eye sight")
            sleep(1.5)

        except sqlerror:
            print("\nAn error occurred while sending the data to the database")
            sleep(1.5)

    else:
        print("\nYou don't have Eye Sight")
        sleep(1.5)


def BMI_Check(roll_no):
    """This function prints the cadet's BMI and other data"""
    print("\nYou chose to see your BMI")
    try:
        cursor.execute(f"""SELECT medical_data.roll_no, cadet.name, cadet.class, medical_data.height, medical_data.weight, 
                        medical_data.BMI, medical_data.BMI_status FROM medical_data, cadet
                        WHERE medical_data.roll_no = cadet.roll_no and cadet.roll_no = {roll_no}""")
        roll,name,clas, height, weight, bmi, bmi_status = cursor.fetchone()

        print(f"Roll Number: {roll_no}")
        print(f"Cadet Name: {name}")
        print(f"Class: {clas}")
        print(f"Cadet height: {height}")
        print(f"Cadet Weight: {weight}")
        print(f"Cadet BMI: {bmi}")
        print(f"Cadet BMI Status: {bmi_status}\n")
        sleep(2)


    except sqlerror:
        print("\nAn Error occurred while parsing the data. Please Try Again")
        sleep(1.5)



def Basic_Medical_Data_Main(roll_no):
    """This function prints the menu of the Updating of the Medical Data"""

    src.Cls()
    while True:
        print("\n-- Personal Medical Data --\n")
        print("Press (1) to update your height")
        print("Press (2) to update your weight")
        print("Press (3) to update your eye sight")
        print("Press (4) to check you Body Mass Index")
        print("Press (5) to go to Cadet Menu")
        print("Press (6) to exit the program\n")

        medical_dict = {'1' : Height_Update,
                        '2' : Weight_Update,
                        '3' : Eye_Sight_Confirm,
                        '4' : BMI_Check}

        medical_input = input("Enter your input from the available options: ")

        if medical_input in medical_dict:
            medical_dict[medical_input](roll_no)

        elif medical_input == '5':
            print("\nYou chose to go to Cadet Menu")
            sleep(1.5)
            break

        elif medical_input == '6':
            src.Exit()

        else:
            print("\nYou have entered an invalid input. Please Try Again")
            sleep(1.5)
            continue
