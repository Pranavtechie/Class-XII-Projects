
import mysql.connector as sql
mycon = sql.connect(host = 'localhost',user = 'root',password = 'student',database = 'viswas')
mycon.commit()
if mycon.is_connected():
    print('Sucessfully connected to Mysql database')


print( '''..........⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄ ⚔ WELCOME ⚔ ⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄...........
..................... ⚓ Pioneer sports store ⚓ ......................
....................    Done by :1.D.Prasad     .....................
                                 2.S.Mukesh
                                 3.M.viswas''')

print(''' see below options and choose one of the below given options:
            press (1) to get the list of equipments present in the store.
            press (2) to pick the item you want to buy from the store. 
            press (3) to add new equipments or add.
            press (4) to complain about damaged equipments.
            press (5) to collect the reciept.
            press (6) to see customers history(only accesible by owners).
            press (7) to exit the program
            ''')
print()
while 1 :
    name = input('Enter your name for further proceedings (of exactly 4 to 10 lettters): ')

    print()
    limit_name = 14
    if len(name) > 14:
        print('Enter short name ')
        continue
    elif len(name) < 14:
        preceed = 14 - len(name)
        space = preceed*' '
        name = name+space
        #print(name)
        break
while True:
    inpt1 = int(input('Enter your choice from the above given list:'))
    print()
    if inpt1 == 1:
        mycursor = mycon.cursor()
        mycursor.execute('select * from sample')
        myresult = mycursor.fetchall()
        print()
        l = []
        for x in myresult:
            #print(x)
            l.append(x)
        #print(l)
        print("\tserial           sports        \t\t\tquantity\tprice","\n")
        for i in l:
            print("\t",i[0],"\t\t",i[1],"\t\t\t ",i[2],"\t\t",i[3],"\n")
        inpt2 = input('if you want to continue press Y: ')
        print()
        
        if inpt2 == 'y':
            print(''' see below options and choose one of the below given options:
                press (1) to get the list of equipments present in the store.
                press (2) to pick the item you want to buy from the store. 
                press (3) to add new equipments or add.
                press (4) to complain about damaged equipments.
                press (5) to collect the reciept.
                press (6) to see customers id(only accesible by owners).
                press (7) to exit the program
            ''')
            continue
        else:
            print("                              THANKING YOU                                ")
            print()
            print('''                                                         Contact numbers;
                                                                    Mobile Number(✆) :748596054
                                                                    Landline number(☎) :16273904''')
            break
    elif inpt1 == 2:
        mycursor = mycon.cursor()
        mycursor.execute('select * from sample')
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            #print(x)
            l.append(x)
        #print(l)
        print("\tserial\t\tsports\t\t\tquantity\tprice","\n")
        for i in l:
            print("\t",i[0],"\t\t",i[1],"\t\t",i[2],"\t\t",i[3],"\n")
        print("\n")
        inp = input('Tell the item you want buy: ')
        for j in range (0,len(l)):
            if inp == l[j][1]:
                p = int(input('Quantity you want to buy: '))
                x = l[j][2]
                k = x - p
                print()
                mycursor = mycon.cursor()
                sql = "update sample set quantity = {} where equip = '{}'".format(k,inp) 
                mycursor.execute(sql)
                mycon.commit()
                total = "select price  from sample where equip = '{}'".format(inp)
                mycursor.execute(total)
                myresult1 = mycursor.fetchone()
                #print(myresult1)
                mycursor.execute('select * from sample')
                myresult = mycursor.fetchall()
                print()
                l = []
                for x in myresult:
                    l.append(x)
                #print(l)
                print("\tserial\t\tsports\t\t\tquantity\tprice","\n")
                for i in l:
                    print("\t",i[0],"\t\t",i[1],"\t\t",i[2],"\t\t",i[3],"\n")
                print("\n")
                mycursor.execute('select * from customer')
                myresult = mycursor.fetchall()
                o = []
                for x in myresult:
                    o.append(x)
                cust = len(o)+1
                pric = p*myresult1[0]
                sql2 = "insert into customer values({},'{}','{}',{},{})".format(cust,
                                                                            name,inp,p,pric)
                mycursor.execute(sql2)
                mycon.commit()
        print()
        inpt3 = input('if you want to continue press y: ')
        if inpt3 == 'y':
            print(''' see below options and choose one of the below given options:
                press (1) to get the list of equipments present in the store.
                press (2) to pick the item you want to buy from the store. 
                press (3) to add new equipments or add.
                press (4) to complain about damaged equipments.
                press (5) to collect the reciept.
                press (6) to see customers id(only accesible by owners).
                press (7) to exit the program
            ''')
            continue
        else:
            name1 = input('Enter the name (the name which you given you bought): ')
            mycursor = mycon.cursor()
            mycursor.execute('select * from customer')
            myresult = mycursor.fetchall()
            #print("Total number of rows in sample is: ", mycursor.rowcount)
            o = []
            for x in myresult:
                #print(x)
                o.append(x)
            #print(o)
            for j in range (0,len(o)):
                if name1 == o[j][1]:
                    print('''        ......................RECIEPT............................
                                                                                  ''')
                    print("\t\tName:   ",name1)
                    print("\t\tITEM:    ",o[j][2])
                    print("\t\tQuantity:    ",o[j][3])
                    print("\t\tPRICE:    ",o[j][4])
                    print("\n")
            print()            
            print("                              THANKING YOU                                ")
            print()
            print('''                                                         Contact numbers;
                                                                    Mobile Number(✆) :748596054
                                                                    Landline number(☎) :16273904''')
            print()
            break
    elif inpt1 == 3:
        while 1:
            inp1 = input('Enter the item you want to add (of 6 to 11 letters): ')
            limit_item = 16
            if len(inp1) > 16:
                exceded = len(inp1) - 16
                lim = item[-1:exceded:-1]
                print('Shorten the name or cut ',lim)
                continue
            elif len(inp1) < 16:
                 preceed = 16 - len(inp1)
                 space = preceed*' '
                 name = name+space
                 print(inp1)
                 break
            print()
        
        quan = int(input('Enter the quantity you want to add: '))
        price = int(input('Enter the price of the item you want to add: '))
        mycursor = mycon.cursor()
        mycursor.execute('select * from sample')
        myresult = mycursor.fetchall()
        s = mycursor.rowcount
        serial = s + 1
        sql = "insert into sample values({},'{}',{},{})".format(serial,inp1,quan,price)
        mycursor.execute(sql)
        mycon.commit()
        mycursor.execute('select * from sample')
        myresult = mycursor.fetchall()
        #print("Total number of rows in sample is: ", mycursor.rowcount)
        l = []
        for x in myresult:
            l.append(x)
        print()
        print("\tserial\t\tsports\t\t\tquantity\tprice","\n")
        for i in l:
            print("\t",i[0],"\t\t",i[1],"\t\t",i[2],"\t\t",i[3],"\n")
        print("\n")        
        print()

        print()
        inpt4 = input('if you want to continue press Y: ')
        if inpt4 == 'y':
            print(''' see below options and choose one of the below given options:
                press (1) to get the list of equipments present in the store.
                press (2) to pick the item you want to buy from the store. 
                press (3) to add new equipments or add.
                press (4) to complain about damaged equipments.
                press (5) to collect the reciept.
                press (6) to see customers id(only accesible by owners).
                press (7) to exit the program
                  ''')            
            continue
        else:
            print("                              THANKING YOU                                ")
            print()
            print('''                                                         Contact numbers;
                                                                    Mobile Number(✆) :748596054
                                                                    Landline number(☎) :16273904''')
            break
    elif inpt1 == 4:
        equi = input("Enter the damaged item name: ")
        mycursor = mycon.cursor()
        mycursor.execute('select * from sample')
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            l.append(x)
        for j in range (0,len(l)):
            if equi == l[j][1]:
                quant = int(input("Enter the number of item damaged: "))
                k = l[j][2]
                x = k - quant
                sql = "update sample set quantity = {} where equip = '{}'".format(x,equi)
                mycursor.execute(sql)
                mycon.commit()
        mycursor.execute('select * from sample')
        myresult = mycursor.fetchall()
        l = []
        for x in myresult:
            l.append(x)
        print(l)
        print()
        print("\tserial\t\tsports\t\t\tquantity\tprice","\n")
        for i in l:
            print("\t",i[0],"\t\t",i[1],"\t\t",i[2],"\t\t",i[3],"\n")
        print("\n")
        print()

        print()
        inpt7 = input('if you want to continue press y: ')
        if inpt7 == 'y':
            print(''' see below options and choose one of the below given options:
                press (1) to get the list of equipments present in the store.
                press (2) to pick the item you want to buy from the store. 
                press (3) to add new equipments or add.
                press (4) to complain about damaged equipments.
                press (5) to collect the reciept.
                press (6) to see customers id(only accesible by owners).
                press (7) to exit the program
                   ''')            
            continue
        else:
            print("                              THANKING YOU                                ")
            print()
            print('''                                                         Contact numbers;
                                                                    Mobile Number(✆) :748596054
                                                                    Landline number(☎) :16273904''')
            break        
        
    elif inpt1 == 5:
        name1 = input('Enter the name (the name which you given you bought): ')
        mycursor = mycon.cursor()
        mycursor.execute('select * from customer')
        myresult = mycursor.fetchall()
        #print("Total number of rows in sample is: ", mycursor.rowcount)
        o = []
        for x in myresult:
            #print(x)
            o.append(x)
        #print(o)
        for j in range (0,len(o)):
            if name1 == o[j][1]:
                print('''        ......................RECIEPT............................
                                                                                  ''')
                print("\t\tName:   ",name1)
                print("\t\tITEM:    ",o[j][2])
                print("\t\tQuantity:    ",o[j][3])
                print("\t\tPRICE:    ",o[j][4])
                print("\n")
        print()
        
        print()
        inpt5 = input('if you want to continue press y: ')
        if inpt5 == 'y':
            print(''' see below options and choose one of the below given options:
                press (1) to get the list of equipments present in the store.
                press (2) to pick the item you want to buy from the store. 
                press (3) to add new equipments or add.
                press (4) to complain about damaged equipments.
                press (5) to collect the reciept.
                press (6) to see customers id(only accesible by owners).
                press (7) to exit the program
            ''')
            continue
        else:
            print("                              THANKING YOU                                ")
            print()
            print('''                                                         Contact numbers;
                                                                    Mobile Number(✆) :748596054
                                                                    Landline number(☎) :16273904''')
            break
    elif inpt1 == 6:
        inp3 = int(input('Enter your ID: '))
        mycursor = mycon.cursor()
        mycursor.execute('select * from owner')
        myresult = mycursor.fetchall()
        #print("Total number of rows in sample is: ", mycursor.rowcount)
        print()
        l = []
        for x in myresult:
            #print(x)
            l.append(x)
        #print(l)
        for j in l:
            m = l[0]
            if inp3 == m[0]:
                mycursor = mycon.cursor()
                mycursor.execute('select * from customer')
                myresult = mycursor.fetchall()
                o = []
                for x in myresult:
                    #print(x)
                    o.append(x)
                #print(o)
        print("         serial\t    name                 item\t\t  quantity\t price","\n")
        for i in o:
            print("\t",i[0],"\t   ",i[1],"\t\t",i[2],"\t ",i[3],"\t\t",i[4],"\n")
        print("\n")        
        print()
        
        print()
        inpt6 = input('If you want to continue press y: ')
        if inpt6 == 'y':
            print(''' see below options and choose one of the below given options:
                press (1) to get the list of equipments present in the store.
                press (2) to pick the item you want to buy from the store. 
                press (3) to add new equipments or add.
                press (4) to complain about damaged equipments.
                press (5) to collect the reciept.
                press (6) to see customers id(only accesible by owners).
                press (7) to exit the program
            ''')
            
            continue
        else:
            print("                              THANKING YOU                                ")
            print()
            print('''                                                         Contact numbers;
                                                                    Mobile Number(✆) :748596054
                                                                    Landline number(☎) :16273904''')
            break
    elif inpt1 == 7:
        print("                              THANKING YOU                                ")
        print()
        print('''                                                         Contact numbers;
                                                                    Mobile Number(✆) :748596054
                                                                    Landline number(☎) :16273904''')
        break
        
    else:
        print('YOU HAVE ENTERED THE WRONG CHOICE')
        print()
        print("                              THANKING YOU                                ")
        print()
        print('''                                                         Contact numbers;
                                                                    Mobile Number(✆) :748596054
                                                                    Landline number(☎) :16273904''')
        break

    
    
        
        
        
