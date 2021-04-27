import mysql.connector as sq
from prettytable import PrettyTable


def exit_program():
    print("\nThank you for using our program")
    print("Have a nice day")
    exit()


def print_cars_table():
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='garage')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM cars")
    data = cursor.fetchall()
    conn.close()

    cars_table = PrettyTable()
    cars_table.field_names = ['Company', 'Name',
                              'Cost', 'Tank Capacity', 'Engine Type']

    for company, name, cost, tank, engine in data:
        cars_table.add_row([company, name, cost, tank, engine])

    print(cars_table)


def print_bikes_table():
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='garage')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM bikes")
    data = cursor.fetchall()
    conn.close()

    bikes_table = PrettyTable()
    bikes_table.field_names = ['Company', 'Name',
                               'Cost', 'Tank Capacity', 'Engine Type']

    for company, name, cost, tank, engine in data:
        bikes_table.add_row([company, name, cost, tank, engine])

    print(bikes_table)


def check_existence(vehicle, company, model):
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='garage')
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT * FROM {vehicle} WHERE company = '{company}' and name = '{model}'")
    data = cursor.fetchone()
    conn.close()

    if data is None:
        return None

    else:
        return data


def update_cars_main():
    print("\n--- UPDATE CAR ---\n")
    company_table, company_list = return_company_table_and_list('cars')
    print(f"\n{company_table}")
    company_input = input("Enter the company name : ")
    if company_input.upper() in company_list:
        model_table, model_list = return_name_table_and_list(
            'cars', company_input)
        print(f"\n{model_table}")
        model_input = input(f"Enter the model from the above table : ")

        if model_input.upper() in model_list:
            old_table = get_old_values('cars', company_input, model_input)
            print(f"\n{old_table}\n")
            new_company_name = input(f"Enter the new company name : ")
            new_model_name = input(f"Enter the new model name : ")
            new_cost = input("Enter the new cost : ")
            new_tank_capacity = input("Enter the new tank capacity : ")
            new_engine_type = input("Enter the new engine type : ")

            confirm_input = input(
                "Are you sure you want to update the data (Y / N) : ")
            if confirm_input in ['Y', 'y']:
                conn = sq.connect(host='localhost', user='root',
                                  password='student', database='garage')
                cursor = conn.cursor()
                cursor.execute(
                    f"UPDATE cars SET company = '{new_company_name}', name = '{new_model_name}', cost = '{new_cost}', tank_capacity = '{new_tank_capacity}', engine_type = '{new_engine_type}' WHERE company =  '{company_input}' and name = '{model_input}'")
                conn.commit()

                print(f"\nYou have successfully updated the data")

            else:
                print(f"You chose not to update the <{model_input}>")
                return None
        else:
            print(
                f"<{model_input} is an invalid model name for {company_input}. Please Try Again>")
            return None

    else:
        print(f"<{company_input}> is an invalid input. Please Try Again")
        return None


def update_bikes_main():
    print("\n--- UPDATE BIKE ---\n")
    company_table, company_list = return_company_table_and_list('bikes')
    print(f"\n{company_table}")
    company_input = input("Enter the company name : ")
    if company_input.upper() in company_list:
        model_table, model_list = return_name_table_and_list(
            'cars', company_input)
        print(f"\n{model_table}")
        model_input = input(f"Enter the model from the above table : ")

        if model_input.upper() in model_list:
            old_table = get_old_values('bikes', company_input, model_input)
            print(f"\n{old_table}\n")
            new_company_name = input(f"Enter the new company name : ")
            new_model_name = input(f"Enter the new model name : ")
            new_cost = input("Enter the new cost : ")
            new_tank_capacity = input("Enter the new tank capacity : ")
            new_engine_type = input("Enter the new engine type : ")

            confirm_input = input(
                "Are you sure you want to update the data (Y / N) : ")
            if confirm_input in ['Y', 'y']:
                conn = sq.connect(host='localhost', user='root',
                                  password='student', database='garage')
                cursor = conn.cursor()
                cursor.execute(
                    f"""UPDATE bikes SET company = '{new_company_name}' name = '{new_model_name}' cost = '{new_cost}' tank_capacity = '{new_tank_capacity}' engine_type = '{new_engine_type}' WHERE company =  '{company_input}' and name = '{model_input}'""")
                conn.commit()

                print(f"\nYou have successfully updated the data")

            else:
                print(f"You chose not to update the <{model_input}>")
                return None
        else:
            print(
                f"<{model_input} is an invalid model name for {company_input}. Please Try Again>")
            return None

    else:
        print(f"<{company_input}> is an invalid input. Please Try Again")
        return None


def add_car_main():
    print("\n--- ADD CAR ---\n")
    company_input = input("Enter the company name : ")
    model_input = input("Enter the model name : ")
    check = check_existence('cars', company_input, model_input)

    if not check:
        cost_input = input("Enter the cost : ")
        tank_input = input("Enter the tank capacity : ")
        engine_type_input = input("Enter the type of the engine : ")

        confirm_input = input(
            "Are you sure you want to add the new car (Y / N) : ")
        if confirm_input in ['Y', 'y']:
            conn = sq.connect(host='localhost', user='root',
                              password='student', database='garage')
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO cars VALUES ('{company_input}','{model_input}','{cost_input}','{tank_input}','{engine_type_input}')")
            conn.commit()

            print(f"\nYou have successfully addedd a new car")

        else:
            print("\nYou chose to cancel the addition of new car to the database")
            return None

    else:
        print(f"The entered model of car already exists. Try updating the data")


def add_bike_main():
    print("\n--- ADD BIKE ---\n")
    company_input = input("Enter the company name : ")
    model_input = input("Enter the model name : ")
    check = check_existence('bikes', company_input, model_input)

    if not check:
        cost_input = input("Enter the cost : ")
        tank_input = input("Enter the tank capacity : ")
        engine_type_input = input("Enter the type of the engine : ")

        confirm_input = input(
            "Are you sure you want to add the new car (Y / N) : ")
        if confirm_input in ['Y', 'y']:
            conn = sq.connect(host='localhost', user='root',
                              password='student', database='garage')
            cursor = conn.cursor()

            cursor.execute(
                f"INSERT INTO bikes VALUES ('{company_input}','{model_input}','{cost_input}','{tank_input}','{engine_type_input}')")
            conn.commit()

            print(f"\nYou have successfully addedd a new car")

        else:
            print("\nYou chose to cancel the addition of new bike to the database")
            return None

    else:
        print(f"The entered model of bike already exists. Try updating the data")


def delete_car_main():
    print("\n--- DELETE CAR ---\n")
    company_table, company_list = return_company_table_and_list('cars')
    print(f"\n{company_table}")
    company_input = input("Enter the company name : ")
    if company_input.upper() in company_list:
        model_table, model_list = return_name_table_and_list(
            'cars', company_input)
        print(f"\n{model_table}")
        model_input = input(f"Enter the model from the above table : ")

        if model_input.upper() in model_list:
            confirm_input = input(
                f"Are you sure you want to delete <{model_input}> (Y / N) :")
            if confirm_input in ['Y', 'y']:
                conn = sq.connect(host='localhost', user='root',
                                  password='student', database='garage')
                cursor = conn.cursor()
                cursor.execute(
                    f"DELETE FROM cars WHERE company = '{company_input}' and name = '{model_input}'")
                conn.commit()

                print(f"\nYou have succssfully deleted the car")

            else:
                print(f"You chose to cancel the deletion of <{model_input}>")
                return None
        else:
            print(f"<{model_input}> is an invalid model name. Please Try Again")
            return None
    else:
        print(f"<{company_input}> is an invalid company. Please Try Again")
        return None


def delete_bike_main():
    print("\n--- DELETE BIKE ---\n")
    company_table, company_list = return_company_table_and_list('bikes')
    print(f"\n{company_table}")
    company_input = input("Enter the company name : ")
    if company_input.upper() in company_list:
        model_table, model_list = return_name_table_and_list(
            'bikes', company_input)
        print(f"\n{model_table}")
        model_input = input(f"Enter the model from the above table : ")

        if model_input.upper() in model_list:
            confirm_input = input(
                f"Are you sure you want to delete <{model_input}> (Y / N) :")
            if confirm_input in ['Y', 'y']:
                conn = sq.connect(host='localhost', user='root',
                                  password='student', database='garage')
                cursor = conn.cursor()
                cursor.execute(
                    f"DELETE FROM bikes WHERE company = '{company_input}' and name = '{model_input}'")
                conn.commit()

                print(f"\nYou have succssfully deleted the car")
            else:
                print(f"You chose to cancel the deletion of <{model_input}>")
                return None
        else:
            print(f"<{model_input}> is an invalid model name. Please Try Again")
            return None
    else:
        print(f"<{company_input}> is an invalid company. Please Try Again")
        return None


def return_company_table_and_list(type):
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='garage')
    cursor = conn.cursor()

    cursor.execute(f"SELECT distinct(company) FROM {type} ORDER BY company")
    company_data = cursor.fetchall()
    conn.close()

    company_list = []
    company_table = PrettyTable()
    company_table.field_names = ['Company Name']

    for company in company_data:
        company = company[0]
        company_table.add_row([company])
        company_list.append(company)

    return company_table, company_list


def return_name_table_and_list(type, company):
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='garage')
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT name FROM {type} WHERE company = '{company}' ORDER BY name ")
    name_data = cursor.fetchall()
    conn.close()
    name_list = []
    name_table = PrettyTable()
    name_table.field_names = ['Model Name']
    for row in name_data:
        row = row[0]
        name_list.append(row)
        name_table.add_row([row])

    return name_table, name_list


def get_old_values(vehicle, company, model):
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='garage')
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM {vehicle} WHERE company = '{company}' and name = '{model}'")
    list = cursor.fetchone()
    conn.close()

    table = PrettyTable()
    table.field_names = ['Company', 'Name',
                         'Cost', 'Tank Capacity', 'Engine Type']
    table.add_row(list)

    return table
