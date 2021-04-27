from the_exit import exit_program
from time import sleep
import explore as exp
from db_connect import est_conn
from mysql.connector import Error

conn, cursor = est_conn()

def complete_entry(input_list):
    l = input_list

    try:
        cursor.execute(f"""INSERT INTO phones VALUES ('{l[0]}','{l[1]}',{l[2]},'{l[3]}','{l[4]}','{l[5]}',{l[6]},
                        '{l[7]}','{l[8]}','{l[9]}','{l[10]}','{l[11]}','{l[12]}',{l[13]})""")
        conn.commit()

        cursor.execute(f"INSERT INTO phones_primary VALUES ('{l[0]}','{l[1]}',{l[2]},'{l[5]}','{l[7]}','{l[12]}','{l[11]}',{l[13]})")
        conn.commit()

        cursor.execute(f"INSERT INTO quantity VALUES ('{l[0]}','{l[1]}',{l[2]})")
        conn.commit()

        return True

    except Error:
        return False



def get_inputs(company, model):
    price = input("\nEnter the price (Value must be integer): ")
    processor = input("\nEnter the processor name: ")
    dimensions = input("\nEnter the dimensions (inches): ")
    battery = input("\nEnter the capacity of the battery (mAh): ")
    year = input("\nEnter the the year of release (4 - digits): ")
    camera = input("\nEnter the cameras: ")
    special = input("\nEnter the special features of the phones (ignore ','): ")
    good_for = input("\nEnter which area the phone is good: ")
    display_spec = input("\nEnter the display specifications: ")
    os = input("\nEnter the operating system name: ")
    ram = input("\nEnter the RAM Capacity of the phone (GigaBytes): ")
    storage = input("\nEnter the Storage Capacity of the phones (GigaBytes): ")
    quantity = int(input("\nEnter the quantity of the phone: "))

    spec_list =  [company, model, price, processor, dimensions, battery, year, camera, special, good_for,
                  display_spec, os, ram, storage,quantity]

    return spec_list

def get_models():
    cursor.execute("SELECT model from phones")
    model_data = cursor.fetchall()

    models_lower = []
    models = []

    for row in model_data:
        models_lower += row[0].lower()
        models += row[0]

    return models, models_lower


def main_add():
    print("\nYou chose to add new phone")

    company_input = input("\nEnter the name of the company: ")

    if company_input in exp.companies or company_input in exp.companies_lower:
        model_input = input("\nEnter the name of the model: ")
        models, models_lower = get_models()

        if model_input in models or model_input in models_lower:
            print("\nThe entered model name exists.")
            sleep(1)

        else:
            inputs_list = get_inputs(company_input, model_input)

            check_value = complete_entry(inputs_list)

            if check_value:
                print("\nYou have successfully entered the new phone")
                sleep(1)

            else:
                print("\nIt looks like there is problem with the data try again.")
                sleep(1)

    else:
        print("\nYou have entered an invalid company name please try again")
        sleep(1.5)


