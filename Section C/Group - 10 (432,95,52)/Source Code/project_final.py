#THIS PROGRAM WAS DEVELOPED BY  B.THIRUMALESWAR REDDY(432), RAM CHARAN(95), VISHNU(52)
from tabulate import tabulate
from colorama import init
from termcolor import colored
init()
import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',password='student',database='project')
cursor=mydb.cursor()
co='★'
unco='☆'

#TO CREATE THE ACCOUNT IN PROGRAM
print('FOR SEEING THE DETAILS YOU NEED TO HAVE AN ACCOUNT')
po='t'
while po == 't':
    option=input('''
             ____________                              ___________
            !            !                            !           !
            !  REGISTER  !                            ! LOGIN IN  !
            !____________!                            !___________!
      
          FOR REGISTERING  PRESS  -- (R)
          FOR LOGING IN PRESS -- (L)
           
        
    ''')
    ni='t'
    if option=='R':
        first_name=input('FIRST NAME : ')
        second_name=input('SECOND NAME : ')
        name=first_name +' '+ second_name
        username=input('USERNAME : ')
        while username[-1:-11:-1]!='moc.liamg@':
            print('DOMAIN OF THE USERNAME SHOULD BE (@gmail.com)')
            username=input('USERNAME : ')
        password=input('PASSWORD : ')
        while password.isalpha() or password.isdigit() or password=='':
            print('PASSWORD SHOULD CONTAIN BOTH ALPHABETS AND NUMBERS')
            password=input('PASSWORD : ')
        age=int(input('AGE : '))
        gender=input('GENDER(M/F) : ')
        print('YOUR ACCOUNT IS BEEN SUCESSFULLY CREATED ')
        ni='k'
        store_sql=f'insert into register values("{name}","{username}","{password}",{age},"{gender}")'
        cursor.execute(store_sql)
        mydb.commit()
    while ni=='k' or option=='L':
        sst=f'select * from register'
        cursor.execute(sst)
        tst=cursor.fetchall()
        print('''

                        LOG  IN 
        ''')
        R=input('USERNAME : ')
        while R[-1:-11:-1]!='moc.liamg@':
            print('DOMAIN OF THE USERNAME SHOULD BE (@gmail.com)')
            R=input('USERNAME : ')
        T=input('PASSWORD : ')
        w='x'
        d=0
        while w=='x':
            if d== len(tst):
                print('Account has not been registered')
                print('FOR SEEING THE DETAILS YOU NEED TO HAVE AN ACCOUNT')
                w='exit'
                z='exit'
                ni='exit'
                option='exit'
            else:
                usernamex=tst[d][1]
                passx=tst[d][2]
                namex=tst[d][0]
                if R == usernamex:
                    if T == passx:
                        print('login was sucessful')
                        w='exit'
                        z='t'
                    else:
                        print('wrong password')
                        print('you have 3 more attempts')
                        attempts=3
                        while attempts > 0:
                            T=input('PASSWORD : ')
                            if T == passx:
                                print('login was sucessful')
                                w='exit'
                                z='t'
                                break
                            attempts=attempts-1
                            print('wrong password')
                            print('you have',attempts,'attempts')
                        else:
                            print('FOR SEEING THE DETAILS YOU NEED TO HAVE AN ACCOUNT')
                            w='exit'
                            z='exit'
                            ni='exit'
                            option='exit'
                            
            d=d+1           
        while z=='t':
            #HEADING OF THE PROGRAM
            namef=colored(namex,'red')
            des=colored('   ⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜','yellow')
            des1=colored('⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜⚜','yellow')
            head=colored('SAINIK SCHOOL KALIKIRI','white','on_blue')
            des2=colored('⚛⚛⚛⚛⚛⚛⚛⚛⚛⚛⚛⚛','green')
            des3=colored('⚛⚛⚛⚛⚛⚛⚛⚛⚛⚛⚛⚛','green')
            print('\t  ',des,head,des1)
            print('\t\t',des2,'WELCOME ',namef,' TO TOLLYWOOD INFO',des3,'\n','\n'
            ' ---> You Can See All Types Of Info About Movies,actors In This Program')
            #MAIN MENU OF THE PROGRAM
            print('''
                    __________________
                   ! ϟ                !
                   ! (a)  MOVIES      !
                   ! (b)  HEROS       !
                   ! (c)  EXIT        ! 
                   !_ϟ________________!
            ''')
            inp=input('ENTER THE CORRESPOINDING VALUES IN THE MENU TO SEE THE INFO:')
            o='t'
            while o=='t':
                if inp=='a':
                    #SUB MENU OF THE PROGRAM
                    print('''
                    ____________________
                   ! ϟ                  !
                   ! (A)  ABOUT         !
                   ! (B)  IMDB INFO     !
                   ! (C)  USER RATING   !
                   ! (D)  ADD MOVIE     !
                   ! (E)  DELETE MOVIE  !
                   ! (F)  ALL INFO      !
                   ! (G)  BACK          !
                   ! (H)  EXIT          !
                   !_ϟ__________________!      

                    ''')
                    inp1=input('ENTER THE CORRESPOINDING VALUES IN THE MENU TO SEE THE INFO:')
                    if inp1=='A':
                        #INPUT FROM THE USER 
                        movie=input('ENTER THE MOVIE NAME : ')
                        sss=f'select * from movies'
                        cursor.execute(sss)
                        ttt=cursor.fetchall()
                        yt=0
                        io='t'
                        while io=='t':
                            if yt==len(ttt):
                                print('THE ENTERED MOVIE DOES NOT EXIST')
                                io='exit'
                            else:
                                moviex=ttt[yt][0]
                                if movie==moviex:
                                    herox=ttt[yt][1]
                                    heroinex=ttt[yt][2]                                    
                                    directorx=ttt[yt][3]
                                    yearx=ttt[yt][4]
                                    print('HERO : ',herox)
                                    print('HEROINE : ',heroinex)
                                    print('DIRECTOR : ',directorx)
                                    print('RELEASED YEAR : ',yearx)
                                    io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no): ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                   
                    elif inp1=='B':
                        movie=input('ENTER THE MOVIE NAME')
                        ll=f'select * from movies'
                        cursor.execute(ll)
                        kk=cursor.fetchall()
                        yt=0
                        io='t'
                        while io=='t':
                            if yt==len(kk):
                                print('THE ENTERED MOVIE DOES NOT EXIST')
                                io='exit'
                            else:
                                moviex=kk[yt][0]
                                if movie==moviex:
                                    ratingx=kk[yt][5]
                                    votersx=kk[yt][6]
                                    print('''
                                    -----------IMDB INFO----------
                                    RATING : ''',ratingx,'''
                                    NO OF VOTERS: ''' ,votersx)
                                    io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no): ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                        
                    elif inp1=='C':
                        movie=input('ENTER THE MOVIE NAME YOU LIKE RATE : ')
                        el=f'select * from movies'
                        cursor.execute(el)
                        kk=cursor.fetchall()
                        yt=0
                        io='t'
                        while io=='t':
                            if yt==len(kk):
                                print('THE ENTERED MOVIE DOES NOT EXIST')
                                io='exit'
                            else:
                                moviex=kk[yt][0]
                                if movie==moviex:
                                    ratingu=eval(input('ENTER YOUR RATING: '))
                                    ratingx=kk[yt][5]
                                    votersx=kk[yt][6]
                                    rate=(ratingx*votersx)+ratingu
                                    rate1=rate/(votersx+1)
                                    su=ratingx/2
                                    sui=int(su)
                                    xo=str(su)
                                    sud=''
                                    for k in range(0,len(xo)):
                                        if xo[k]=='.':
                                            sud+=xo[k+1]            
                                    sud=int(sud)
                                    if sud in [1,2,3,4,5]:
                                        b=unco
                                    elif sud in [6,7,8,9]:
                                        b=co
                                    fo=int(5-su)
                                    a=co*sui
                                    c=unco*fo
                                    sa=a+b+c
                                    ratingx=su*2
                                    rai=int(ratingx)
                                    s=str(ratingx)
                                    rad=''
                                    for l in range(0,len(s)):
                                        if s[l]=='.':
                                            rad+=s[l+1]
                                    rad=int(rad)
                                    tot=str(rai)+'.'+str(rad)
                                    votersx+=1
                                    print('\n','\t\t\t',sa,'[',su,'/','5]')
                                    print('\t\t\t rating of the movie :',tot)
                                    print('\t\t\t no of voters :',votersx)
                                    ex=f'update movies set rating={tot},no_of_voters={votersx} where movie_name="{movie}"'
                                    cursor.execute(ex)
                                    mydb.commit()
                                    io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no) : ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                                                            
                    elif inp1 == 'D':
                        movie=input('ENTER THE MOVIE NAME :')
                        aa=f'select * from movies'
                        cursor.execute(aa)
                        kk=cursor.fetchall()
                        yt=0
                        io='t'
                        while io == 't':
                            if yt== len(kk):
                                hero_name=input('ENTER THE HERO NAME : ')
                                heroine_name=input('ENTER THE HEROINE NAME : ')
                                director_name=input('ENTER THE DIRECTOR NAME : ')
                                released_year=eval(input('ENTER THE RELEASED YEAR : '))
                                rating=eval(input('ENTER THE RATING : '))
                                voters=int(input('ENTER THE NO OF VOTERS : '))
                                ex=f'insert into movies values("{movie}","{hero_name}","{heroine_name}","{director_name}",{released_year},{rating},{voters})'
                                cursor.execute(ex)
                                mydb.commit()
                                io='exit'
                            else:
                                moviex=kk[yt][0]
                                if movie==moviex:
                                    print('ENTERED MOVIE ALREADY EXISTS')
                                    lo=input('would you like to edit the deatils of the movie(yes/no) : ')
                                    if lo=='yes' or lo=='Yes' or lo=='YES':
                                        hero_name=input('ENTER THE HERO NAME : ')
                                        heroine_name=input('ENTER THE HEROINE NAME : ')
                                        director_name=input('ENTER THE DIRECTOR NAME : ')
                                        released_year=eval(input('ENTER THE RELEASED YEAR : '))
                                        rating=eval(input('ENTER THE RATING : '))
                                        voters=int(input('ENTER THE NO OF VOTERS : '))
                                        ex=f'update movies set hero_name="{hero_name}",heroine_name="{heroine_name}",director_name="{director_name}",released_year={released_year},rating={rating},no of voters={voters} where movie_name="{movie}"'
                                        cursor.execute(ex)
                                        mydb.commit()
                                        io='exit'
                                    else:
                                        io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no) : ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                            
                    elif inp1 == 'E':
                        movie=input('ENTER THE MOVIE NAME YOU WOULD LIKE TO DELETE :')
                        nn=f'select * from movies'
                        cursor.execute(nn)
                        ko=cursor.fetchall()
                        yt=0
                        io='t'
                        while io=='t':
                            if yt==len(ko):
                                print('THE ENTERED MOVIE DOES NOT EXIST')
                                io='exit'
                            else:
                                moviex=ko[yt][0]
                                if movie==moviex:
                                    de=f'delete from movies where movie_name="{movie}"'
                                    print('the movie and details are sucessfully deleted')
                                    io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no): ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))

                    elif inp1=='F':
                        #TO SEE ALL THE INFO
                        info=f'select * from movies'
                        cursor.execute(info)
                        ok=cursor.fetchall()                        
                        print(tabulate(ok,headers=["MOVIE","HERO","HEROINE","DIRECTOR","YEAR","RATING","VOTERS"]))                             
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no) : ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                            z='t'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                            
                    elif inp1=='G':
                        #TO GO BACK
                        o='exit'
                    elif inp1=='H':
                        #TO EXIT 
                        o='exit'
                        z='exit'
                        po='exit'
                        ni='exit'
                        option='exit'
                        print('\t\t\t',end='')
                        print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                    else:
                        #CHECKING THE CORRECT OPTION
                        o='t'
                        print('-----> ENTER THE CORRECT OPTION <-----')
                        
                elif inp=='b':
                    #SUB MENU FOR HEROES
                    print('''
                    _____________________
                   ! ϟ                   !
                   ! (A)  PERSONAL INFO  !
                   ! (B)  MOVIE CARIER   !
                   ! (C)  ADD HEROS      !
                   ! (D)  DELETE HEROS   !
                   ! (E)  ALL INFO       !
                   ! (F)  BACK           !
                   ! (G)  EXIT           !
                   !_ϟ___________________! 
                    ''')
                    inp3=input('ENTER THE CORRESPONDING VALUES TO SEE THE DETAILS :')
                    if inp3=='A':
                        hero=input('ENTER THE HERO NAME OF WHOM YOU WANT TO SEE THE INFO')
                        yu=f'select * from heros'
                        cursor.execute(yu)
                        tt=cursor.fetchall()
                        yt=0
                        io='t'
                        while io=='t':
                            if yt==len(tt):
                                print('THE ENTERED HERO NAME DOES NOT EXIST')
                                io='exit'
                            else:
                                herox=tt[yt][0]
                                if hero==herox:
                                    wifex=tt[yt][1]
                                    fatherx=tt[yt][2]                                    
                                    motherx=tt[yt][3]
                                    agex=tt[yt][4]
                                    print('WIFE : ',wifex)
                                    print('FATHER : ',fatherx)
                                    print('MOTHER : ',motherx)
                                    print('AGE : ',agex)
                                    io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no): ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                            
                    elif inp3=='B':
                        hero=input('ENTER THE HERO NAME')
                        ku=f'select * from heros'
                        cursor.execute(ku)
                        pp=cursor.fetchall()
                        yt=0
                        io='t'
                        while io=='t':
                            if yt==len(pp):
                                print('THE ENTERED HERO NAME DOES NOT EXIST')
                                io='exit'
                            else:
                                herox=pp[yt][0]
                                if hero==herox:
                                    awardsx=pp[yt][5]
                                    best_moviex=pp[yt][6]
                                    no_of_moviesx=pp[yt][7]
                                    experencex=pp[yt][8]
                                    print('NO_OF_AWARDS : ',awardsx)
                                    print('BEST_MOVIE : ',best_moviex)
                                    print('NO_OF_MOVIES : ',no_of_moviesx)
                                    print('EXPERIENCE : ',experencex)
                                    io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no): ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                        
                    elif inp3 == 'C':
                        hero=input('ENTER THE HERO NAME :')
                        aa=f'select * from heros'
                        cursor.execute(aa)
                        kk=cursor.fetchall()
                        yt=0
                        io='t'
                        while io == 't':
                            if yt== len(kk):
                                wife=input('WIFE NAME : ')
                                father=input('FATHER NAME : ')
                                mother=input('MOTHER NAME : ')
                                age=eval(input('AGE : '))
                                awards=eval(input('AWARDS : '))
                                best_movie=input('BEST MOVIE : ')
                                movies=int(input('NO OF MOVIES : '))
                                experience=int(input('EXPERIENCE : '))
                                ex=f'insert into heros values("{hero}","{wife}","{father}","{mother}",{age},{awards},"{best_movie}",{movies},{experience})'
                                cursor.execute(ex)
                                mydb.commit()
                                io='exit'
                            else:
                                herox=kk[yt][0]
                                if hero==herox:
                                    print('ENTERED HEROs NAME ALREADY EXISTS')
                                    lo=input('would you like to edit the deatils of the hero(yes/no) : ')
                                    if lo=='yes' or lo=='Yes' or lo=='YES':
                                        wife=input('WIFE NAME : ')
                                        father=input('FATHER NAME : ')
                                        mother=input('MOTHER NAME : ')
                                        age=eval(input('AGE : '))
                                        awards=eval(input('AWARDS : '))
                                        best_movie=input('BEST MOVIE : ')
                                        movies=int(input('NO OF MOVIES : '))
                                        experience=int(input('EXPERIENCE : '))
                                        ex=f'update heros set hero_name="{hero}",wife_name="{wife}",father_name="{father}",mother_name="{mother}",age={age},awards={awards},best_movie="{best_movie}",no_of_movies={movies},experience={experience}'
                                        cursor.execute(ex)
                                        mydb.commit()
                                        io='exit'
                                    else:
                                        io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no) : ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                        
                    elif inp3 == 'D':
                        hero=input('ENTER THE HERO NAME YOU WOULD LIKE TO DELETE :')
                        #DELETING THE MOVIE
                        nn=f'select * from heros'
                        cursor.execute(nn)
                        ko=cursor.fetchall()
                        yt=0
                        io='t'
                        while io=='t':
                            if yt==len(ko):
                                print('THE ENTERED HEROS_NAME DOES NOT EXIST')
                                io='exit'
                            else:
                                herox=ko[yt][0]
                                if hero==herox:
                                    de=f'delete from heros where hero_name="{hero}"'
                                    print('the heros details are sucessfully deleted')
                                    io='exit'
                            yt+=1
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no): ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                       
                    elif inp3 == 'E':
                        #TO SEE ALL THE DETAILS OF THE HEROES
                        info=f'select hero_name,wife_name,age,awards,best_movie,no_of_movies,experience from heros'
                        cursor.execute(info)
                        ok=cursor.fetchall()                        
                        print(tabulate(ok,headers=["HERO","WIFE","AGE","AWARDS","BEST MOVIE","NO OF MOVIES","EXPERIENCE"])) 
                        cont=input('WOULD YOU LIKE TO COTINUE THE PROGRAM (yes/no) : ')
                        if cont=='yes' or cont=='Yes' or cont=='YES':
                            o='exit'
                            z='t'
                        else:
                            o='exit'
                            z='exit'
                            po='exit'
                            ni='exit'
                            option='exit'
                            print('\t\t\t',end='')
                            print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                    
                    elif inp3=='F':
                        #TO GO BACK
                        o='exit'
                    elif inp3=='G':
                        # TO EXIT
                        o='exit'
                        z='exit'
                        po='exit'
                        ni='exit'
                        option='exit'
                        print('\t\t\t',end='')
                        print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                    else:
                        #CHECKING THE OPTION
                        print('-----> ENTER THE CORRECT OPTION <-----')
                elif inp=='c':
                    #TO EXIT FROM THE PROGRAM
                    o='exit'
                    z='exit'
                    po='exit'
                    ni='exit'
                    option='exit'
                    print('\t\t\t',end='')
                    print(colored('THANK YOU FOR USING OUR PROGRAM','white','on_blue'))
                    
                else:
                    #CHECKING OPTION
                    o='exit'
                    print('-----> ENTER THE CORRECT OPTION <-----')
                    
    if option not in ['R','L'] and ni!='exit':
        #CHECKING OPTION
        print('-----> ENTER THE CORRECT OPTION <-----')   
