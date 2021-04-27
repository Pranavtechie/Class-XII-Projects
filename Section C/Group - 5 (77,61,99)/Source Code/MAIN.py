import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'student', database='project' )
cust1=conn.cursor()

print('WELCOME TO COURIER SERVICE:')
print("Hi")
o=input('Press enter to begin your courier surfing')
print('1.CREATE YOUR COURIER SERVICE ACCOUNT')
print('2.LOGIN')
print('3.UPDATE PROFILE')
choose=int(input('ENTER (1) FOR NEW ACCOUNT OR (2) FOR LOGIN OR (3) FOR UPDATE:'))
if choose==1:
     name=input('Enter your user-name:')
     passwd=input('Set your password here:')
     passwd1=input('Confirm password:')
     cust1.execute("INSERT INTO user VALUES(' "+name+" ',' "+passwd+" ')")
     conn.commit()
     print('ACCOUNT CREATED CONGRATULATIONS')
     move_in=input('press enter to login:')
     import B_COURIER_MENU
elif choose==2:
     user=input('Enter your username')
     passd=input('Enter your PASSWORD:')
     cust1.execute('select * from user where user_name = " '+user+' " and password = " '+passd+' " ')
     if cust1.fetchone() is None:
          print('sorry your password in wrong')
     else:
         import B_COURIER_MENU

elif choose==3:
     name1=input("Enter your existing user name:")
     passwd2=input('Enter your old password :')
     cust1.execute('select * from user where user_name = " '+name1+' " and password = " '+passwd2+' " ')
     data = cust1.fetchone()
     if name1 == data[0].strip() and passwd2 == data[1].strip():
          password = input("Enter your new password:")
          password1 = input("Confirm your new password:")
          if password == password1:
               Query = f"update user set password ='{password1}'where user_name='{data[0]}'"
               cust1.execute(Query)
               conn.commit()
               print("Password Successfully changed")


