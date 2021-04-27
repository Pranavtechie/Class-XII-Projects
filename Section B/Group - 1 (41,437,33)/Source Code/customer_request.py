from db_connect import est_conn
from time import sleep
from the_exit import exit_program
import explore

conn, cursor = est_conn()

def request_phone():
    name_input = input("Enter you name before you request a phone: ")

    print("Note: You can only request a phone from the existing companies.\n")

    company_table = explore.make_company_table()
    print(company_table)
    print("\nNote: You can only request a phone from the existing companies.\n")
    sleep(1.5)
    company_input = input("Enter the company name to request a new phone: ")

    if company_input in explore.companies_lower:
        model_input = input("Enter the name of the model you want to request: ")

        model_list , table = explore.get_single_primary_list_table('model',company_input)

        if model_input not in model_list:

            cursor.execute(f"INSERT INTO customer_request ('{name_input}', '{company_input}', '{model_input}') VALUES (name, company, model)")
            conn.commit()

            print("\nYour request will brought the the owners notice. Your request will be processed soon.\n")

        else:
            print("\nThe model you want to request already exists.\n")
            print(table)
            sleep(2)


    else:
        print("You have entered an invalid company name. Please try again.")
        sleep(2)

def request_restock():
    pass


def request_menu():
    while True:

        print("\n------------ Request Menu ------------")
        print("Press (1) to request a new phone")
        print("Press (2) to request restock of a specific phone")
        print("Press (3) to go to customer menu")
        print("Press (4) to exit the program")

        check_dict = {'1' : request_phone, '2' : request_restock, '4' : exit_program}

        user_input = input("Enter your input from the above options: ")

        if user_input in check_dict:
            check_dict[user_input]()

        elif user_input == '3':
            print("\nYou chose to go the customer menu")
            sleep(2)
            break

        else:
            print("\nYou have entered an invalid input. Please try again")
            sleep(1.5)
            continue