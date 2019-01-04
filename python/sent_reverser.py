'''2)Python Classes: Write a python class to reverse a sentence (initialized via constructor) word
by word. Example: “I am here” should be reversed as “here am I”. Create instances of this
class for each of the three strings input by the user and display the reversed string for each, in
descending order of number of vowels in the string.'''



class Sentencereverser:
   vowels=['a','e','i','o','u']
   vowelcount=0
   sentence=""
   reverse=""
   def __init__(self,sentence):
     self.sentence=sentence
     self.reverseSentence()
   def reverseSentence(self):
     self.reverse=" ".join(reversed(self.sentence.split(" ")))
   def getvowelcount(self):
     self.vowelcount=sum(s in self.vowels for s in self.sentence.lower())
     return self.vowelcount
   def getreverse(self):
     return self.reverse
items=[]
for i in range(3):
 sentence=input("enter sentence: ")
 reverse=Sentencereverser(sentence.strip())
 items.append(reverse)
sorteditems=sorted(items,key=lambda item: item.getvowelcount(),reverse=True)
for i  in range(len(sorteditems)):
 print("reversed:",sorteditems[i].getreverse(),"vowelcount: ",sorteditems[i].getvowelcount())
    
