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

#%%
import re

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
print(sum(range(1, 6))) 

#%%

















  
  













  
  








    