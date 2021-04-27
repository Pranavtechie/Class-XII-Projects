import mysql.connector as sq
import random as r
from mysql.connector import Error as sqlerror
from os import system
from time import sleep
from getpass import getpass
from admin import main_admin_menu
user_points = 0
computer_points = 0
random_list = []
x = 1



def start_program():
    """The start of the program"""
    while True:
        system('cls')
        print("\n~~~~~~~~~~~~~ QUIZ INTERFACE ~~~~~~~~~~~~~~~")
        print("Press (0) to Log in as Admin")
        print("Press (1) to Play the Game")
        print("Press (2) to exit the program")

        user_input = input("Please Enter your choice : ")
        if user_input == '0':
            login_as_admin()
        elif user_input == '1':
            start_rebuttal()
        else:
            exit_program()

def exit_program():
    print("Thank You for using the program.")
    exit()

def login_as_admin():
    """This function handles the logging in of admin to the program"""
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()

    username_input = input('Please Enter your username : ')

    cursor.execute(f"select * from admin_user where username = '{username_input}'")
    data = cursor.fetchone()
    if data == ():
        print("The entered username does not exists in the database. Please contact the developer")
        sleep(1)
        start_program()
    else:
        password_input = getpass('Please Enter your password : ')
        if password_input == data[2]:
            print('You have successfully logged in as admin')
            sleep(1.5)
            main_admin_menu()
        else:
            print(f"The entered password for the username <{username_input}> is invalid. Please try Again")
            sleep(1.5)
            start_program()

    
def get_questions():

    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")
    data = cursor.fetchall()
    conn.close()
    return data


def append_mistakes(question, given_answer, correct_answer):
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()

    cursor.execute(
        f"INSERT INTO mistakes VALUES ('{question}','{given_answer}','{correct_answer}')")
    conn.commit()
    conn.close()

    print(f"The question has been updated successfully. Thank you")


def start_rebuttal():
    system('cls')
    print(f"\n>>>>> ROUND 1 : REBUTALL QUIZ <<<<<\n")
    print(f"Rules :")
    print(f"1. This ROUND will consist of 10 questions")
    print(f"2. User and computer can ask questions one after another. Who get's the higest points win's the game")
    print(f"3. You should not ask the same question twice")
    print(f"4. If the user qualifies ROUND 1. There will be a assessment question to qualify for the FINAL ROUND")
    print(f"5. If you're score is less than the computer, you are not eligible for assessment")
    global x, user_points, computer_points, username
    username = input("\nEnter your name to start the game: ")

    if username == '' or username == '\n':
        print(f"You have not entered your name. You are not eligible to play this game")
        print("Please start the game again")
        exit()

    while x <= 10:
        print(f"Question {x}: ")
        if x % 2 != 0:
            computer_question()
        else:
            user_question()

        x += 1

    else:
        print(f"### ROUND 1 COMPLETED ###")
        show_points(user_points, computer_points)

        if user_points > computer_points:
            start_assessment()

        else:
            print(f"\nYou did not qualify the REBUTTAL ROUND. Better Luck Next Time")
            exit()


def start_assessment():
    print("The Riddle to get to the Final Round")

    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM assessment")
    data = cursor.fetchone()
    conn.close()

    print(f"\n*** ASSESSMENT QUESTION ***")
    print(f"\nQueston : {data[0]}")

    user_answer_input = input("Enter your answer : ")

    if user_answer_input.lower() == data[1].lower():
        print(f"\n#### CORRECT ANSWER ####")
        print("\nYou are qualified for the 'FINAL ROUND'")
        start_riddle()

    else:
        print(f"You didn't qualify the assessment. Better Luck Next Time")
        exit()


def start_riddle():
    print(f"\n>>>>> FINAL ROUND : Riddle Time <<<<<\n")
    print(f"Rules : ")
    print(f"1. This round will consit of 5 questions")
    print(f"2. Only the computer can ask questions and the user has to answer to the question")

    r_list = []
    user_score = 0
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM riddles")
    data = cursor.fetchall()

    conn.close()

    for i in range(5):

        random_number = r.randint(1, len(data) - 1)

        if random_number not in r_list:
            r_list.append(random_number)

            print(f"Riddle {i+1}")
            print(f"{data[random_number][0]}")

            user_answer = input("Enter you answer : ")

            if user_answer.lower() == data[random_number][1].lower():
                print("\nCORRECT ANSWER")
                user_score += 1
                print(f"{username} Score is {user_score}")

            else:
                print(f"The Correct Answer is {data[random_number][1]}")
                print(f"{username} Score is {user_score}")

        else:
            continue
    
    print(f"You have completed the FINAL ROUND")
    final_score = user_points + 1 + user_score
    print(f"Your final score is {final_score}")
    print(f"Thank you for joining the Program")
    print(f"Have a nice day!!")
    exit()


def show_points(user, comp):
    global username
    print(f"\n{username} obtained {user} points")
    print(f"Computer obtained {comp} points\n")


def computer_question():

    global user_points, computer_points, random_list
    data = get_questions()
    while True:

        random_number = r.randint(0, len(data) - 1)

        if random_number not in random_list:
            random_list.append(random_number)
            question = data[random_number][0]
            answer = data[random_number][1]
            print(f"\nComputer Turn to ask question\n")
            print(f"\nQuestion : {question}")
            user_answer = input("\nEnter the answer for the question : ")

            if user_answer.lower() == answer.lower():
                print(f"\nCorrect Answer")
                user_points += 1
                show_points(user_points, computer_points)
                return None
            else:
                computer_points += 1
                print(f"\nWrong Answer")
                print(f"The Correct Answer is {answer}")

                user_conf = input("Is the given answer correct (Y / N) : ")

                if user_conf in ['y', 'Y']:
                    print(f"Thank you for your confirmation.")

                else:
                    print(f"You said that the given answer is wrong")
                    correct_input = input("Please Enter the correct answer : ")
                    append_mistakes(question, answer, correct_input)
                    show_points(user_points, computer_points)
                return None

        else:
            continue


def user_question():
    global username, user_points, computer_points, random_list
    print(f"{username} Turn to ask question\n")

    question_input = input("Enter your question : ")
    answer = get_user_answer(question_input)

    if answer:
        print(f"The answer to the question is {answer}")
        computer_points += 1

    else:
        print(f"Couldn't find the answer to the question")
        user_points += 1
        answer_input = input(
            f"Enter the correct answer for the question asked : ")
        add_question(question_input, answer_input)

    show_points(user_points, computer_points)


def get_user_answer(user_question):
    data = get_questions()

    for question, answer in data:
        if question.lower() == user_question.lower():
            return answer

    else:
        return None


def add_question(question, answer):
    conn = sq.connect(host='localhost', user='root',
                      password='student', database='quiz')
    cursor = conn.cursor()

    if question == '' or question == '\n':
        pass

    else:
        try:
            cursor.execute(
                f"INSERT INTO questions VALUES ('{question}','{answer}')")
            conn.commit()
            print(f"\nThank you for the new question. I got some knowledge")
            conn.close()

        except sqlerror:
            print(f"\nAn error occurred couldn't add the question to the database")
            conn.close()


if __name__ == '__main__':
    start_program()
