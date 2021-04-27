import mysql.connector as sq
import random as r
from prettytable import PrettyTable
from mysql.connector import Error as sqlerror
from os import system
from time import sleep
from getpass import getpass

def print_mistakes_table():
    """This function prints the mistakes table"""
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()

    cursor.execute("select * from mistakes")
    data = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['Question', 'Given Answer','User Given Answer']
    for row in data:
        table.add_row(row)
    conn.close()

    return table
    
def return_questions_data():
    """Returns the prettytable of questions along with questions in dictionary format"""
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()
        
    cursor.execute("select * from questions")
    data = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['Question', 'Answer']
    questions = {}
    for q,a in data:
        table.add_row([q,a])
        questions[q] = a
    conn.close()

    return table, questions
    
def correct_append_mistakes():
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()
    
    print("-- Mistakes table --")
    mistakes_table = print_mistakes_table()
    print(mistakes_table)
    print('\n')
    sleep(1.5)
    print("-- Questions table --")
    table, questions_dict = return_questions_data()
    print(table)

    question_input = input("Enter the question to update it : ").lower()

    if question_input not in questions_dict:
        print("Please enter the complete question as in the table.")
        return None
    else:
        print('Press (1) to change the question')
        print('Press (2) to change the answer')

        change_input = input("Please enter you choice : ")
        if change_input not in ['1','2']:
            print("You have entered an invalid choice. Please Try Again.")

        elif change_input == '1':
            print("You chose to change the question.")

            new_question_input = input("Plese Enter the new question : ")
            confirm = input("Are you sure you want to update (Y / N) : ")
            if confirm in ['y','Y']:
                cursor.execute(f"update questions set question = '{new_question_input}' where question = '{question_input}'")
                conn.commit()
                print("YOU HAVE SUCCESSFULLY UPDATED THE QUESTION")
            else:
                print("You chose not to update the question.")
                return None

        elif change_input == '2':
            print("You chose to change the answer for a question")

            new_answer_input = input("Please Enter the new answer : ")
            confirm = input("Are you sure you want to update (Y / N) : ")
            if confirm in ['y','Y']:
                cursor.execute(f"update questions set answer = '{new_answer_input}' where question = '{question_input}'")
                conn.commit()
                print("YOU HAVE SUCCESSFULLY UPDATED THE ANSWER FOR THE QUESTION")
            else:
                print("You chose not to update the answer of the questions.")
                return None

        else:
            pass

def delete_question():
    """This function allows the admin user to delete the question from the questions table"""
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()

    table, questions = return_questions_data()
    print(table)
    sleep(1.5)

    question_input = input("Enter the question to delete : ")
    if question_input in questions:
        confirm_input = input("Are you sure you want to delete the question (Y / N) : ")
        if confirm_input.lower() == 'y':
            cursor.execute(f"delete from questions where question = '{question_input}'")
            conn.commit()
            print("\nThe question has been deleted successfully.")
            conn.close()
        else:
            print("You chose not to delete the question.")
            conn.close()
            return None

    else:
        print("The question was not found in the database. Please enter the question as in the table")
        conn.close()
        return None
        

def clear_mistakes_table():
    """This function lets the admin user clears the mistakes table"""
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()
    table = print_mistakes_table()
    print(table)
    sleep(1.5)
    confirm_input = input("Are you sure you want to delete the mistakes table (Y / N) : ")
    if confirm_input.lower() == 'y':
        cursor.execute("delete from mistakes")
        conn.commit()
        print("\n")
        print("Mistakes table has been successfully cleared.\n")
    else:
        print("You chose not to clear the mistakes table")
        conn.close()
        return None
    


def exit_program():
    print("Thank You for using the program.")
    exit()

def main_admin_menu():
    """This function prints the admin menu and takes input from the user"""
    system('cls')
    while True:
        print("----- ADMIN MENU -----")
        print("Press (1) to append the mistakes in questions of ROUND 1")
        print("Press (2) to delete a question from questions table")
        print("Press (3) to clear the mistakes table")
        print("Press (4) to go the main menu")
        print("Press (5) to exit the program")

        admin_user_dict = {'1' : correct_append_mistakes,
                           '2' : delete_question,
                           '3' : clear_mistakes_table,
                           '5' : exit_program}
        admin_user_input = input("Enter you choice : ")

        if admin_user_input in admin_user_dict:
            admin_user_dict[admin_user_input]()
            
        elif admin_user_input == '4':
            return None
        
        else:
            print("You have entered an invalid option. Please Try Again")
            continue


        
        
