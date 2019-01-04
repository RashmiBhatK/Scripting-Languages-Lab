'''8)Create a list of 6 numbers. Use ‘list-comprehension’ to create a new list where each element
in the original list is multiplied by 3. Use ‘lambda’ and ‘reduce’ function find the sum of the
elements of the original list as well as the new list.'''



from functools import reduce
l=[]
l1=[]
for i in range(6):
 x=int(input("enter number: "))
 l.append(x)
l1=[x*3 for x in l];
print(l1)
sum1=reduce(lambda a,b:a+b,l)
print("old sum ",sum1)
sum2=reduce(lambda a,b:a+b,l1)
print("new sum",sum2)
