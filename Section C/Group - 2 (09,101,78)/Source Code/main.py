import mysql.connector as sq
from prettytable import PrettyTable
from mysql.connector import Error as sqlerror

heading = """<<<<<<<<<<<<<<<<<<<<<       CRICKET KNOWLEDGE    >>>>>>>>>>>>>>>>>>>>>>
....................      SAINIK SCHOOL KALIKIRI   ...............
---------------  BY : Vinay , Tanish , Bhargav  ------------------"""
fields = ['Player Name', 'Country', 'Rating']


def individual_profile():
    conn = sq.connect(host="localhost", user='root',
                      password='student', database='cric_db')
    cursor = conn.cursor()

    name_input = input("Enter the name of the player: ")

    if name_input != '':
        cursor.execute(
            f"SELECT * FROM batsmen WHERE name like  '%{name_input}%'")
        player_data = cursor.fetchone()

        conn.close()

        player_table = PrettyTable()
        player_table.field_names = fields
        player_table.add_row([player_data[0], player_data[1], player_data[2]])

        print(f"\n{player_table}\n")

    else:
        print("You have not entered any value")
        conn.close()


def view_table():
    conn = sq.connect(host="localhost", user='root',
                      password='student', database='cric_db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM batsmen ORDER BY rating desc")
    data = cursor.fetchall()

    conn.close()

    players_table = PrettyTable()
    players_table.field_names = ['Rank'] + fields

    for i in range(len(data)):
        name, country, rating = data[i][0], data[i][1], data[i][2]
        players_table.add_row([i + 1, name, country, rating])

    print(f"\n\n{players_table}\n\n")


def add_player():
    conn = sq.connect(host="localhost", user='root',
                      password='student', database='cric_db')
    cursor = conn.cursor()

    name_input = input("Enter the name of the player you want to add: ")

    if name_input != '':
        cursor.execute(
            f"SELECT name FROM batsmen WHERE name LIKE '%{name_input}%'")
        data = cursor.fetchall()

        if not data:
            print(
                f"No record with the name {name_input} exists you can proceed to add the record to the database")
            country = input(f"Enter the country of {name_input}: ")
            rating = input(f"Enter the rating of {name_input}")

            try:
                cursor.execute(
                    f"INSERT INTO batsmen VALUES ('{name_input}', '{country}',{rating})")
                conn.commit()
                print(
                    f"\nYou have successfully added the {name_input}'s record to the database")

            except sqlerror:
                print(
                    f"\nAn Error Occurred while adding {name_input}'s record. Please try Again\n")

        else:
            print(
                f"\nThere exists a record with the name of {name_input}. Please view the {name_input}'s record using option (1)")

        conn.close()

    else:
        print("You have not entered any player value")
        conn.close()


def edit_player():
    conn = sq.connect(host="localhost", user='root',
                      password='student', database='cric_db')
    cursor = conn.cursor()

    name_input = input("Enter the name of the player: ")

    if name_input != '':

        cursor.execute(
            f"SELECT * FROM batsmen WHERE name like  '%{name_input}%'")
        player_data = cursor.fetchone()

        player_table = PrettyTable()
        player_table.field_names = fields
        player_table.add_row([player_data[0], player_data[1], player_data[2]])

        print(f"\n{player_table}\n")

        new_name = input(f"Enter the new name for {player_data[0]}: ")
        new_country = input(f"Enter the new country for {new_name}: ")
        new_rating = input(f"Enter the new rating for {new_name}: ")

        try:
            new_rating = int(new_rating)

            try:
                confirm_input = input(
                    f"Do you want to update {player_data[0]} with the provided data.")

                if confirm_input in ['Y', 'y']:
                    cursor.execute(
                        f"UPDATE batsmen SET name = '{new_name}', country = '{new_country}', rating = {new_rating} WHERE name = '{player_data[0]}'")

                else:
                    print(
                        f"\nYou chose not to update {player_data[0]}'s records")

            except sqlerror:
                print(
                    f"\nAn error occurred while updating the {player_data[0]}. Please try Again")

        except ValueError:
            print(
                f"\n You have entered an invalid value for {player_data[0]}'s rating.Please try again")

        conn.close()

    else:
        print("You have not entered the player value")
        conn.close()


def delete_player():
    conn = sq.connect(host="localhost", user='root',
                      password='student', database='cric_db')
    cursor = conn.cursor()

    name_input = input("Enter the name of the player you want to delete: ")

    if name_input != '':

        cursor.execute(
            f"SELECT * FROM batsmen WHERE name like  '%{name_input}%'")
        player_data = cursor.fetchone()

        player_table = PrettyTable()
        player_table.field_names = fields
        player_table.add_row([player_data[0], player_data[1], player_data[2]])

        print(f"\n{player_table}\n")

        confirm_input = input(
            f"Are you sure you want to delete {player_data[0]} from the database (Y/ N): ")

        if confirm_input in ['Y', 'y']:
            try:
                cursor.execute(
                    f"DELETE FROM batsmen WHERE name = '{player_data[0]}'")
                conn.commit()
                print(
                    f"\nYou have successfully deleted {player_data[0]} from the database\n")

            except sqlerror:
                print(
                    f"\nAn error occurred while deleting {player_data[0]} record. Please Try Again")

        else:
            print(f"\n You chose not to delete {player_data[0]} record\n")

        conn.close()

    else:
        print("You have not entered the player value")
        conn.close()


def exit_program():
    print("You chose to exit the program")
    exit()


def main():
    while True:
        print("\nPress (1) to check the individual player profile")
        print("Press (2) to view the table")
        print("Press (3) to add a player profile")
        print("Press (4) to edit a player profile")
        print("Press (5) to delete a player")
        print("Press (6) to exit the program\n\n")

        func_dict = {'1': individual_profile,
                     '2': view_table,
                     '3': add_player,
                     '4': edit_player,
                     '5': delete_player,
                     '6': exit_program}

        user_input = input("Enter your input here: ")

        if user_input in func_dict.keys():
            func_dict[user_input]()

        else:
            print("\nYou have given an invalid input please try again\n")
            continue


if __name__ == "__main__":
    print(heading)
    main()
