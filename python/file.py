'''4) Python File Handling & List Comprehension: Write a python program to read contents of a
file (filename as argument) and store number of occurrences of each word in a dictionary.
Display the top 10 words with most number of occurrences in descending order. Store the
length of each of these words in a list and display the list. Write a one-line reduce function to
get the average length and one-line list comprehension to display squares of all odd numbers
and display both.'''



import re
import sys
import operator
from operator import itemgetter
from functools import reduce

if(sys.argv[1]!=""):
 count_list=[]
 count_dict={}
 with open(sys.argv[1],'r') as f:
   for line in f:
     for word in line.split():
       word=re.sub(r'[^\w\s]','',word)
       if word not in count_dict:
         count_dict[word]=1
       else:
         count_dict[word]+=1
 count_list=sorted(count_dict.items(),key=operator.itemgetter(1),reverse=True)
 print(count_list[:10])
 count=[]
 for i in range(len(count_list)):
   count.append(count_list[i][1])
 print(count)
 avg=reduce(lambda a,b:a+b,count)/len(count)
 print("average:",avg)
 print([x*x for x in count if x%2!=0])
else:
 print("enter filename")
exit()  


