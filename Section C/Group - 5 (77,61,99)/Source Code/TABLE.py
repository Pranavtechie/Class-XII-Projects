"""import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'student', database='project' )
cust1=conn.cursor()
cust1.execute('create table user(user_name varchar(99) ,password varchar(99))')
import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'student', database='project' )
cust1=conn.cursor()
cust1.execute('create table courier(customer_name varchar(99) ,customer_mobile_number varchar(789),customer_address text(789),receiver_name varchar(99) ,receiver_mobile_number varchar(789),receiver_address text(789))')



import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'student', database='project' )
cust1=conn.cursor()
cust1.execute('create table couriers2(Weight_in_kgs varchar(789),Cost_in_rupees varchar(789));')
"""


import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'student', database='project' )
cust1=conn.cursor()
cust1.execute('create table couriers3(city varchar(99),courier_boys varchar(99),courier_service_boys_mob_number varchar(99));')
