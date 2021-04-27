from db_connect import est_conn
from prettytable import PrettyTable
from time import sleep
from the_exit import exit_program

conn, cursor = est_conn()
primary_field_names = ['Company','Model','Price','Battery','Camera','RAM','OS','Storage']
companies_lower = ['samsung','apple', 'vivo', 'oneplus', 'redmi', 'realme']
companies = ['Samsung','Apple','Vivo','OnePlus','Redmi','Realme']

def get_detail_table(model_input):
    cursor.execute(f"SELECT * FROM phones WHERE model = '{model_input}'")
    m_d = cursor.fetchone()
    labels = ['Company', 'Model', 'Price', 'Processor', 'Dimensions', 'Battery', 'Year', 'Camera', 'Speciality',
              'Good For',
              'Display', 'Operating System', 'RAM', 'Storage']
    data_list = [m_d[0], m_d[1], m_d[2], m_d[3], m_d[4], m_d[5], m_d[6], m_d[7], m_d[8], m_d[9], m_d[10], m_d[11],
                 m_d[12], m_d[13]]
    detail_table = PrettyTable()
    detail_table.add_column('Labels', labels)
    detail_table.add_column('Information', data_list)

    return detail_table


def make_company_table():
    company_table = PrettyTable()
    company_table.field_names = ['Available Companies']
    for row in companies:
        company_table.add_row([row])

    return company_table


def get_single_primary_list_table(column,company):

    cursor.execute(f"SELECT {column} FROM phones WHERE company = '{company}'")
    data = cursor.fetchall()
    show_list = []
    show_table = PrettyTable()
    show_table.field_names = ['Model Names']

    for row in data:
        show_table.add_row([row[0]])
        show_list += row

    return show_list, show_table


def single_list_table(data, column_name):

    show_list = []
    show_table = PrettyTable()
    show_table.field_names = [column_name]

    for row in data:
        show_table.add_row([row[0]])
        show_list += row

    return show_list, show_table


def make_primary_table(data):
    show_table = PrettyTable()
    show_table.field_names = primary_field_names

    for com,m,p,b,ca,r,s,o in data:
        show_table.add_row([com,m,p,b,ca,r,s,o])

    return show_table

def phone_details():

    company_table = make_company_table()
    print(company_table)
    sleep(2)

    company_input = input("\nEnter the company name from the available options: ")

    model_list,model_table = get_single_primary_list_table('model',company_input)
    print(model_table)
    sleep(2)
    print("\nNote: Enter the name as in the above list")
    model_input = input("\nEnter the model name from the available options: ")

    if model_input in model_list:

        detail_table = get_detail_table(model_input)

        print(detail_table)
        sleep(2)

    else:
        print("\nThe entered model name does not exists. Try again")
        sleep(2)


def all_phones():

    cursor.execute('SELECT * FROM phones_primary')
    data = cursor.fetchall()
    table = make_primary_table(data)

    print(table,'\n')
    sleep(5)


def company_phones():
    first_table = make_company_table()
    print(first_table)
    sleep(3)

    company_input = input("\nEnter the company name to view it's phones: ")

    if company_input.lower() in companies_lower:

        cursor.execute(f"SELECT * FROM phones_primary WHERE company = '{company_input}'")
        data = cursor.fetchall()

        table = make_primary_table(data)

        print(table)
        print('\n')
        sleep(5)

    else:
        print("The entered company name does not exists.Please try again\n")
        sleep(3)



def year_phones():
    cursor.execute("SELECT DISTINCT(year) FROM phones ORDER BY year DESC")
    year_data = cursor.fetchall()

    year_list, year_table = single_list_table(year_data, 'Year of Release')

    print(year_table)
    sleep(3)
    print("\nNote: Enter the year as in the table.\n")
    year_input = input('Please enter an year for the available options: ')

    try:
        int(year_input)
        year_input = int(year_input)

        if year_input in year_list:
            cursor.execute(f"SELECT company,model,price,battery,camera,ram,storage,os FROM phones WHERE year = {year_input}")
            data = cursor.fetchall()

            table = make_primary_table(data)

            print(table)
            sleep(5)

        else:
            print("\nEnter a valid year the entered year does not exists")
            sleep(3)


    except ValueError:
        print("\nThe entered data does not contain numbers. Try Again")
        sleep(3)


def os_phones():
    cursor.execute("SELECT distinct(os) FROM phones ORDER BY os")
    os_data = cursor.fetchall()

    os_list, os_table = single_list_table(os_data, 'Operating System')

    print(os_table)
    sleep(3)
    print("\nEnter the name of the OS as in the above list\n")
    os_input = input("Enter the name of the operating system for the available options: ")

    if os_input in os_list:
        cursor.execute(f"SELECT * FROM phones_primary WHERE os = '{os_input}' ORDER BY os")
        aval_data = cursor.fetchall()

        aval_table = make_primary_table(aval_data)

        print(aval_table)
        sleep(5)

    else:
        print("\nThe entered operating system does not exists try again\n")
        sleep(3)


def explore():

    while True:
        print("\nYou can explore all kinds of mobiles here\n")
        print("Press (1) to see all the mobile phones available")
        print("Press (2) to see all the details of a phone")
        print("Press (3) to see all the phones based on company name")
        print("Press (4) to see all the phones based on the year of release")
        print("Press (5) to see all the phones based on the operation system")
        print("Press (6) to go to the customer menu")
        print("Press (7) to exit the program\n")

        user_input = input("Enter your input from the above options: ")

        explore_dict = {'1' : all_phones, '2': phone_details, '3' : company_phones, '4' : year_phones, '5' : os_phones,
                        '7' : exit_program}

        if user_input in explore_dict:
            explore_dict[user_input]()

        elif user_input == '6':
            print('\nYou chose to go the customer menu\n')
            break

        else:
            print("\nYou have entered an invalid input please try again\n")
            sleep(3)
