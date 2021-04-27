import mysql.connector as sq
from prettytable import PrettyTable

formats_list = ['TEST', 'ODI', 'T20']
player_type_list = ['BATSMEN', 'BOWLERS']
type_dict = {'1': 'batsmen',
             '2': 'bowlers'}
format_dict = {
    '1': 'test',
    '2': 'odi',
    '3': 't20'
}
batsmen_orderby = ['Matches Played', 'Runs Scored', 'Strike Rate',
                   'Average', 'Half Centuries', 'Centuries', 'Highest Score']
bowlers_orderby = ['Matches Played', 'Wickets Taken',
                   'Economy', '5 Wickets In A Match']
batsmen_orderby_dict = {
    '1': 'matchesPlayed',
    '2': 'runsScored',
    '3': 'strikeRate',
    '4': 'average',
    '5': 'halfCenturies',
    '6': 'centuries',
    '7': 'highestScore'}
bowlers_orderby_dict = {
    '1': 'matchesPlayed',
    '2': 'wicketsTaken',
    '3': 'economy',
    '4': '5wicketsInAMatch'}
order_type_dict = {
    '1': '',
    '2': 'desc'}
batsmen_fields = ['Name', 'DOB', 'Matches Played', 'Runs Scored', 'Strike Rate',
                  'Average', 'Half Centuries', 'Centuries', 'Highest Score']
bowlers_fields = ['Name', 'DOB', 'Matches Played', 'Wickets Taken',
                  'Economy', '5 Wickets In A Match']


def exit_program():
    """Exits the program when called"""
    print("Thank you for using our program")
    exit()


def establish_connection():
    """Establishes connection the the mysql database"""
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='cricket')
    cursor = conn.cursor()

    return conn, cursor


def print_format_type():
    """Prints the format types to choose option"""
    print(f"--- FORMAT TYPE ---")
    for i in range(len(formats_list)):
        print(f'Press ({i + 1}) for', formats_list[i])
    print()
    return None


def print_player_type():
    """Prints the player types to choose an option"""
    print(f"--- PLAYER TYPE ---")
    for i in range(len(player_type_list)):
        print(f'Press ({i + 1}) for', player_type_list[i])
    print()
    return None


def get_order_based_on(player_type):
    """Prints the order types to choose an option"""
    if player_type == 'batsmen':
        """The order type is bowler"""
        while True:
            print(f"--- Order Value ---")
            for i in range(len(batsmen_orderby)):
                print(f"Press ({i + 1}) to order by {batsmen_orderby[i]}")
            print()
            order_value_input = input("Enter the desired order number : ")
            if order_value_input in batsmen_orderby_dict:
                order_value = batsmen_orderby_dict[order_value_input]
                while True:
                    print("-- Order Type")
                    print("Press (1) for ascending order")
                    print("Press (2) for descending order")
                    order_type_input = input("Enter the desired number : ")
                    if order_type_input in order_type_dict:
                        order_type = order_type_dict[order_type_input]
                        return order_value, order_type
                    else:
                        print(
                            f"<{order_type_input}> is an invalid input. Please Try Again")
                        continue
            else:
                print(
                    f"<{order_value_input}> in an invalid order input. Please Try Again")
                continue

    elif player_type == 'bowlers':
        """The order type is bowlers"""
        while True:
            print(f"--- Order Value ---")
            for i in range(len(bowlers_orderby)):
                print(f"Press ({i + 1}) to order by {bowlers_orderby[i]}")
            print()
            order_value_input = input("Enter the desired order number : ")
            if order_value_input in bowlers_orderby_dict:
                order_value = bowlers_orderby_dict[order_value_input]
                while True:
                    print("-- Order Type")
                    print("Press (1) for ascending order")
                    print("Press (2) for descending order")
                    order_type_input = input("Enter the desired number : ")
                    if order_type_input in order_type_dict:
                        order_type = order_type_dict[order_type_input]
                        return order_value, order_type
                    else:
                        print(
                            f"<{order_type_input}> is an invalid input. Please Try Again")
                        continue
            else:
                print(
                    f"<{order_value_input}> in an invalid order input. Please Try Again")
                continue
    else:
        return None, None


def get_format_and_type():
    """Prints the format and type to get options"""
    while True:
        print_format_type()
        format_input = input("Enter the format type : ")

        if format_input in format_dict:
            return_format = format_dict[format_input]
            print()
            while True:
                print_player_type()
                type_input = input("Enter the player type : ")
                if type_input in type_dict:
                    return_type = type_dict[type_input]
                    return return_format, return_type
                else:
                    print(
                        f"<{type_input}> is an invalid input. Please Try Again\n")
                    continue
        else:
            print(f"<{format_input}> is an invalid input. Pleae Try Again\n")
            continue


def get_players_name_from_type():
    print_player_type()
    usertype_input = input("Enter an option from above : ")
    if usertype_input in type_dict:
        usertype_input = type_dict[usertype_input]
    else:
        print(f"{usertype_input} is an invalid input. Please Try again")
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='cricket')
    cursor = conn.cursor()
    data = cursor.execute(
        f"SELECT name from {'test'+usertype_input}")
    data = cursor.fetchall()
    nametable = PrettyTable()
    playersname = []
    nametable.field_names = ['Name']
    for row in data:
        nametable.add_row([row[0]])
        playersname.append(row[0])

    print(nametable)
    gotname = False
    while not gotname:
        nameinput = input("Please Enter a name to see the data : ").lower()
        if nameinput in playersname:
            gotname = True
            print(nameinput, usertype_input)
            return nameinput, usertype_input

        else:
            print(f"<{nameinput}> is not there in the table. Please try again")


def see_format_table():
    format, type = get_format_and_type()
    order_value, order_type = get_order_based_on(type)
    if order_type == '':
        print(
            f"Table for format:{format}, type:{type}, order_value:{order_value}, order_type:ascending")
    else:
        print(
            f"Table for format:{format}, type:{type}, order_value:{order_value}, order_type:descending")

    conn = sq.connect(host='localhost', user='root',
                      password='student', database='cricket')
    cursor = conn.cursor()
    tablename = format.lower() + type.lower()
    cursor.execute(
        f"SELECT * FROM {tablename} ORDER BY {order_value} {order_type}")
    data = cursor.fetchall()
    table = PrettyTable()
    if type == 'batsmen':
        field_names_list = batsmen_fields
    else:
        field_names_list = bowlers_fields
    for row in data:
        row = list(row)
        table.field_names = field_names_list
        table.add_row(row)
    print(table)
    conn.close()


def print_player_table(playername, playertype):
    """user can see all the data of the player"""
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='cricket')
    cursor = conn.cursor()

    if playertype == 'batsmen':
        querystring = "SELECT matchesPlayed,runsScored,strikeRate,average,halfCenturies,centuries,highestScore FROM {} WHERE name = '{}'"
        datatable = PrettyTable()
        datatable.add_column('fields\\formats', batsmen_orderby)
    else:
        querystring = "SELECT matchesPlayed,wicketsTaken,economy,5wicketsInAMatch FROM {} WHERE name = '{}'"
        datatable = PrettyTable()
        datatable.add_column('fields\\formats', bowlers_orderby)

    for type in formats_list:
        cursor.execute(querystring.format(type.lower()+playertype, playername))
        data = cursor.fetchall()
        datatable.add_column(type, list(data[0]))
    conn.close()
    print(datatable)


def see_player_stats():
    "user can see the stats of a player"
    playername, playertype = get_players_name_from_type()
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='cricket')
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT dob FROM {'odi'+playertype} WHERE name = '{playername}'")
    dob = cursor.fetchone()[0]
    conn.close()
    print(f"\nPlayer Name : {playername}")
    print(f"Type : {playertype}")
    print(f"DOB : {dob}\n")
    print_player_table(playername, playertype)

    return playername, playertype



def get_date():
    """user enters the date of the player"""
    print("- DATE INPUT -")
    day = input("Enter the day : ")
    month = input("Enter the month ('jan' for january) : ")
    year = input("Enter the year : ")
    date = f"{day} {month} {year}"
    return date

def delete_player():
    """user can delete a retired player from the database"""
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='cricket')
    cursor = conn.cursor()

    plr_format, plr_type = get_format_and_type()
    get_table_name = plr_format+plr_type
    cursor.execute(f"select name from {get_table_name}")
    player_name = cursor.fetchall()
    print("Available players in the database")
    player_table = PrettyTable()
    player_table.field_names = ['Player Name']
    for row in player_name:
        player_table.add_row(row)

    print(player_table)
    print('\n')
    
    player_input = input("Enter the player name : ")
    check_val = False
    for row in player_name:        
        if row[0].lower() == player_input.lower():            
            check_val = True            
            break

    if check_val:
        print("Player match found.\n")
        confirm_input = input("Do you want to delete the player (Y / N) : ")
        if confirm_input.lower() == 'y':
            try:    
                cursor.execute(f"delete from {get_table_name} where name = '{player_input}'")
                conn.commit()
                print(f"You have successfully deleted <{player_input}> from {plr_format} table")
            except conn.Error as err:
                print("The following error as occurred")
                print(err)
                conn.close()
                return None

        else:
            print("You chose not to delete the player.")
            conn.close()
            return None

    else:
        print("The enetered player does not exists. Please Try again")
        return None


    conn.close()

    

def add_new_player():
    """user can add a player to the database"""
    print("You chose to add a new player to the database\n")  
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='cricket')
    cursor = conn.cursor()
    plr_format, plr_type = get_format_and_type()
    get_table_name = 'odi'+plr_type
    cursor.execute(f"select name from {get_table_name}")
    player_name = cursor.fetchall()
    print("Available players in the database")
    player_table = PrettyTable()
    player_table.field_names = ['Player Name']
    for row in player_name:
        player_table.add_row(row)

    print(player_table)
    print('\n')
    player_input = input("Enter the player name : ")
    for name in player_name:
        if name[0].lower() == player_input.lower():
            print(f"<{player_input}> already exists in the database. Please update the data")
            conn.close()
            return None
    player_dob = get_date()

    if plr_type == 'batsmen':
        cursor.execute(f"insert into {'test'+plr_type} values ('{player_input}','{player_dob}',{0},{0},{0.0},{0.0},{0},{0},{0})")
        cursor.execute(f"insert into {'odi'+plr_type} values ('{player_input}','{player_dob}',{0},{0},{0.0},{0.0},{0},{0},{0})")
        cursor.execute(f"insert into {'t20'+plr_type} values ('{player_input}','{player_dob}',{0},{0},{0.0},{0.0},{0},{0},{0})")

    elif plr_type == 'bowlers':
        cursor.execute(f"insert into {'test'+plr_type} values ('{player_input}','{player_dob}',{0},{0},{0.0},{0})")
        cursor.execute(f"insert into {'odi'+plr_type} values ('{player_input}','{player_dob}',{0},{0},{0.0},{0})")
        cursor.execute(f"insert into {'t20'+plr_type} values ('{player_input}','{player_dob}',{0},{0},{0.0},{0})")

    conn.commit()
    print("The data has been added sucessfully. To update the stats use <update option>")

    conn.close()
        

def get_specific_value(playername, playertype, playerformat, ordervalue):
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='cricket')
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT {ordervalue} FROM {playerformat+playertype} WHERE name = '{playername}'")
    value = cursor.fetchone()
    conn.close()
    return value



def update_player_stats():
    """user can update stats of a player"""
    playername, playertype = see_player_stats()
    while True:
        print_format_type()
        format_input = input("Select a format to update : ")
        if format_input in format_dict:
            playerformat = format_dict[format_input]
        else:
            print(f"<{format_input}> is invalid format. Please Try Again")
            continue
        print(playerformat)
        if playertype == 'batsmen':
            playerlist = batsmen_orderby
            playerdict = batsmen_orderby_dict
        else:
            playerlist = bowlers_orderby
            playerdict = bowlers_orderby_dict
        while True:
            print(f"--- Player Data ---")
            for i in range(len(playerlist)):
                print(f"Press ({i + 1}) to update {playerlist[i]}")
            print()
            order_value_input = input("Enter the desired order number : ")
            if order_value_input in playerdict:
                ordervalue = playerdict[order_value_input]
            else:
                print(f"<{order_value_input}> is invalid. Please Try Again")
                continue
            present_value = get_specific_value(
                playername, playertype, playerformat, ordervalue)

            print(f"The current value of {ordervalue} is {present_value[0]}")
            confirm_input = input("Are you sure you want to update (Y / N) : ")
            if confirm_input.lower() == 'y':
                value_input = input(f"Enter the new value for {ordervalue} : ")
                if isinstance(present_value, int):
                    try:
                        value_input = int(value_input)
                    except ValueError:
                        print(
                            f"{value_input} is invalid data for updating. Please Try Again")
                        continue
                else:
                    try:
                        value_input = float(value_input)
                    except ValueError:
                        print(
                            f"{value_input} is invalid data for updating. Please Try Again")
                        continue
                conn = sq.connect(host='localhost', user='root',
                                  password='student', database='cricket')
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        f"UPDATE {playerformat+playertype} SET {ordervalue} = {value_input} WHERE name = '{playername}'")
                    conn.commit()
                except sq.Error:
                    print("An Error Occurred while updating the data. Please Try Again")
                    return None
                print("#"*20)
                print("Data Updated Sucessfully")
                print("#"*20, '\n')
                print_player_table(playername, playertype)
                break

            else:
                print("You chose not to update the data.")
                return None

        update_more = input("Do you want to update more (Y / N) : ")
        if update_more.lower() == 'y':
            continue
        else:
            return None
