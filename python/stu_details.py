'''10)Create a dictionary to hold student details with register numbers as the key. Print those
student details whose register numbers are even.'''



n=int(input("enter no of students"));
d={}
l1=[]
l2=[]
for i in range(n):
 x=int(input("enter register no: "))
 l1.append(x)
for i in l1:
 name=input("Enter name: ");
 l2.append(name)
 total=input("Enter total marks: ");
 l2.append(total)
 d[i]=l2
 l2=[]
print(d)
for i in d.keys():
 if(i%2==0):
  print(d[i])
