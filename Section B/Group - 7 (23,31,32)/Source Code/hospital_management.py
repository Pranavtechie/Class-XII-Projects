import mysql.connector as conn 
from prettytable import PrettyTable
from texttable import Texttable
#from datetime import datetime
#import time,calender
#import csv
global data

from os import system
mydb=conn.connect(host='localhost',
                  user='root',
                  password='student',
                  database='Hospital_Management')
if mydb.cursor:
      print('###### WELCOME TO THE HOSPITAL DATABASE MANAGEMENT #######')

#Function is for entering information into InPatient_Management table
def entryIPM():
      sl=input("Enter Slno:")
      pn=input("Enter the Patient Name:")
      pd=input("Enter Patient_ID:")
      se=input("Enter the Sex of the Patient:")
      ag=input("Enter the Age of the Patient:")
      il=input("Enter the Illness of the Patient:")
      cd=input("Enter the Name of the Doctor the Patient  is Consulting:")
      rn=input("Enter the Room no of the Patient:")
      da=input("Enter the Date of Admission of the Patient:")
      pa=input("Enter the Payment Amount:")
      data=(sl,pn,pd,se,ag,il,cd,rn,da,pa)
      sql='insert into InPatient_Management values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
      
      
      c=mydb.cursor()
      c.execute(sql,data)
      mydb.commit()
      print("------------------SUCCESSFULLY ENTERED!!!!!!----------------------")
      system("cls")
     

#Fuction to show InPatient_Management table
def showIPM():
      
      sql='select * from InPatient_Management;'
      c=mydb.cursor()
      c.execute(sql)
      data=c.fetchall()
      system("cls")
      t=PrettyTable(['Slno','Patient_Name','Patient_ID','Sex','Age','Illness',
               'Consulting_Doctor','Room_No','Date_of_Admission','Payment'])
      for i in data:
                  t.add_row(list(i))
      print(t)      

#Function is for entering information into OutPatient_Management table
def entryOPM():
      sl=input("Enter Slno:")
      pn=input("Enter the Patient Name:")
      pd=input("Enter Patient_ID:")
      se=input("Enter the Sex of the Patient:")
      ag=input("Enter the Age of the Patient:")
      il=input("Enter the Illness of the Patient:")
      dv=input("Enter the Date of Visit of the Patient:")
      pa=input("Enter the Payment Amount:")
      data=(sl,pn,pd,se,ag,il,dv,pa)
      sql='insert into OutPatient_Management values(%s,%s,%s,%s,%s,%s,%s,%s);'
      c=mydb.cursor()
      c.execute(sql,data)
      mydb.commit()
      print("------------------SUCCESSFULLY ENTERED!!!!!!----------------------")
      system("cls")

#Function is to show OutPatient_Management table
def showOPM():
      sql='select * from OutPatient_Management;'
      c=mydb.cursor()
      c.execute(sql)
      data=c.fetchall()
      system("cls")
      t=PrettyTable(['Slno','Patient_Name','Patient_ID','Sex','Age','Illness','Date_of_Visiting',
                     'Payment'])
      for i in data:
                  t.add_row(list(i))
      print(t)
      
#Function is to enter the information into the Doctor table
def entryDoctor():
      sl=input("Enter Slno:")
      dn=input("Enter the Doctor Name:")
      dd=input("Enter Doctor_ID:")
      se=input("Enter the Sex of the Doctor:")
      ag=input("Enter the Age of the Doctor:")
      da=input("Enter the Department of the Doctor:")
      ad=input("Enter the Days on which the Doctor is Available:")
      sa=input("Enter the Salary of the Doctor:")
      data=(sl,dn,dd,se,ag,da,ad,sa)
      sql='insert into Doctor values(%s,%s,%s,%s,%s,%s,%s,%s);'
      c=mydb.cursor()
      c.execute(sql,data)
      mydb.commit()
      print("------------------SUCCESSFULLY ENTERED!!!!!!----------------------")
      system("cls")
      
#Function to show Doctor table
def showDoctor():
      sql='select * from doctor;'
      c=mydb.cursor()
      c.execute(sql)
      data=c.fetchall()
      system("cls")
      t=PrettyTable(['Slno','Doctor_Name','Doctor_ID','Sex','Age','Department',
                     'Available_Days','Salary'])
      for i in data:
                  t.add_row(list(i))
      print(t)

#Fuction to enter information into pay table
def entrypay():
      sl=input("Enter SlNo:")
      PID=input("Enter patient ID:")
      Pn=input("Enter patient name:")
      kat=katta()
      ndo,SSC,med,ot,cost=kat
      data=(sl,PID,Pn,ndo,SSC,med,ot,cost)
      sql='insert into pay values(%s,%s,%s,%s,%s,%s,%s,%s);'
      c=mydb.cursor()
      c.execute(sql,data)
      mydb.commit()

def showpay():
      sql='select*from pay;'
      c=mydb.cursor()
      c.execute(sql)
      data=c.fetchall()
      system("cls")
      t=PrettyTable(['SlNo','Patient_ID','Patient_Name','Room_Rent','Scanning_Bill','Medicine_Charges','Other_Charges','Total_Payments'])
      for i in data:
                  t.add_row(list(i))
      print(t)
               
def entryMed():
      sl=input("Enter the SlNo:")
      mi=input("Enter medicine ID:")
      mn=input("Enter medicine name:")
      cost=input("Enter cost of medicine:")
      data=(sl,mi,mn,cost)
      sql='inset into medicine values(%s,%s,%s,%s);'
      c=mydb.cursor()
      c.execute(sql,data)
      mydb.commit()

def showmed():
      sql='select*from medicine;'
      c=mydb.cursor()
      c.execute(sql)
      data=c.fetchall()    
      system("cls")
      t=PrettyTable(['SlNo','Medicine_ID','Medicine_Name','Cost'])
      for i in data:
                  t.add_row(list(i))
      print(t)
               

def freakkan():
      med=0
      nm=int(input("Enter no. of medicine the patient has taken:"))
      l=0
      if (l<nm):
           mn=int(input("Enter the medicine code:"))
           cos=f'select cost from medicine where Medicine_ID = {mn}'
           c=mydb.cursor()
           c.execute(cos)
           zen=c.fetchall()
           cos=int(zen[0][0])
           med+=cos
           l+=1
      else:
           return med

def katta():
      global nd
      ad=input("Was the patient admitted (Y/N):")
      SC=input("Did the patient undergo scans(Y/N):")
      med=freakkan()
      cost=0
      if (ad.lower() =='y'):
            nd=int(input("For how many days was the patient admitted:"))
            IC=input("Was the patient in ICU(Y/N):")
            if (IC.lower() =='y'):
                 nc=int(input("For how days was the patient admitted in ICU:"))
                 nco=nc*3000
            nd=nd-nc
            ndo=(nd*1500)+nco
            cost+=ndo
      else:
                 cost+=0
      if (SC=='Y'):
            mr=input("Did the patient undergo MRI scan(Y/N):")
            ct=input("Did the patient undergo CT scan(Y/N):")
            us=input("Did the patient undergo Ultrasound scan(Y/N):")
            xr=input("Did the patient take X-Ray(Y/N):")
            SSC=0
            if (mr.lower() =='y'):  
                  SSC+=9000
            if (ct.lower() =='y'):
                  SSC+=4500
            if (us.lower() =='y'):
                  SSC+=2000
            if (xr.lower() =='y'):
                  SSC+=300
            cost+=SSC
      ot=int(input("Enter other charges:"))
      med = 0
      cont=0
      
      cont+=med

      ndo=(nd*1500)+nco
      SSC=0
      
      data=(ndo,SSC,med,ot,cost)
      return data
                   

#__mainfunction__
def main():
      system("cls")
      while(True):
           print("HOSPITAL MANAGEMENT SYSTEM")
           print("1:Add patient details")
           print("2:Show Inpatient details")
           print("3:Add outpatient details")
           print("4:Show outpatient details")
           print("5:Add doctor details")
           print("6:Show doctor details")
           print("7:Add payment details")
           print("8:Show payment details")
           print("9:show medicine")
           print("10:Exit")
           choice=int(input("\t PLEASE SELECT AN ABOVE OPTION:"))
           if (choice==1):
                 entryIPM()
           elif (choice==2):
                 showIPM()
           elif (choice==3):
                 entryOPM()
           elif (choice==4):
                 showOPM()
           elif (choice==5):
                 entryDoctor()
           elif (choice==6):
                 showDoctor()
           elif (choice==7):
                 entrypay()
           elif (choice==8):
                 showpay()
           elif (choice==9):
                 showmed()
           elif (choice==10):
                 break
           else:
                  print("-----!!!!Wrong choice!!!!!-----")
main()  #Main function call   
      

      
      



