from db_connect import est_conn
import explore
from time import sleep
from the_exit import exit_program

conn, cursor = est_conn()

def write_review():
    print("\nYou have to chose a phone to write a review for a phone\n")
    company_table = explore.make_company_table()
    print(company_table,'\n')
    sleep(2)

    company_input = input("Enter the name of the company from the above options: ")

    models_list, models_table = explore.get_single_primary_list_table('model', company_input)
    print('\n')
    print(models_table)
    print("\nNote : Please enter the name as in the list above.")
    model_input = input("Enter the name of the model to write a review: ")

    if model_input in models_list:
        print("\nBefore you write the review just give a look at the complete features of the selected phone\n")

        detailed_table = explore.get_detail_table(model_input)
        print(detailed_table)

        reviewer_name = input("Before you write your review please specify your name: ")

        complete_review = input("Please type your complete review here: ")

        cursor.execute(f"INSERT INTO direct_review values ('{reviewer_name}', '{model_input}', '{complete_review}')")
        conn.commit()

        print("\nYou review has been entered. Thank you for your review\n")
        sleep(1.5)

    else:
        print("\nYou have entered an invalid model. Please try again")
        sleep(1.5)

def review():
    while True:
        print("\nYou can write reviews to the phones that are available\n")
        print("Press (1) to write a review for a mobile")
        print("Press (2) to explore the mobiles for review")
        print("Press (3) to go to customer menu")
        print("Press (4) to exit the Program\n")

        rev_dict = {'1' : write_review, '2' : explore.explore, '4' : exit_program}

        user_input = input("Enter a number from the above available options: ")

        if user_input in rev_dict:
            rev_dict[user_input]()

        elif user_input == '3':
            print("\nYou chose to go to customer menu")
            sleep(1.2)
            break

        else:
            print("\nYou have entered an invalid input.Please try again")
            sleep(2)
