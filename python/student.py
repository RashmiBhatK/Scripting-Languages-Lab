'''9)(i) Create a Python class called ‘Student’ having ‘name’, ‘age’ as attribute along with a list
having the marks obtained for three subjects.
(ii) Create a constructor to initialize two objects of this class.
(iii) Create a member function called ‘display’ printing the details of a specific object
(iv) Ask user to enter the values for an object through an ‘accept’ member function.
(v) Display these details.'''



class Student:
 name="";
 age=0;
 l=[];
 def __init__(self,n,a,l):
   self.name=n;
   self.age=a;
   self.l=l;
 def accept(self):
   self.name=input("Enter the student name: ");
   self.age=int(input("Enter the student age: "));
   y=[]
   for i in range(3):
     x=input("enter marks of subject: ");
     y.append(x);
   self.l=y;
 def display(self):
   print(self.name)
   print(self.age)
   print(self.l)

obj1=Student("Sanjana",20,[45,56,78])
obj1.display()

obj2=Student("Sumuki",20,[45,56,78])
obj2.display()
obj2.accept()
obj2.display()

