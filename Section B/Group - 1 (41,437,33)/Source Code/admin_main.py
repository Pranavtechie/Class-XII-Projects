from db_connect import est_conn
from prettytable import PrettyTable
from the_exit import exit_program
from time import sleep
from add_phones import main_add
from manage_qty import main_qty

conn, cursor = est_conn()

def get_customer_requests_table():
    cursor.execute("SELECT * FROM customer_request")
    requests = cursor.fetchall()

    request_table = PrettyTable()
    request_table.field_names = ['Serial No', 'Name', 'Company', 'Model']
    for serial, name, company, model in requests:
        request_table.add_row([serial, name, company, model])

    return request_table

def get_requests():
    print("\nYou chose to see the customer requests\n")

    request_table = get_customer_requests_table()
    print(request_table)


def delete_request_entry():
    print("\nYou chose to delete an entry\n")

    request_table = get_customer_requests_table()
    print(request_table, '\n')

    serial_input = input("Enter the serial no to delete the request: ")

    try:
        serial_input = int(serial_input)

        cursor.execute("SELECT request_id FROM customer_request")
        serial_data = cursor.fetchall()
        serial_list = []

        for no in serial_data:
            serial_list += no[0]

        if serial_input in serial_list:
            confirm = input("Please Confirm before deleting (Y / N): ")

            if confirm in ['y','Y']:
                cursor.execute(f"DELETE FROM customer_request WHERE request_id = {serial_input}")
                conn.commit()

                print("The request entry is deleted successfully")
                sleep(1)

            else:
                print("\nYou chose not to delete the request entry\n")
                sleep(1)

        else:
            print("The entered value does not exists. Please try again")
            sleep(1)

    except ValueError:
        print("\nYou have entered an invalid value please try again")
        sleep(1)


def clear_requests():
    print("\nYou chose to clear the requests_table")

    confirm = input("Confirm to clear the request table(Y / N): ")

    if confirm in ['y','Y']:
        cursor.execute("DELETE FROM customer_request")
        conn.commit()

        print("\nYou have successfully cleared the request table")
        sleep(1)

    else:
        print("\nYou chose not to clear the request_table")
        sleep(1)



def customer_requests():

    while True:
        print("\n----------- Customer Requests -----------\n")
        print("Press (1) to see the customer requests")
        print("Press (2) to delete an entry")
        print("Press (3) to clear the customer requests")
        print("Press (4) to go to the admin menu")
        print("Press (5) to exit the program\n")

        request_dict = {'1' : get_requests, '2' : delete_request_entry, '3' : clear_requests, '5' : exit_program}

        admin_input = input("Enter an valid input from the above options: ")

        if admin_input in request_dict:
            request_dict[admin_input]()

        elif admin_input == '4':
            print("\nYou chose to go the admin menu")
            sleep(1)
            break

        else:
            print("\nYou have entered an invalid input, Please try again")
            sleep(1)
            continue


def clear_customer_logs():
    print("\nYou chose to delete the customer logs")

    confirm = input("Please confirm that you want to delete the logs (Y / N): ")

    if confirm in ['y','Y']:
        cursor.execute("SELECT COUNT(*) FROM customer_users")
        rows = cursor.fetchone()[0]

        cursor.execute("DELETE FROM customer_users")
        conn.commit()

        print(f"\nSuccessfully deleted {rows} logs")

    else:
        print("\nYou chose to abort the deletion of the logs")
        sleep(1)


def see_customer_logs():
    cursor.execute("SELECT * FROM customer_users")
    customer_data = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['Customer Name', 'Time Stamp']
    for name, time in customer_data:
        table.add_row([name, time])

    print(table)
    sleep(1)


def customer_logs():

    while True:
        print("\n--------- Customer Logs ---------\n")
        print("Press (1) to see the logs")
        print("Press (2) to clear the logs")
        print("Press (3) to go to admin menu")
        print("Press (4) to exit the program\n")

        log_dict = {'1' : see_customer_logs, '2' : clear_customer_logs, '4' : exit_program }

        admin_input = input("Enter a valid input from the above options: ")

        if admin_input in log_dict:
            log_dict[admin_input]()

        elif admin_input == '3':
            print("\nYou chose to go to admin menu")
            sleep(1)
            break

        else:
            print("\nYou have entered an invalid input. Please try again")
            sleep(1)
            continue


def admin_menu():
    while True:
        print("\n---------- Admin Menu ----------\n")
        print("Press (1) to see the customer logs")
        print("Press (2) to see the requests from customer")
        print("Press (3) to add a new phone")
        print("Press (4) to manage the stock")
        print("Press (5) to go to the main menu")
        print("Press (6) to exit the Program\n")

        check_dict = {'1' : customer_logs,'2': customer_requests,'3' : main_add,'4' : main_qty, '6' : exit_program}

        get_input = input("\nEnter a valid input from the above options: ")

        if get_input in check_dict:
            check_dict[get_input]()

        elif get_input == '5':
            print("\nYou chose to go to the main menu")
            sleep(1)
            break

        else:
            print("You have entered an invalid option, please try again.")
            sleep(1)
            continue
