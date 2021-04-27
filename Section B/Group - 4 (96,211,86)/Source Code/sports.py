import mysql.connector as m
from prettytable import PrettyTable
con = m.connect (host = 'localhost', user = 'root', password = 'student')
cur = con.cursor()
cur.execute('create database if not exists sports')
cur.execute('use sports')
cur.execute('create table if not exists issue(itemno varchar(10) primary key,itemname varchar(150),issuedto varchar(50),rollno int(20),house varchar(30))')
cur.execute('create table if not exists winners(year int(10) primary key,godavari int(10),krishna int(10),penna int(10),tungabhadra int(10))')
con.commit()
print('#'*95)
print('                   WELCOME TO THE DATABASE OF SPORTS OF SSKAL ')
print('#'*95)


while True:
    print('1.Sports items record')
    print('2.Winners record')
    print('3.How to play')
    print('4.Exit')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        print('Here you can find the record of items available at SSKAL')
        print('1.Add record')
        print('2.Display record')
        print('3.Delete record')
        print('4.Exit')
        choice = int(input('Enter your choice:'))
        if choice == 1:
            itemno = input('Enter item number: ')
            itemname = input('Enter item name: ')
            issuedto = input('Enter issued to cadet(name): ')
            rollno = int(input('Enter roll no of cadet: '))
            house = input('Enter house name : ')
            query0 = "insert into issue values('{}','{}','{}',{},'{}')".format(itemno,itemname,issuedto,rollno,house)
            try:
                cur.execute(query0)
                con.commit()
                print('Data added successfully.')
            except m.Error as err:
                print('The following error occured')
                print(err)
        elif choice == 2:
            query1 = "select * from issue "
            try:
                cur.execute(query1)
                result = cur.fetchall()
                t = PrettyTable(['itemno','itemname','issuedto','rollno','house'])
                for i in result:
                    t.add_row(i)
                print(t)
            except m.Error as err:
                print('The following error occured.')
                print(err)
   
        

        elif choice == 3:
            delete = int(input('Enter the item number to delete: '))
            query5 = "delete from issue where itemno = {}".format(delete)
            cur.execute(query5)
            con.commit()
            print('Record deleted successfully')


        elif choice == 4:
            con.close()
            print('*'*40,' Thank you ','*'*40)
            break
        
        else:
            print('Invalid choice!!!')
        
    elif choice == 2:
        print('Here you can find the data about winners of interhouse competitons of respective years.')
        print('1.Add record')
        print('2.Display record')
        print('3.Update record')
        print('4.Delete record')
        print('5.Exit')
        choice = int(input('Enter your choice:'))
        if choice == 1:
            year = int(input('Enter the year: '))
            godavari = int(input('Enter the no of trophies won by godavari: '))
            krishna = int(input('Enter the no of trophies won by krishna: '))
            penna = int(input('Enter the no of trophies won by penna: '))
            tungabhadra = int(input('Enter the no of trophies won by tungabhadra: '))
            query0 = "insert into winners values({},{},{},{},{})".format(year,godavari,krishna,penna,tungabhadra)
            try:
                cur.execute(query0)
                con.commit()
                print('Data added successfully.')
            except m.Error as err:
                print('The following error occured')
                print(err)
        elif choice == 2:
            query1 = "select * from winners "
            try:
                cur.execute(query1)
                result = cur.fetchall()
                t = PrettyTable(['year','godavari','krishna','penna','tungabhadra'])
                for i in result:
                    t.add_row(i)
                print(t)
            except m.Error as err:
                print('The following error occured.')
                print(err)
   
        elif choice == 3:
            year = int(input("Enter the year to update: "))
            query3 = "select * from winners where year = {}".format(year)
            cur.execute(query3)
            result = cur.fetchall()
            if cur.rowcount == 0:
                print('No record found')
            else:
                house = input('Enter the house name: ')
                no_of_trophy = int(input("Enter the no of trophies to update : "))
                cur.execute(f"update winners set {house} = {no_of_trophy} where year = {year}")
                con.commit()
                print('Updated successfully')

        elif choice == 4:
            delete = int(input('Enter the year to delete: '))
            query5 = "delete from winners where year = {}".format(delete)
            cur.execute(query5)
            con.commit()
            print('Record deleted successfully')

        elif choice == 5:
            con.close()
            print('*'*40,' Thank you ','*'*40)
            break
        
        else:
            print('Invalid choice!!!')

    elif choice == 3:
        
        print('1.Basket ball')
        print('2.Badminton')
        print('3.Cricket')
        print('4.Chess')
        print('5.Football')
        print('6.Hockey')
        print('7.Volleyball')
        print('8.Table tennis')
        print('9.Exit')
        choice = int(input('Enter your choice: '))
        ###1 Basket ball
        if choice == 1:
            print('''>>The game is played between 24 players. (i.e. Two teams)
In a team 5 players are main players and 7 players are substitute.
                 
>>The primary objective is shooting a basketball through the
defender's hoop in diameter mounted 10 feet high to a backboard at
each end of the court while preventing the opposing team from
shooting through their own hoop.
                 
>>The basic points given for each basket is 2,unless basket is
scored from behind of three pointer line.
                 
>>After a foul, timed play stops and the player fouled or
designated to shoot a technical foul is given one, two or three
one-point free throws.
                 ''')
    


        ###2 Badminton
        elif choice == 2:
            
            print('''>>The game is played between 2 players.

>>Badminton is a racquet sport played using racquets to hit
a shuttlecock across a net. 
                 
>>Points are scored by striking the shuttlecock with the racquet
and landing it within the opposing side's half of the court.
                 
>>Each side may only strike the shuttlecock once before it passes
over the net. Play ends once the shuttlecock has struck the floor
or if a fault has been called by the umpire, service judge, or
(in their absence) the opposing side.
                 
                 ''')
    

        ###3 Cricket
        elif choice == 3:
            
             print('''>>The game is played between 32 players. (i.e. Two teams)
In a team 11 players are main players and 5 players are substitute.
                 
>>Cricket is a bat-and-ball game played between two teams of eleven
players on a field at the centre of which is a 22-yard (20-metre)
pitch with a wicket at each end, each comprising two bails balanced
on three stumps.
                 
>> The batting side scores runs by striking the ball bowled at the
wicket with the bat (and running between the wickets), while the
bowling and fielding side tries to prevent this by preventing
the ball from leaving the field, and getting the ball to either wicket
and dismiss each batter (so they are "out").                 
                 
>> Means of dismissal include being bowled, when the ball hits the
stumps and dislodges the bails, and by the fielding side either
catching the ball after it is hit by the bat and before it hits the
ground, or hitting a wicket with the ball before a batter can cross
the crease in front of the wicket.
                 
>>The game is adjudicated by two umpires, aided by a third umpire
and match referee in international matches.''')
    


        ###4 Chess
        elif choice == 4:
            print('''>>The game is played between 2 players. 
                 
>>Chess is an abstract strategy game and involves no hidden information.
It is played on a square chessboard with 64 squares arranged in an
eight-by-eight grid. 
                 
>>The object of the game is to checkmate the opponent's king, whereby
the king is under immediate attack (in "check") and there is no way to
remove it from attack on the next move. 
                 
>> At the start, each player (one controlling the white pieces, the
other controlling the black pieces) controls sixteen pieces:
one king, one queen, two rooks, two knights, two bishops, and eight pawns.                 ''')
    
    

        ###5 Football
        elif choice == 5:
    
            print('''>>The game is played between 32 players. (i.e. Two teams)
In a team 11 players are main players and 5 players are substitute.
                 
>>Football is a family of team sports that involve, to varying
degrees, kicking a ball to score a goal.
                 
>>After a foul, timed play stops and the player fouled or
designated to shoot a technical foul is given red or yellow card.''')
    


        ###6 Hockey
        elif choice == 6:
    
            print('''>>The game is played between 32 players. (i.e. Two teams)
In a team 11 players are main players and 5 players are substitute.
                 
>>Hockey is a sport in which two teams play against each other by
trying to manoeuvre a ball or a puck into the opponent's goal
using a hockey stick.
                 
>>There are many types of hockey such as bandy, field hockey,
ice hockey and rink hockey.''')
        
    


        ###7 Volleyball
        elif choice == 7:
    
            print('''>>The game is played between 24 players. (i.e. Two teams)
In a team 6 players are main players and 6 players are substitute.
                 
>>Each team tries to score points by grounding a ball on the other
team's court under organized rules.
                 
>>The ball is usually played with the hands or arms, but players
can legally strike or push (short contact) the ball with any part
of the body.''')
        
    


        ###8 Table tennis
        elif choice == 8:
   
            print('''>>The game is played between 2 or 4 players. (i.e. Two teams)
In a team  1 or 2(For doubles team) players are main players.
                 
>>Table tennis is a sport in which two or four players hit a
lightweight ball back and forth across a table using small rackets.
                 
                 ''')

        elif choice == 9:
            print('*'*40,' Thank you ','*'*40)
            break

    elif choice == 4:
        print('*'*40,' Thank you ','*'*40)
        break
        
    else:
        print('Invalid choice!!!')

    








