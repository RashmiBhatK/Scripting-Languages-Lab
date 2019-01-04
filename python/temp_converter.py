'''1)Introduction to Python Functions: Write a temperature converter python program, which is
menu driven. Each such conversion logic should be defined in separate functions. The program
should call the respective function based on the user’s requirement. The program should run
as long as the user wishes so. Provide an option to view the conversions stored as list of tuples
with attributes - from unit value, to unit value sorted by the user’s choice (from-value or
to-value).'''



import datetime
import time
from datetime import datetime
from operator import itemgetter

records=()
record=()
details=()
records=list(records)


def c_to_k():

  temp=float(input("enter the temperature in celsius"));
  converted=temp+273.15
  dt=date_time()
  print("the temperature in kelvin: ",converted)
  details=("Celsius",temp,"Kelvin",converted,str(dt))
  insert_tuple(records,details)


def c_to_f():

  temp=float(input("enter the temperature in celsius"));
  converted=(temp*1.8)+32
  dt=date_time()
  print("the temperature in faherhiet: ",converted)
  details=("Celsius",temp,"faherhiet",converted,str(dt))
  insert_tuple(records,details)


def f_to_c():

  temp=float(input("enter the temperature in faherhiet"));
  converted=(temp-32)/1.8
  dt=date_time()
  print("the temperature in Celsius: ",converted)
  details=("faherhiet",temp,"Celsius",converted,str(dt))
  insert_tuple(records,details)


def k_to_c():

  temp=float(input("enter the temperature in kelvin"));
  converted=temp-273.15
  dt=date_time()
  print("the temperature in Celsius: ",converted)
  details=("kelvin",temp,"Celsius",converted,str(dt))
  insert_tuple(records,details)


def date_time():

  dt=datetime.now()
  return dt



def insert_tuple(records,details):

  records.append(details)
  return records


def view_conversion():

 print("TO VIEW :\n1.from-value\n2.To-value\n3.date")
 x=int(input(">>>"))
 if(x==1):
  record=sorted(records,key=itemgetter(1))
  print(record)
 elif(x==2):
  record=sorted(records,key=itemgetter(3))
  print(record)
 elif(x==3):
  record=sorted(records,key=itemgetter(4))
  print(record)
 




while(True):

  print("1.celsius to kelvin\n2.celsius to fahernhiet\n3.faherhiet to celsius\n4.kelvin to celsius\n5.view conversion")
  c=int(input("Enter your choice: "))
  if(c==1):
    c_to_k()
  elif(c==2):
    c_to_f()
  elif(c==3):
    f_to_c()
  elif(c==4):
    k_to_c()
  elif(c==5):
   view_conversion()
  else:
   print("Invalid choice")
  print("Want to continue? y/n ")
  i=input(">>>")
  if(i=='n'):
   print("you exited")
   break;



