from time import sleep
from the_exit import exit_program
from db_connect import est_conn
from prettytable import PrettyTable
import explore as exp

cursor, conn = est_conn()

def add_qty():
    print("\nYou chose to restock phones")

    company_table = exp.make_company_table()
    print(company_table)

    company_input = input("\nEnter the company name: ")

    if company_input in exp.companies or company_input in exp.companies_lower:
        model_list ,model_table = exp.get_single_primary_list_table('model',company_input)
        model_input = input("\nEnter the model name: ")

        if model_input in model_list:
            quantity_input = int(input("Enter the quantity you want to restock: "))

            cursor.execute(f"UPDATE quantity set quantity = quantity + {quantity_input} WHERE model = '{model_input}'")
            conn.commit()

        else:
            print("\nYou have entered an invalid model name, Please try again")
            sleep(1)

    else:
        print("\nYou have entered an invalid company name, Please try again")
        sleep(1)





def show_qty_table():
    qty_table = PrettyTable()
    qty_table.field_names = ['Company','Model','Quantity']

    cursor.execute("SELECT * FROM quantity")
    qty_data = cursor.fetchall()

    for company, model, qty in qty_data:
        qty_table.add_row([company, model, qty])

    print('\n')
    print(qty_table,'\n')


def main_qty():
    while True:
        print("\nYou choose to manage the quantity\n")
        print("Press (1) to add quantity to a phone")
        print("Press (2) to see the quantity table")
        print("Press (3) to go the admin menu")
        print("Press (4) to exit the program\n")

        qty_dict = {'1': add_qty, '2' : show_qty_table, '4' : exit_program}

        qty_input = input("Enter a valid input from the available options: ")

        if qty_input in qty_dict:
            qty_dict[qty_input]()

        elif qty_input == '3':
            print("\nYou chose to go to the admin menu")
            sleep(1)
            break

        else:
            print("\nYou have entered an invalid input.Please try again")
            sleep(1)
