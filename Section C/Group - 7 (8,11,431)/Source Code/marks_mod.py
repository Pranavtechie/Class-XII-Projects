import mysql.connector as mysql
mycon = mysql.connect(host='localhost',user='root',password='student',charset='utf8')
mycur = mycon.cursor()
mycur.execute(f"SHOW DATABASES LIKE 'students'")
database_check = mycur.fetchall()
if database_check == []:
    mycur.execute(f"create database students")
    mycon.commit()
    mycur.execute(f"use students")
    mycon.commit()
    mycur.execute(f"create table data(rollno int(5) primary key not null,name varchar(50) not null,section char(1) not null)")
    mycon.commit()
    mycur.execute(f"create table pre_mid_term(rollno int(5) not null unique,english int(2),maths int(2),physics int(2),chemistry int(2),computer int(2),biology int(2),foreign key (rollno) references data(rollno))")
    mycon.commit()
    mycur.execute(f"create table mid_term(rollno int(5) not null unique,english int(2),maths int(2),physics int(2),chemistry int(2),computer int(2),biology int(2),foreign key (rollno) references data(rollno))")
    mycon.commit()
    mycur.execute(f"create table post_mid_term(rollno int(5) not null unique,english int(2),maths int(2),physics int(2),chemistry int(2),computer int(2),biology int(2),foreign key (rollno) references data(rollno))")
    mycon.commit()
    mycur.execute(f"create table annual(rollno int(5) not null unique,english int(2),maths int(2),physics int(2),chemistry int(2),computer int(2),biology int(2),foreign key (rollno) references data(rollno))")
    mycon.commit()
mycur.execute(f"use students")
mycon.commit()
exam_dict = {1:'pre_mid_term',2:'mid_term',3:'post_mid_term',4:'annual'}
sub_dict = {1:'english',2:'maths',3:'physics',4:'chemistry',5:'computer',6:'biology'}
def show_all_marks():
    print('''1.show pre mid term marks
2.show mid term marks
3.show post mid term marks
4.show annual exam marks''')
    show_select = int(input('enter the desired option:'))
    mycur.execute(f"select * from {exam_dict[show_select]}")
    print_marks = mycur.fetchall()
    print('rollno\t\tenglish marks\t\tmaths marks\t\tphysics marks\t\tchemistry marks\t\tcomputer marks\t\tbiology marks')
    for i in print_marks:
        print()
        for j in i:
            print(j,end='\t\t\t')
    print()
    print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
def show_stu_marks():
    rollno_search = int(input('enter the rollno:'))
    mycur.execute(f"SELECT EXISTS(SELECT * from data WHERE rollno={rollno_search});")
    rollno_check = mycur.fetchall()
    if rollno_check == [(0,)]:
        print('rollno does not exist')
    else:
        print('rollno\t\tname\t\tsection')
        mycur.execute(f"select * from data where rollno = {rollno_search}")
        show_print_1 = mycur.fetchall()
        for i in show_print_1:
            print()
            for j in i:
                print(j,end='\t\t\t')
            print()
        print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
        for i in exam_dict:
            exam_search_dict = exam_dict[i]
            print(exam_search_dict,'marks')
            print('rollno\t\tenglish marks\t\tmaths marks\t\tphysics marks\t\tchemistry marks\t\tcomputer marks\t\tbiology marks')
            mycur.execute(f"select * from {exam_search_dict} where rollno = {rollno_search}")
            show_print = mycur.fetchall()
            for i in show_print:
                print()
                for j in i:
                    print(j,end='\t\t\t')
                print()
            print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
def edit_marks():
    edit_roll = int(input('enter the roll no of student:'))
    mycur.execute(f"SELECT EXISTS(SELECT * from data WHERE rollno={edit_roll});")
    rollno_check_edit = mycur.fetchall()
    if rollno_check_edit == [(0,)]:
        print('rollno does not exist')
        print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    else:
        print('''1.edit name
2.edit section
3.edit marks''')
        edit_select = int(input('enter the desired option:'))
        print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
        if edit_select == 1:
            edit_name = input('enter the name:')
            mycur.execute(f"update data set name = '{edit_name}' where rollno = {edit_roll}")
            mycon.commit()
            print('data has been successfully edited')
        elif edit_select == 2:
            edit_sec = input('enter the section:')
            mycur.execute(f"update data set section = '{edit_sec}' where rollno = {edit_roll}")
            mycon.commit()
            print('data has been successfully edited')
        elif edit_select == 3:
            print('''1.edit english marks
2.edit maths marks
3.edit physics marks
4.edit chemistry marks
5.edit computer marks
6.edit biology marks''')
            edit_select_marks = int(input('enter desired option:'))
            print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
            print('''1.update pre mid term marks
2.update mid term marks
3.update post mid term marks
4.update annual exam marks''')
            edit_exam_marks =int(input('enter the desired option:'))
            edit_sub_marks = int(input('enter the updated marks:'))
            while 0 > edit_sub_marks or edit_sub_marks > 80:
                edit_sub_marks = int(input('enter the updated marks:'))
            mycur.execute(f'update {exam_dict[edit_exam_marks]} set {sub_dict[edit_select_marks]} = {edit_sub_marks} where rollno = {edit_roll}')
            mycon.commit()
            print('marks have been successfully updated')
            print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
def delete_marks():
    rollno_del = int(input('enter the student roll no:'))
    mycur.execute(f"SELECT EXISTS(SELECT * from data WHERE rollno={rollno_del});")
    rollno_check_del = mycur.fetchall()
    if rollno_check_del == [(0,)]:
        print('rollno does not exists')
        print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    else:
        for i in exam_dict:
            exam_del_dict = exam_dict[i]
            mycur.execute(f"delete from {exam_del_dict} where rollno = {rollno_del}")
            mycon.commit()
        mycur.execute(f"DELETE FROM data WHERE rollno = {rollno_del}")
        mycon.commit()
        print('data of student has been successfully deleted')
        print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
def add_marks():
    rollno_add = int(input('enter the student roll no:'))
    mycur.execute(f"SELECT EXISTS(SELECT * from data WHERE rollno={rollno_add});")
    rollno_check_add = mycur.fetchall()
    if rollno_check_add == [(1,)]:
        print('rollno already exists')
        print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
    else:
        name = input('enter the student name:')
        section = input('enter the section:')
        mycur.execute(f"insert into data values({rollno_add},'{name}','{section}')")
        mycon.commit()
        for i in exam_dict:
            exam_edit_dict = exam_dict[i]
            mycur.execute(f"insert into {exam_edit_dict} values({rollno_add},null,null,null,null,null,null)")
            mycon.commit()
        print('''1.add pre mid term marks
2.add mid term marks
3.add post mid term marks
4.add annual exam marks''')
        add_select = int(input('select the desired option:'))
        add_english_1 = int(input('enter the english marks:'))
        while 0 > add_english_1 or add_english_1 > 80:
            add_english_1 = int(input('enter the english marks:'))
        add_math_1 = int(input('enter the maths marks:'))
        while 0 > add_math_1 or add_math_1 > 80:
            add_math_1 = int(input('enter the maths marks:'))
        add_physics_1 = int(input('enter the physics marks:'))
        while 0 > add_physics_1 or add_physics_1 > 80:
            add_physics_1 = int(input('enter the physics marks:'))
        add_chemistry_1 = int(input('enter the chemistry marks:'))
        while 0 > add_chemistry_1 or add_chemistry_1 > 80:
            add_chemistry_1 = int(input('enter the chemistry marks:'))
        print('''1.computer
2.biology''')
        sub_select = int(input('enter the fifth subject:'))
        if sub_select == 1:
            add_computer_1 = int(input('enter the computer marks:'))
            while 0 > add_computer_1 or add_computer_1 > 80:
                add_computer_1 = int(input('enter the computer marks:'))
            mycur.execute(f"update {exam_dict[add_select]} set english={add_english_1},maths={add_math_1},physics={add_physics_1},chemistry={add_chemistry_1},computer={add_computer_1} where rollno = {rollno_add}")
            mycon.commit()
        else:
            add_biology_1 = int(input('enter the biology marks:'))
            while 0 > add_biology_1 or add_biology_1 > 80:
                add_biology_1 = int(input('enter the biology marks:'))          
            mycur.execute(f"update {exam_dict[add_select]} set english={add_english_1},maths={add_math_1},physics={add_physics_1},chemistry={add_chemistry_1},biology={add_biology_1} where rollno = {rollno_add}")
            mycon.commit()
        print('data has been successfully added')
        print('''------------------------------------------------------------------------------------------------------------------------------------------------------------------''')