import mysql.connector as sq
from prettytable import PrettyTable
from os import system

def heading():
    print("--- Marks Consodlidation ---")

def menu():
    print("--- Main Menu ---\n")
    print('1. To show the cadets total marks')
    print('2. To show subject wise cadet marks')
    print('3. To get remedial cadets')
    print('4. To get subject average')
    print('5. To update cadet marks')
    print('6. To delete a cadet ')
    print('7. To search a cadet marks')
    print('8. Exit the Program')
system('cls')
heading()

def show_cadets_total_marks():
    """This function shows the marks of all the cadets"""
    conn = sq.connect(host = 'localhost', user = 'root', password = 'student', database = 'marks')
    cursor = conn.cursor()

    cursor.execute('select * from cadets_total_marks')
    data = cursor.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = ['Roll No', 'Name', 'Class', 'Section', 'Total Marks']
    for row in data:
        table.add_row(row)

    print(table)

def cadets_marks():
    """This function shows the marks of all the cadets"""
    conn = sq.connect(host = 'localhost', user = 'root', password = 'student', database = 'marks')
    cursor = conn.cursor()

    cursor.execute('select cadets_marks.rollno, name, class, section,mathematics, physics, chemistry, english, comp_or_bio from cadets_marks,cadets_total_marks where cadets_marks.rollno = cadets_total_marks.rollno')
    data = cursor.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = ['Roll No', 'Name', 'Class', 'Section', 'Mathematics', 'Physics','Chemistry','English','Comp/Bio']
    for row in data:
        table.add_row(row)
    
    print(table)
    

def get_remedial_cadets(sub_name):
    """This function shows the cadets for remedial for a subject"""
    conn = sq.connect(host = 'localhost', user = 'root', password = 'student', database = 'marks')
    cursor = conn.cursor()

    cursor.execute(f"select cadets_marks.rollno,name,section,{sub_name} from cadets_marks,cadets_total_marks where {sub_name} < 60.00 and cadets_total_marks.rollno = cadets_marks.rollno")
    data = cursor.fetchall()
    conn.close()

    table = PrettyTable()
    table.field_names = ['Roll No', 'Name', 'Section',sub_name]
    for row in data:
        table.add_row(row)
    
    print(table)
   

def remedial_menu():
    """This function shows the menu of subject and selection for user"""
    while True:
        print('-- Remedial Menu --')
        print('1. Physics')
        print('2. Chemistry')
        print('3. Mathematics')
        print('4. English')
        print('5. Computer/Biology')
        print('6. Go to Main Menu')

        sub_dict = {
            '1' : 'physics',
            '2' : 'chemistry',
            '3' : 'mathematics',
            '4' : 'english',
            '5' : 'comp_or_bio'
        }

        sub_input = input("Enter the desired number for a subject : ")

        if sub_input in sub_dict:
            get_remedial_cadets(sub_dict[sub_input])

        elif sub_input == '6':
            break

def get_subject_average():
    """This function returns all the subject averages"""
    conn = sq.connect(host = 'localhost', user = 'root', password = 'student', database = 'marks')
    cursor = conn.cursor()

    cursor.execute('select avg(chemistry),avg(physics),avg(mathematics),avg(english),avg(comp_or_bio) from cadets_marks')
    data = cursor.fetchall()
    conn.close()
    table = PrettyTable()
    table.field_names = ['Chemistry', 'Physics', 'Mathematics', 'English', 'Computer/Biology'] 
    for row in data:
        table.add_row(row)

    print(table)
    
def update_cadet_marks():
    """This function lets the teacher update the cadets marks"""
    conn = sq.connect(host = 'localhost', user = 'root', password = 'student', database = 'marks')
    cursor = conn.cursor()

    roll_no = int(input("Enter the rollno to update the marks : "))

    cursor.execute(f"select cadets_total_marks.rollno, name, class, section, mathematics, physics,chemistry,english, comp_or_bio from cadets_marks,cadets_total_marks where cadets_total_marks.rollno = {roll_no} and cadets_marks.rollno = cadets_total_marks.rollno")
    data = cursor.fetchall()

    first_table = PrettyTable()
    first_table.field_names = ['Roll No', 'Name', 'Class', 'Section', 'Mathematics', 'Physics','Chemistry','English','Comp/Bio']
    for row in data:
        first_table.add_row(row)

    print(first_table)

    maths_input = float(input("Enter Mathematics Marks : "))
    phy_input = float(input("Enter physics marks"))
    che_input = float(input("Enter the Chemistry Marks"))
    eng_input = float(input("Enter the English Marks"))
    comp_input = float(input("Enter the Computer/Bio Marks"))

    total_marks = maths_input + phy_input + che_input + eng_input + comp_input
    cursor.execute(f"update cadets_total_marks set total_marks = {total_marks} where rollno = {roll_no}")
    cursor.execute(f"update cadets_marks set chemistry = {che_input}, physics = {phy_input}, mathematics = {maths_input}, comp_or_bio = {comp_input}, english = {eng_input} where rollno = {roll_no}")
    conn.commit()
    conn.close()
    print("Data has been updated successfully")

def delete_cadet():
    """This function lets the teacher delete the cadets marks"""
    conn = sq.connect(host = 'localhost', user = 'root', password = 'student', database = 'marks')
    cursor = conn.cursor()
    roll  = int(input("Enter the rollno of the cadet : "))
    ans = input('are you sure you want  delete:')
    if ans == 'y' or ans == 'Y':
        query1 = "delete from cadets_marks where rollno = {}".format(roll)
        cursor.execute(query1)
        conn.commit()
        query2 = "delete from cadets_total_marks where rollno = {}".format(roll)
        cursor.execute(query2)
        conn.commit()
        print("Data deleted successfully")
    conn.close()

def cadet_marks():
    """This function lets the teacher search the cadets marks"""
    conn = sq.connect(host = 'localhost', user = 'root', password = 'student', database = 'marks')
    cursor = conn.cursor()
    roll  = int(input("Enter the rollno of the cadet : "))
    query = "select * from cadets_marks where rollno ={} ".format(roll)
    cursor.execute(query)
    data = cursor.fetchall()
    
    t = PrettyTable(['Rollno','mathematics','physics','chemistry','English','Comp or Bio'])
    for row in data:
        t.add_row(row)
    print(t)
    conn.commit()
    conn.close()



while True:
    menu()

    user_input = input("Enter your desired choice : ")

    dict = {
        '1' : show_cadets_total_marks,
        '2' : cadets_marks,
        '3' : remedial_menu,
        '4' : get_subject_average,
        '5' : update_cadet_marks,
        '6' : delete_cadet,
        '7' : cadet_marks,
        '8' : exit
    }

    if user_input in dict:
        dict[user_input]()

    else:
        print("You have entered an invalid input. Please Try Again")
        continue
