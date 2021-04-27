import os
from explore import explore
from buyphone import buy_phone
from write_review import review
from the_exit import exit_program
from time import sleep
from customer_request import request_menu

def clear_customer_screen():
    os.system('cls')
    print("--------------------------- VSR Mobiles --------------------------")
    print("----------------------- Mobile Phone Store -----------------------")
    print("--------------------- SAINIK SCHOOL KALIKIRI ---------------------")
    print("------------------------- Customer Login -------------------------\n\n")



def customer_menu():

    clear_customer_screen()

    while True:
        os.system('cls')

        print("------------ Customer Menu ------------\n")
        print("Press (1) for exploring the mobile Specifications")
        print("Press (2) for buying a mobile")
        print("Press (3) for writing a review")
        print("Press (4) to request new products")
        print("Press (5) for Clearing the screen")
        print("Press (6) to go to previous menu")
        print("Press (7) to exit the program\n\n")

        transfer_dic = {'1': explore, '2': buy_phone,'3' : review, '4': request_menu,'5': clear_customer_screen, '7' : exit_program }

        main_input = input("Enter your input from the above available options: ")

        if main_input in transfer_dic:
            print('\n')
            transfer_dic[main_input]()

        elif main_input == '6':
            print("\nYou chose to go to main menu\n")
            sleep(1)
            break

        else:
            print("\nYou have chose an incorrect option please try again\n")
            sleep(1)
            continue
