# %%
a = "no"
b = "yes"
class MyClass:
    def __init__(self,x):
        self.x = x
p1 = MyClass(36)
print(p1.x)


#%%
import pandas as pd
c = "not"
df = pd.read_csv("Churn.csv")
# ------------------------------------------BASIC PROBLEMS PRACTICE--------------------------------
#%%

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")
  
# %% 
def greater_than(num1,num2):
  if (num1 * num2) > 1000:
    return(num1 * num2)
  else:
    return(num1 + num2)
    
result = greater_than(10,6)   

print("The result is ", greater_than(2,3))

#%%

def current_previous(num):
  if num > 0:
    current = num
    previous = num - 1
    sums= current + previous
  else:
    current = num
    previous = num 
    sums= current + previous
  return  ("Current Number %d Previous Number %d previous Sum: %d " %(current,previous,sums))

print(current_previous(5))  

#%%
def current_previous_2():
  for i in range(1,11):
    current = i
    previous = i-1
    sums = current + previous
    print("Current Number %d Previous Number %d Sum: %d" %(current, previous, sums))

print(current_previous_2())

#%%
import math
def display_even(word1):
  arr = []
  # word = input("Enter Word")
  size = len(word1)
  for i in range(0, size, 2):
    arr.append(word1[i])
    # if i % 2 == 0:
    print(word1[i])
 
  

print(display_even("word"))

#%%

import math
def display_even1(word):
  string = ''
  # word = input("Enter Word")
  size = len(word)
  x = list(word)
  for i in x[0::2]:
    
    # if i % 2 == 0:
    print(type(i))
    return i
print(display_even1("word"))

#%%

def remove_chars(n):
  word = input("Enter word")
  # x = list(word)
  x = word[n:]
  return x
print(remove_chars(4))

#%%

arr = [1,2,3,4,5,1]

def first_last(arr):
  first_num = arr[0]
  last_num = arr[-1]
  print(arr[0::len(arr)-1])
  if first_num == last_num:
    return True
  else:
    return False  


print(first_last(arr))

#%%
arr = [5,10,15,7,8]
def div_by_five():
  for i in arr:
    if i % 5 == 0:
       print(i)

print(div_by_five())

#%%

def string_count(str):
  string = input("Enter text here")

  cap_string = string.upper()

  cap_param = str.upper()
  print(cap_param)
  

  
  return ("%s appeared %d times" %(cap_string,cap_param.count(cap_string)))

print(string_count("Jimmy is the best. Jimmy smells good"))  
    
#%%

def loop_pattern1():
  rows = int(input("Enter number of rows"))
  for i in range(rows):
    for j in range(i):
      print("*",end=' ')
    print('\n')  
print(loop_pattern1())    

#%%

def loop_pattern2():
  rows = int(input("Enter number of rows"))
  for i in range(rows +1, 0,-1):
    for j in range(0, i-1):
      print("*",end=' ')
    print('\n') 
print(loop_pattern2())  

#%%

def loop_pattern3():
  rows = int(input("Enter number of rows"))
  k = 2 * rows - 2
  for i in range(0,rows):
    for j in range(0, k):
      print(end=' ')
    k = k -2
    for j in range(0, i+1):
      print("* ", end="")   
    print('\n') 
print(loop_pattern3())  

#%%

def is_palindrome():
  number = (input("Enter number")) 
  x = list(number)
  b = (list(reversed(x)))
  c = "".join(x)
  z = "".join(b)
  print(c)
  print(z)
  if c == z:
    return True
  else: 
    return False  


  
print(is_palindrome()) 

#%%

def combined_list( array_even,array_odd):
  results = []
  for i in array_even:
    if i % 2 == 0:
      results.append(i)
  for j in array_odd:
    if j % 2 == 1:
      results.append(j)
  return results

print(combined_list([1,2,3,4,5],[444,55,23]))
#%%

def taxable_income():
  income = input("Enter income here")
  ten = 0.0 
  remainder = 0.0
  twenty = 0.0

  if float(income) >= 20000:
    ten = ten + (10000 *.1)
    remainder = remainder + (float(income) - 20000)
    twenty = twenty + (remainder *.2)

    print(ten, remainder, twenty)

  return round(float(ten + twenty),2)

print(taxable_income())

#%%

def mult_table():
  for i in range(1,11):
    for j in range(1,11):
      print(i * j, end=" ")
    print("\n")  
  return "Complete"
    

print(mult_table())

#%%
def exponent(base, exp):
  arr = []
  result = 1
  for i in range(exp):
    arr.append(base)
    # print(arr)
  for i in arr:
    result = result * i      
    # print(result)
  return result
      
    
print(exponent(5,8))

#%%

def my_name_():
    name = input("Enter first name")
    print("Name", "Is", name, sep="**",end=' YAY')
    return ""

print(my_name_())
# --------------------------------------LOOPS PRACTICE------------------------------------------------
#%%

def number_pyramid():
  rows = int(input("Enter number of rows"))
  for i in range(1, rows + 1, 1):
    for j in range(1, i + 1):
      print(j,end=' ')
    print('\n')  
print(number_pyramid())

#%%

def sum_all():
    number = int(input("Enter Number"))
    num = 0
    # range(start, stop, increment) The number between start and stop not including the stop
    for i in range(0,number + 1):
        num = num + i
        print(i)
    return ("Sum is: %d"%num)   

print(sum_all())       
print(sum(range(1, 5))) 

#%%

def multiply():
    number = int(input("Enter Number"))
    # range(start, stop, increment) The number between start and stop not including the stop
    for i in range(0,11):
       
        print(number * i)
    return ""

print(multiply())

#%%

#recursive function

def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)

#%%
def display_student(name, age):
    print(name, age)

display_student("Emma", 26)

show_student = display_student

show_student("Emma", 26)


#%%
# OOP

class Vehicle:

    # Class Attribute
    color = "White"
    
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
        

    def show(self):
        print("Car Speed:",self.max_speed, "Gas Mileage:", self.mileage)   

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    def fare(self):
        return self.capacity * 100

modelX = Vehicle("Ford",100,20, 5) 
modelX.show()   
print(modelX.color)

#%%

class Vehicle1:
    pass

#%%
# Child Class: Inheritance

class Bus(Vehicle):
    def seating_capacity(self, capacity=60):
        print(super().seating_capacity(capacity=60))
        return super().seating_capacity(capacity=60)

# Overriding a method from the parent
    def fare(self): 
        amount= super().fare()
        amount += amount * 10 / 100
        return amount
    

School_bus = Bus("School Volvo", 180, 12,5)
# School_bus.seating_capacity = 50
# print("The seating capcity for this bus is %d" %School_bus.seating_capacity)
print(School_bus.color,"Vehicle Name:", School_bus.name, "\nSpeed:", School_bus.max_speed, "\nMileage", School_bus.mileage)
print(School_bus.seating_capacity())
print (School_bus.color)
print(School_bus.fare(), modelX.fare())
print(isinstance(School_bus, Vehicle))

#%%

import json

data = {"ID" : 1, "value2" : "age"}

# json.dumps takes in a json object and returns a string
jsonData = json.dumps(data)
print(type(data))
print(type(jsonData))

#%%

import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

# json.load takes in a string and returns a json object.
data1 = json.loads(sampleJson)

print(data['key2'])

#%%

import json

# formats json string
prettyPrint = json.dumps(data, indent=2, separators=(",", " = "))

print(prettyPrint)

#%%

# sampleJson2 = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
print("Writing started...")
with open("sampleJson2.json", "w") as write_file:
    json.dump(sampleJson2, write_file, indent=4, sort_keys=True)
print("Done writing")  

#%%
import pandas as pd
import re
# dater = json.loads(sampleJson2)
# print(dater['company']['employee']['payble']['salary'])


# Opening the .json file
f = open('sampleJson2.json')

dater = json.load(f)
daterr = json.dumps(dater, indent=2, separators=(",", " = "))

print(daterr)

toppings = dater['topping']

for topping in toppings:

    if 'Choc' in topping['type']:
     print(topping['id'])

#%%

import numpy

firstarray = numpy.empty([4,2], dtype = numpy.uint16)
print("Printing Array")
print(firstarray)
print("Array shape is:",firstarray.shape)
print("Dimensions:", firstarray.itemsize)


#%%

from bs4 import BeautifulSoup
from requests import get
url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
print(response.text[:500])
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))






        







 





















  
  













  
  








    