from db_connect import est_conn
import explore
from time import sleep
from the_exit import exit_program

conn, cursor = est_conn()

def phone_buy():
    company_table = explore.make_company_table()
    print(company_table)
    sleep(3)

    company_input = input("\nEnter the company name from the above options: ")

    if company_input in explore.companies_lower:
        model_list, model_table = explore.get_single_primary_list_table('model',company_input)
        print(model_table)
        sleep(3)
        print("\nNote: Enter the model name as in the above table\n")
        model_input = input("Enter the model name from the above available options: ")

        if model_input in model_list:
            cursor.execute(f"SELECT quantity FROM quantity WHERE model = '{model_input}'")
            quantity_info = cursor.fetchone()[0]

            if quantity_info > 0:

                print("Before we go with the purchase you can see the complete details of the selected model\n")
                sleep(1.7)
                detail_table = explore.get_detail_table(model_input)
                print(detail_table)
                sleep(2)

                print("\nNote: Ones you confirm the purchase you can't undo the purchase please be sure while confirming\n")
                sleep(1.5)
                confirm = input("The selected mobile is in stock. Do you want to continue your purchase. (Y / N): ")

                if confirm in ['y','Y']:
                    print("\nThank you for choosing our services. Please fill the details below to complete your purchase\n")

                    customer_name = input("Please enter your name: ")
                    experience = input("\nHow was you experience spending time with us: ")
                    mobile_review = input("\nTell us your opinion on the phone you purchased: ")

                    cursor.execute(f"INSERT INTO purchase_review VALUES ('{model_input}', '{customer_name}','{experience}','{mobile_review}')")
                    conn.commit()

                    cursor.execute(f"UPDATE quantity SET quantity = quantity - 1 WHERE model = '{model_input}'")
                    conn.commit()

                    print("\nYou have successfully completed you purchase.")
                    sleep(2)

                else:
                    print("\nYou chose to cancel the purchase. If you want to by please try again.")
                    sleep(2)

            else:
                print("\nSorry, The mentioned model is out of stock, you can try to purchase different model")
                sleep(2)

        else:
            print("\nYou have entered an invalid model, Please try again.")
            sleep(2)

    else:
        print("\nThe entered company name does not exits. Please try again.\n")
        sleep(2)


def buy_phone():

    while True:
        print("\nYou can buy any mobile which are available here. Happy Shopping!\n")
        print("Press (1) to explore the mobile you want to buy")
        print("Press (2) to buy the mobile")
        print("Press (3) to go the main menu")
        print("Press (4) to exit the program\n")

        user_input = input("Enter the required input the above options: ")

        input_dic = {'1' : explore.explore, '2' : phone_buy, '4' : exit_program}

        if user_input in input_dic:
            input_dic[user_input]()

        elif user_input == '3':
            break

        else:
            print("You have entered an invalid input. Please try again")
