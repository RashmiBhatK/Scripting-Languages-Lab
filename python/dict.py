'''7)(i) Create a dictionary that contains the atomic element symbol and its name.
(ii) Add a unique & duplicate element into this dictionary by interacting with the user.
Observe the output and justify it.
(iii) Display the number of atomic elements in this dictionary
(iv) Ask user to enter an element to search in the dictionary. Display appropriate results.
Rewrite this program so that these operations are inside a function called ‘AtomicDictionary’.
Create another python file called “Atomic.py” and execute this function in it.'''



def AtomicDictionary():
  d={"B":"Boron","S":"sulphur","He":"Helium"};
  print(d);
  new_sym=input("Enter a symbol: ");
  new_ele=input("Enter Element: ");
  if(new_sym not in d.keys()):
    print("added to dict");
  else:
    print("The key exists and hence value is replaced");
  d[new_sym]=new_ele;
  print(d);
  print("The no. of elements: ",len(d));
  ele=input("enter  a element to check its existance: ");
  if ele not in d.keys():
    print("element not found");
  else:
    print(d[ele]);
