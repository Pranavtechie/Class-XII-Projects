import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'student', database='project' )
cust1=conn.cursor()
for i in range(0,76):
 print('WELCOME TO COURIER SERVICE:')
 print('1.Courier_order and customer_details')
 print('2.billing_procedure')
 print('3.courier_service_boys')
 print('4.exit')
 choice=int(input('enter the section you want to access:....(1,2,3or4)........:'))
 if choice==1:
    print('For placing a courier do enter A')
    print('To see order placed list do enter B')
    print('enter c to cancel the order')
    sect=str(input('enter the section that you want to access:'))
    if sect=="A":
       print('COURIER-ORDER')
       a=(input('enter the customer name:'))
       b=int(input('enter the customer mobile number:'))
       c=(input('enter the customer address:'))
       d=(input('enter the receiver name:'))
       e=int(input('enter the receiver mobile number:'))
       f=(input('enter the receiver address:'))
       cust1.execute("INSERT INTO courier VALUES(' "+a+" ',"+str(b)+",' "+c+" ',' "+d+" ',"+str(e)+",' "+f+" ')")
       conn.commit()
       print(cust1.rowcount,'courier (s) placed')
       print('===============================================================================================================')
    elif sect=="B":
       S=str(input('do you want to see your courier_order''(y \ n):'))
       if S=="y":
         a=input('enter the customer mob number:')
         cust1.execute('select * from courier where customer_mobile_number="{}" '.format(a))
         order=cust1.fetchall()
         print('customer name,','customer mob no,','customer address,','receiver name,','receiver mob no,','receiver address:')
         for j in order:
              print(j)
         print('===============================================================================================================')

    elif sect=="c":

        mob_no=int(input(('enter the mobile number to delete your order: ')))
        cust1.execute(f"delete from courier where customer_mobile_number='{mob_no}'")
        conn.commit()
        
        print('Order successfully deleted')
    else:
        print('Thank you')
        print('==============================================================================================================')
 elif choice==2:
      print('BILLING PROCEDURE:[weight_in_kgs......AND.......cost_in_rupees]')
      cust1.execute("select * from couriers2")
      bill=cust1.fetchall()
      for x in bill:
           print(x)
      print('===============================================================================================================')
 if choice==3:
      city1=input('enter your city name:')
      cust1.execute("select * from couriers3 where city='"+city1+"' ".format(city1))
      boys = cust1.fetchall()
      print(' City    delivery_boy     mobile no:')
      for y in boys:
             print(y)
      print('===============================================================================================================')
 elif choice==4:
            quit()


B_COURIER_MENU.py









