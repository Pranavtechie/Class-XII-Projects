import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'student', database='project' )
cust1=conn.cursor()
cust1.execute("insert into couriers3 values('kadapa','mohith','8328480609')")
cust1.execute("insert into couriers3 values('kalikiri','nani','9581207696')")
cust1.execute("insert into couriers3 values('kerala','amit','8666666666')")
cust1.execute("insert into couriers3 values('bengaluru','DJ','689742315')")
cust1.execute("insert into couriers3 values('kalikiri','naveen','200034272')")
conn.commit()
conn.close()