import mysql.connector as sql
mycon =sql.connect(host="localhost",user="root",passwd="student")
cursor=mycon.cursor()
st="create database if not exists sskal"
cursor.execute(st)
st="use sskal"
cursor.execute(st)
st="CREATE TABLE IF NOT EXISTS login(subject varchar(25),fname varchar(50),lname varchar(50),uid varchar(25),passwd varchar(25))"
cursor.execute(st)
st="CREATE TABLE IF NOT EXISTS physics(rollno int(10) not null)"
cursor.execute(st)
st="CREATE TABLE IF NOT EXISTS chemistry(rollno int(10) not null)"
cursor.execute(st)
st="CREATE TABLE IF NOT EXISTS english(rollno int(10) not null)"
cursor.execute(st)
st="CREATE TABLE IF NOT EXISTS mathematics(rollno int(10) not null)"
cursor.execute(st)
st="CREATE TABLE IF NOT EXISTS computerscience(rollno int(10) not null)"
cursor.execute(st)
st="CREATE TABLE IF NOT EXISTS details(rollno int(5) not null,name varchar(20),class int(5),section varchar(3),house varchar(20))"
cursor.execute(st)
mycon.commit()
print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✔✔✘✔ CLASS ATTENDANCE REGISTER ✘✔✘✘✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
print('✍To login press-(1) or Register press-(0)')
a=int(input("Enter your responce:"))
if a==0:
    fname=input('enter your first name✍:')
    lname=input('enter your last name✍:')
    sub={'P':'Physics','C':'Chemistry','M':'Mathematics','E':'English','CS':'ComputerScience'}
    for i in sub.keys():
        print(i,'-',sub[i])
    subcode=input('Enter your subjectCode✍:')
    subject=sub[subcode]
    uid=input('enter your user Id✍:')
    passwd=input('enter your password✍:')
    cursor=mycon.cursor()
    cursor.execute("INSERT INTO login(subject,fname,lname,uid,passwd) VALUES('{}','{}','{}','{}','{}')".format(subject,fname,lname,uid,passwd))
    mycon.commit()
    print('Registered Successfully....✔✔')
if a==1:
    uid=input('Enter your usernsme✍:')
    passwd=input('enter your password✍:')
    cursor=mycon.cursor()
    cursor.execute("SELECT * FROM login WHERE uid='{}' AND passwd='{}'".format(uid,passwd))
    data=cursor.fetchmany(1)
    count=cursor.rowcount
    lst=list(data)
    if lst==[]:
        print('✘Invalid Username or passwrd.........please try again...!')
    else:
        print('Logined successfully......✔✔')
        while 1<10:
            print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✔✔✘✔ WELCOME TO MAINMENU ✘✔✘✘✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
            print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
            print('✔.To Mark Attendence of Today✍                         -PRESS(1)')
            print('✔.To Make Changes in Attendence✍                     -PRESS(2)')
            print('✘.To View Attendence of Cadets✍                         -PRESS(3)')
            print('✔.Enroll a New Cadet✍                                         -PRESS(4)')
            print('✘.TO Delete Attendance data✍                               -PRESS(5)')
            print('✘.To Exit ...                                              -PRESS(0)')
            input2=int(input('Enter your responce here✍: '))
            if input2==1:
                cursor=mycon.cursor()
                date=input('Enter Todays Date(DD_MM_YYYY)✍:')
                sub={'P':'Physics','C':'Chemistry','M':'Mathematics','E':'English','CS':'ComputerScience'}
                for i in sub.keys():
                    print(i,'-',sub[i])
                subcode=input('Enter your subjectCode✍:')
                subject=sub[subcode]
                if subject==sub['P']:
                    st="CREATE TABLE attendence (rollno int(5), "
                    qr=" VARCHAR(2))"
                    a=st+date+qr
                    cursor.execute(a)
                    cursor.execute("SELECT rollno FROM physics")
                    data=cursor.fetchall()
                    lst=[]
                    for i in data:
                        for j in i:
                            lst.append(j)
                    #print(lst)
                    for k in lst:
                        print("✍P-(Present) or A-(Absent) for the rollno-",k)
                        input123=input("Mark the attendence✍:")
                        st="INSERT INTO attendence(rollno,"
                        qr=") VALUES(%s,%s)"
                        values=(k,input123)
                        ask=st+date+qr
                        #print(ask)
                        cursor.execute(ask,values)
                        mycon.commit()
                    st="ALTER TABLE physics ADD COLUMN "
                    rt=" TINYINT UNSIGNED DEFAULT 0"
                    b=st+date+rt
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    st=" ALTER TABLE physics MODIFY "
                    tr=" VARCHAR(2)"
                    b=st+date+tr
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    ab="UPDATE physics t1 INNER JOIN attendence t2 ON t1.rollno=t2.rollno SET t1."
                    bc="=t2."
                    b=ab+date+bc+date
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    cursor.execute("DROP TABLE attendence")
                    mycon.commit()
                    ans=input("✔If you want to continue press-(y) or else press-(n):")
                    if ans=='y':
                        continue
                    else:
                        break
                elif subject==sub['C']:
                    st="CREATE TABLE attendence (rollno int(5), "
                    qr=" VARCHAR(2))"
                    a=st+date+qr
                    cursor.execute(a)
                    cursor.execute("SELECT rollno FROM chemistry")
                    data=cursor.fetchall()
                    lst=[]
                    for i in data:
                        for j in i:
                            lst.append(j)
                    #print(lst)
                    for k in lst:
                        print("✍P-(Present) or A-(Absent) for the rollno-",k)
                        input123=input("Mark the attendence✍:")
                        st="INSERT INTO attendence(rollno,"
                        qr=") VALUES(%s,%s)"
                        values=(k,input123)
                        ask=st+date+qr
                        #print(ask)
                        cursor.execute(ask,values)
                        mycon.commit()
                    st="ALTER TABLE chemistry ADD COLUMN "
                    rt=" TINYINT UNSIGNED DEFAULT 0"
                    b=st+date+rt
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    st=" ALTER TABLE chemistry MODIFY "
                    tr=" VARCHAR(2)"
                    b=st+date+tr
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    ab="UPDATE chemistry t1 INNER JOIN attendence t2 ON t1.rollno=t2.rollno SET t1."
                    bc="=t2."
                    b=ab+date+bc+date
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    cursor.execute("DROP TABLE attendence")
                    mycon.commit()
                    ans=input("✔If you want to continue press-(y) or else press-(n):")
                    if ans=='y':
                        continue
                    else:
                        break           
                elif subject==sub['E']:
                    st="CREATE TABLE attendence (rollno int(5), "
                    qr=" VARCHAR(2))"
                    a=st+date+qr
                    cursor.execute(a)
                    cursor.execute("SELECT rollno FROM english")
                    data=cursor.fetchall()
                    lst=[]
                    for i in data:
                        for j in i:
                            lst.append(j)
                    #print(lst)
                    for k in lst:
                        print("✍P-(Present) or A-(Absent) for the rollno-",k)
                        input123=input("Mark the attendence✍:")
                        st="INSERT INTO attendence(rollno,"
                        qr=") VALUES(%s,%s)"
                        values=(k,input123)
                        ask=st+date+qr
                        #print(ask)
                        cursor.execute(ask,values)
                        mycon.commit()
                    st="ALTER TABLE english ADD COLUMN "
                    rt=" TINYINT UNSIGNED DEFAULT 0"
                    b=st+date+rt
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    st=" ALTER TABLE english MODIFY "
                    tr=" VARCHAR(2)"
                    b=st+date+tr
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    ab="UPDATE english t1 INNER JOIN attendence t2 ON t1.rollno=t2.rollno SET t1."
                    bc="=t2."
                    b=ab+date+bc+date
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    cursor.execute("DROP TABLE attendence")
                    mycon.commit()
                    ans=input("✔If you want to continue press-(y) or else press-(n):")
                    if ans=='y':
                        continue
                    else:
                        break
                elif subject==sub['M']:
                    st="CREATE TABLE attendence (rollno int(5), "
                    qr=" VARCHAR(2))"
                    a=st+date+qr
                    cursor.execute(a)
                    cursor.execute("SELECT rollno FROM mathematics")
                    data=cursor.fetchall()
                    lst=[]
                    for i in data:
                        for j in i:
                            lst.append(j)
                    #print(lst)
                    for k in lst:
                        print("✍P-(Present) or A-(Absent) for the rollno-",k)
                        input123=input("Mark the attendence✍:")
                        st="INSERT INTO attendence(rollno,"
                        qr=") VALUES(%s,%s)"
                        values=(k,input123)
                        ask=st+date+qr
                        #print(ask)
                        cursor.execute(ask,values)
                        mycon.commit()
                    st="ALTER TABLE mathematics ADD COLUMN "
                    rt=" TINYINT UNSIGNED DEFAULT 0"
                    b=st+date+rt
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    st=" ALTER TABLE mathematics MODIFY "
                    tr=" VARCHAR(2)"
                    b=st+date+tr
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    ab="UPDATE mathematics t1 INNER JOIN attendence t2 ON t1.rollno=t2.rollno SET t1."
                    bc="=t2."
                    b=ab+date+bc+date
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    cursor.execute("DROP TABLE attendence")
                    mycon.commit()
                    ans=input("✔If you want to continue press-(y) or else press-(n):")
                    if ans=='y':
                        continue
                    else:
                        break
                elif subject==sub['CS']:
                    st="CREATE TABLE attendence (rollno int(5), "
                    qr=" VARCHAR(2))"
                    a=st+date+qr
                    cursor.execute(a)
                    cursor.execute("SELECT rollno FROM computerscience")
                    data=cursor.fetchall()
                    lst=[]
                    for i in data:
                        for j in i:
                            lst.append(j)
                    #print(lst)
                    for k in lst:
                        print("✍P-(Present) or A-(Absent) for the rollno-",k)
                        input123=input("Mark the attendence✍:")
                        st="INSERT INTO attendence(rollno,"
                        qr=") VALUES(%s,%s)"
                        values=(k,input123)
                        ask=st+date+qr
                        #print(ask)
                        cursor.execute(ask,values)
                        mycon.commit()
                    st="ALTER TABLE computerscience ADD COLUMN "
                    rt=" TINYINT UNSIGNED DEFAULT 0"
                    b=st+date+rt
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    st=" ALTER TABLE computerscience MODIFY "
                    tr=" VARCHAR(2)"
                    b=st+date+tr
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    ab="UPDATE computerscience t1 INNER JOIN attendence t2 ON t1.rollno=t2.rollno SET t1."
                    bc="=t2."
                    b=ab+date+bc+date
                    #print(b)
                    cursor.execute(b)
                    mycon.commit()
                    cursor.execute("DROP TABLE attendence")
                    mycon.commit()
                    ans=input("✔If you want to continue press-(y) or else press-(n):")
                    if ans=='y':
                        continue
                    else:
                        break
            if input2==2:
                cursor=mycon.cursor()
                print("✔To change attendance data✍            PRESS-(1)")
                print("✔To change users password✍            PRESS-(2)")
                print("✔To change details of the cadet✍       PRESS-(3)")
                b=int(input("Enter your responce here✍:"))
                if b==1:
                    sub={'P':'Physics','C':'Chemistry','M':'Mathematics','E':'English','CS':'ComputerScience'}
                    for i in sub.keys():
                        print(i,'-',sub[i])
                    subcode=input('Enter your subjectCode✍:')
                    subject=sub[subcode]
                    date=input('Enter The Date you want to change (DD_MM_YYYY):')
                    rollno=int(input("enter the rollno of the cadet✍:"))
                    attendance=input('Mark the updated attendance(P/A)✍:')
                    cursor=mycon.cursor()
                    ab="UPDATE "
                    bc=" SET "
                    cd="=%s"
                    de=" WHERE rollno=%s"
                    ask=ab+subject+bc+date+cd+de
                    #print(ask)
                    values=(attendance,rollno)
                    cursor.execute(ask,values)
                    mycon.commit()
                    ans=input("✔if you want to continue press-(y) or else press-(n)")
                    if ans=='y':
                        continue
                    else:
                        break
                if b==2:
                    username=input("enter your username✍:")
                    passwd=input("enter your new password✍:")
                    cursor=mycon.cursor()
                    ab="UPDATE login SET  passwd=%s WHERE uid=%s"
                    values=(passwd,username)
                    cursor.execute(ab,values)
                    mycon.commit()
                    ans=input("✔if you want to continue press-(y) or else press-(n)")
                    if ans=='y':
                        continue
                    else:
                        break
                if b==3:
                    rollno=int(input("enter the rollno of the cadet✍:"))
                    cursor=mycon.cursor()
                    st="SELECT * FROM details WHERE rollno=%s"
                    val=(rollno,)
                    cursor.execute(st,val)
                    data=cursor.fetchmany(1)
                    for i in data:
                        print(data)
                    print("Enter the updated details of the cadet below✍:")
                    name=input("Enter the name of the cadet✍:")
                    class1=int(input("enter the class✍-"))
                    section=input("enter the section✍:")
                    house=input("enter the house name✍:")
                    st="UPDATE details SET name=%s,class=%s,section=%s,house=%s WHERE rollno=%s"
                    val=(name,class1,section,house,rollno)
                    cursor.execute(st,val)
                    mycon.commit()
                    print("The updated details are:")
                    st="SELECT * FROM details WHERE rollno=%s"
                    val=(rollno,)
                    cursor.execute(st,val)
                    data=cursor.fetchmany(1)
                    for i in data:
                        print(data)
                    ans=input("✔if you want to continue press-(y) or else press-(n)")
                    if ans=='y':
                        continue
                    else:
                        break
            if input2==3:
                cursor=mycon.cursor()
                rollno=int(input("Enter the rollno of the cadet✍:"))
                sub={'P':'Physics','C':'Chemistry','M':'Mathematics','E':'English','CS':'ComputerScience'}
                for i in sub.keys():
                    lst=[]
                    m=0
                    n=0
                    a=(sub[i])
                    st="SELECT * FROM "
                    qr=" WHERE rollno=%s"
                    ask=st+a+qr
                    #print(ask)
                    val=(rollno,)
                    cursor.execute(ask,val)
                    data=cursor.fetchmany(1)
                    for i in data:
                        for j in i:
                            lst.append(j)
                    for k in lst:
                       if k=='P':
                           m=m+1
                       else:
                            n=n+1
                    print('✔SUBJECT:-',a)
                    print('✔total no.of periods:-',m+n)
                    print('✔toal no.of periods present:-',m)
                    print('✔total no.of periods absent:-',n)
                    print('✔Overall attendence percentage in the subject:-',(m/(m+n))*100,'%')
                ans=input("✔if you want to continue press-(y) or else press-(n)")
                if ans=='y':
                    continue
                else:
                    break
            if input2==4:
                cursor=mycon.cursor()
                rollno=int(input("enter the rollno. of the cadet✍:"))
                cursor.execute("SELECT rollno FROM details")
                data=cursor.fetchall()
                lst=[]
                for i in data:
                    for j in i:
                        lst.append(j)
                for k in lst:
                    if k==rollno:
                        print("This rollno already exists......Try again !")
                        ans=input("✔if you want to continue press-(y) or else press-(n)")
                        if ans=='y':
                            continue
                        else:
                            break
                else:
                    name=input("enter the name of the cadet✍:")
                    class1=int(input("enter the class✍:"))
                    section=input("enter the section✍:")
                    house=input("enter the house name✍:")
                    cursor.execute("INSERT INTO  details(rollno,name,class,section,house) VALUES({},'{}','{}','{}','{}')".format(rollno,name,class1,section,house))
                    mycon.commit()
                    sub={'P':'Physics','C':'Chemistry','M':'Mathematics','E':'English','CS':'ComputerScience'}
                    for i in sub.keys():
                        a=(sub[i])
                        ab="INSERT INTO "
                        bc="(rollno) VALUES(%s)"
                        val=(rollno,)
                        ask=ab+a+bc
                        cursor.execute(ask,val)
                        mycon.commit()
                print("Data inserted successfully...")    
                ans=input("✔if you want to continue press-(y) or else press-(n)")
                if ans=='y':
                    continue
                else:
                    break
            if input2==5:
                rollno=int(input("enter the rollno. of the cadet that you want to delete attendance data✍:"))
                cursor.execute("SELECT rollno FROM details")
                data=cursor.fetchall()
                lst=[]
                for i in data:
                    for j in i:
                        lst.append(j)
                #print(lst)
                for k in lst:
                    if k==rollno:
                        query="DELETE FROM details WHERE rollno={}".format(rollno)
                        cursor.execute(query)
                        mycon.commit()
                        print("Data deleted successfully...✔✔")
                        ans=input("✔if you want to continue press-(y) or else press-(n)")
                        if ans=='y':
                            continue
                        else:
                            break
                else:
                    print("This rolno. doesn't exists...! please try again.....")
                    ans=input("✔if you want to continue press-(y) or else press-(n)")
                    if ans=='y':
                        continue
                    else:
                        break
            else:
                print("Thank you......✔✔")
                break
