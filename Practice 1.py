#!/usr/bin/env python
# coding: utf-8

# In[3]:


x, y, z = input("Enter three values : ").split()
print(x)
print(y)
print(z)


# In[1]:


i = 0;
sum = 0;
while i<9:
    if i%4 == 0:
        sum = sum + i;
    i = i + 2
print(sum)


# In[4]:


a, b = input("Enter two values: ").split()
print("First number is {} and Second number is {}".format(a,b))


# In[5]:


x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ",x)


# In[6]:


name = "John"
age = 30

print("Name:", name)
print("Age:", age)


# In[8]:


name = "Aman"
age = 19

print("Hello, my name is", name, "and I am", age, "years old.")


# In[10]:


import time

count_seconds = 8
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print("Start")


# In[11]:


import time

count_seconds = 8
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(1)
    else:
        print("Start")


# In[12]:


a = 12
b = 12
c = 2023
print(a,b,c,sep="-")


# In[15]:


a = [1,2,3,4,5,6,7,8,9]

for i in range(9):
    print(a[i])


# In[18]:


a = [1,2,3,4,5,6,7,8,9]

for i in range(9):
    print(a[i], end =" ")


# In[19]:


l = [1,2,3,4,5]
print(*l)


# In[20]:


print("A","M","A","N", sep=" ")


# In[21]:


print('I love {} for "{}!"'.format('Geeks', 'Geeks'))

print('{0} and {1}'.format('Geeks', 'Portal'))

print('{1} and {0}'.format('Geeks', 'Portal'))

print(f"I love {'Geeks'} for \"{'Geeks'}!\"")

print(f"{'Geeks'} and {'Portal'}")


# In[22]:


a = int(input("Enter the value: "))
b = int(input("Enter the value: "))

add = a + b

sub = a - b

mul = a * b

mod = a % b

p = a ** b

print(add)
print(sub)
print(mul)
print(mod)
print(p)


# In[23]:


x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


# In[1]:


import keyword as kw
print(kw.kwlist)
print("\n No. of Keywords:",len(kw.kwlist))


# In[3]:


a = 10 ; b = 20 ; c = 30

print("Value of a is {} and b is {} and c is {}" .format(a,b,c))


# In[5]:


print("Hello {name},{greeting}" .format(name = "Aman", greeting = "Kya kr rahe ho"))


# In[6]:


print("Ram has {0} Shyam has {1}" .format("Car","Bike"))


# In[7]:


n = int(input("Kitna number h bhai :"))
print(n)


# In[9]:


n,k = map(int,input().split())
print(n)
print(k)


# In[10]:


x = 3
print(id(x))


# In[11]:


y = 5 
print(id(x))


# In[12]:


y = 3456
print(id(y))


# # Let's Start Python 
# 

# ## Keywords in Python

# In[13]:


import keyword as kw
print(kw.kwlist)
print("\n No. of Keywords:",len(kw.kwlist))


# ## Identifiers  in Python

# 1. Identifiers is the name given to entities like class, function, variable.
# 2. It helps differentiating one entity from other.
# 3. (a-z),(A-Z),(0-9),(_).
# 4. Cannot Start with Digits.
# 4. Keywords cannot be used as an identifiers.

# ## Standard IO

# In[15]:


a = 10
print("Value of a is",a)


# In[16]:


a = 10 ; b = 20
print("Value of a is {} and value of b is {}".format(a,b))


# In[17]:


a = 20 ; b = 10
print("Value of a is {1} and b is {0}". format(a,b))


# In[18]:


print("My name is {name} and my age is {age}". format(name="Aman",age=19))


# In[20]:


n = int(input("Kuch number daal bhai  "))
print(n)


# In[25]:


n,k = map(int,input("Number likho :").split())
print("n ki value hai:",n)
print("k ki value hai:",k)


# ## Comments & Indentation in Python

# In[26]:


# Single line comment


# ##### Indentation

# In[29]:


a = 500
if(a>5):
    print("5 se bada hai")
print("Kya yaar itna bda number")


# ### Data Types in Python

# 1. Integer
# 2. Float
# 3. Complex
# 4. Boolean
# 5. String

# In[31]:


a = 12 
print(a, "is of type", type(a))


# In[32]:


a = 12.4
print(a, "is of type", type(a))


# In[33]:


a = 4 + 5j
print(a, "is of type", type(a))


# In[34]:


a = "Aman"
print(a, "is of type", type(a))


# In[36]:


print(a[0])
print(a[1])
print(a[2])
print(a[3])


# In[37]:


print(a[-1])
print(a[-2])


# In[38]:


print(len(a))


# Slicing
# 

# In[39]:


a[3:]


# In[40]:


a[:]


# In[41]:


a[1:]


# In[42]:


a[0:-1]


# ## Data Structures in Python

# 1. List
# 2. Tuple
# 3. Sets
# 4. Dictionary

# 1. List :-
#      List is Mutable

# In[43]:


a = [10,24,5.76,"Aman"]
print(a[3])


# In[45]:


a[1] = "Hello"
print(a)


# 2. Tuple :- Tuple is immutable

# In[46]:


t = (1, 2,56,"Aman",5 + 6j)
print(t)


# 3. Sets

# In[47]:


a = {10,30,65,85,46,24}
print(a)


# 4. Dictionary

# In[48]:


d = {"a": "Aman",
     "b": "Bat"}
print(d)


# In[49]:


print(d["a"])


# ## Operators in Python

# Operators are special Symbol in python that cary out arithematic or logical computation. The value that the operator operates on is called the operand.

# Types :-
#  1. Arithematic Operator
#  2. Realtion Operator
#  3. Logical Operator
#  4. Bitwise Opeartor
#  5. Assignment Opeartor
#  6. Special Opeartor

# In[50]:


a, b = 2, 5
print(a+b)


# In[51]:


a, b = 5, 7
print(a*b)


# In[52]:


a, b = 4, 4
print(a**a)


# In[53]:


print(a//b)


# In[54]:


a , b = 3, 6
print(a%b)


# In[55]:


a, b = 10,20
print(x!=y)


# In[56]:


a, b = True, False
print(a and b)


# In[57]:


print(a or b)


# In[58]:


print(a & b)


# In[59]:


a = 10
a +=20
print(a)


# ## Conditions in Python

# 1. Equals : a == b
# 2. Not Equals: a != b
# 3. Less than: a < b
# 4. Less than or equal to : a <= b
# 5. Greater than : a > b
# 6. Graeter than or equal to : a >= b

# ## Statements in Python

# 1. If Statement

# In[60]:


a = 33
b = 100
if b > a:
    print("b is greater than a")


# 2. Elif Statement

# In[61]:


a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


# 3. Else Statement

# In[62]:


a = 100
b = 33

if b>a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greter than b")


# ## Loops in Python

#     1. While Loop
#     2. For Loop

# #### 1. While Loop

# In[64]:


list = [10,20,30,40,50]
product = 1
index = 0
while index < len(list):
    product *= list[index]
    index += 1
print("Product is : {}".format(product))    


# In[66]:


numbers = [1,2,3,4,5]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
else :
    print("Kuch nhi bacha bhai")


# In[67]:


# Program to check if a number is prime or not 


# In[70]:


num = int(input("Enter the number: "))

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
            
    else:
        print(num,"is prime number")


# In[71]:


# Find Product of all numbers in a list


# In[72]:


list = [10,20,30,40,50]
product = 1
index = 0
for i in list:
    product *= i
print("Product is : {}".format(product))


# In[73]:


for i in range(10):
    print(i)


# In[76]:


for i in range(1,20,2):
    print(i)


# In[77]:


list = ["Aman","Ankush","Delhi","Noida"]
for index in range(len(list)):
    print(list[index])


# In[78]:


list = ["Aman","Ankush","Delhi","Noida"]
for element in list:
    print(element)


# In[79]:


number = [1,2,3,4,5]
for item in number:
    print(item)


# In[80]:


# Program to display all the prime numbers within an interval


# In[81]:


lower = 900
upper = 1000

print("Prime number between", lower, "and", upper, "are:")

for num in range (lower, upper +1):
    if num > 1:
        for i in range(2,num):
            if (num% i) == 0:
                break
                
        else:
            print(num)



# ### Break and Continuity Statement

# In[82]:


numbers = [1,2,3,4]
for num in numbers:
    if num == 4:
        break
    print(num)
print("Loop ke bahar aa gya bhai")


# In[83]:


numbers = [1,2,3,4,5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
print("Loop ke bahar hu mai")


# ## List Data Structure

# #### List is mutable

# In[84]:


khali_list = []
list_1 = ["One","two","three","four"]
list_2 = [1,2,3,4,5,]
list_3 = [[1,2],[3,4]]
list_4 = [1,"Aman",99.456,34]


# In[85]:


print(list_3)


# In[86]:


list = ["one","tw0","three","four","five"]


# In[87]:


print(len(list))


# In[88]:


list.append("Six")
print(list)


# In[89]:


list.insert(2,"Nine")
print(list)


# In[90]:


list.remove("four")
print(list)


# In[91]:


list_1 = ["one","two","three","four"]
list_2 = ["five","six"]

list_1.append(list_2)
print(list_1)


# In[93]:


list_1 = ["one","two","three","four"]
list_2 = ["five","six"]

list_1.extend(list_2)
print(list_1)


# In[94]:


list_1 = ["one","two","three","four"]

del list_1[1]
print(list_1)


# In[95]:


list_1 = ["one","two","three","four"]

a = list.pop()
print(a)
print(list)


# In[96]:


list_1 = ["one","two","three","four"]

list_1.remove("three")
print(list_1)


# In[99]:


list = ["one","two","three","four"]

if "two" in list:
    print("Noob")
    
if "six" not in list:
    print("Pro")


# In[100]:


list = ["one","two","three","four"]
list.reverse()
print(list)


# In[101]:


numbers = [3,5,6,2,4,7,8,9,2,1,43,56,79]
sorted_list = sorted(numbers)
print("Sorted list:",sorted_list)
print("Original list:",numbers)


# In[102]:


numbers = [3,5,6,2,4,7,8,9,2,1,43,56,79]
sorted_list = sorted(numbers)
print("reverse sorted list:",sorted(numbers, reverse = True))
print("original list:",numbers)


# In[103]:


list = [1,54,76,23,61,99,21,11]
list.sort()
print("Sorted list :", list)


# In[104]:


list = [1,2,3,4,5]
abc = list
abc.append(6)
print("Original list:",list)


# In[105]:


s = "one,two,three,four,five"
split = s.split(",") # convert into list
print(split)


# In[107]:


s = "Kya hua bhai"
split_list = s.split()
print(split_list)


# In[108]:


num = [10,20,30,40,50,60,70,80,90]

print(num[:])
print(num[0:4])


# In[109]:


num = [10,20,30,40,50,60,70,80,90]

print(num)
print(num[::2])
print(num[2::2])


# In[110]:


list_1 = [1,2,3,4,5]
list_2 = ["Aman","Ajay","Alok","Abir"]

new_list = list_1 + list_2
print(new_list)


# In[111]:


num = [1,2,3,4,5,6,6,3,2,4,2,3,1,4,6,7,1,8,9,3,1,3,5,3,2,5,6,3,1,7,8]

print(num.count(1))


# In[112]:


num = [1,2,3,4,5]
for element in num:
    print(element)


# In[119]:


squares = []
for i in range(10):
    squares.append(i**2)
print(squares)


# In[120]:


squares = [i**2 for i in range(10)]
print(squares)


# In[121]:


list = [-10,-20,10,20,50]
list = [2*i for i in list]
print(list)


# In[122]:


list = [(i,2*i) for i in range(10)]
print(list)


# ## Tuple Data Structure

# #### Tuple is immutable

# In[123]:


t = (1,2,3)
print(t)

t = (1,(1,2,3),("Aman","Shyam","Ajay"),45,67)
print(t)


# In[124]:


t = ([1,2,3,4],["Aman","Ajay","Shyam"])
print(t)   #tuple ke andar list


# #### Parenthesis is optional in Tuple

# In[126]:


t = "jai","shree","Ram"
print(type(t))


# In[127]:


t = "jai","shree","Ram"
print(t[1])


# In[129]:


t = (1,(1,2,3),("Aman","Shyam","Ajay"),45,67)
print(t[2][1])


# #### Slicing

# In[130]:


t = (1,2,3,4,5,6,7)
print(t[1:4])

print(t[:-2])

print(t[:])


# In[131]:


t = (1,2,3) + (4,5,6)
print(t)


# In[132]:


t = (("Aman",)*5)
print(t)


# In[134]:


t = (1,2,3,4,5)
del t


# In[136]:


t = (1,2,3,1,2,4,5,1,6,3,6,1,4,7,1)
print(t.count(1))


# In[137]:


t = (1,2,3,1,2,4,5,1,6,3,6,1,4,7,1)
print(t.index(3))


# In[138]:


t = (1,2,3,4,5)
print(1 in t)
print(8 in t)


# In[140]:


t = (1,2,3,4,5,6)
print(len(t))


# In[141]:


t = (3,5,2,4,67,21,5,9,1)
sorted_tuple = sorted(t)
print(sorted_tuple)


# In[142]:


# sorted krne se wo list ban jata h taki usme ham changes kr sake 


# ## String Data Structure

# ####
# 1. String is mutable
# 2. String is a sequence of Character
# 3. A character is simply a symbol

# In[143]:


my_string = "Texted Someone"
print(my_string)

my_string = 'Or bhai kese ho ?'
print(my_string)

my_string = '''kese ho bhai ?'''
print(my_string)


# In[144]:


my_string = "Hello"

print(my_string[0])
print(my_string[-1])
print(my_string[2:5])


# In[146]:


s1 = "Hello "
s2 = "Aman "

print(s1 + s2)

print(s2*3)


# In[148]:


count = 0
for i in "Hello World":
    if i == "o":
        count += 1
print(count," mil gya")


# In[150]:


print("l" in "Hello World")
print("or" in "Hello World")


# In[151]:


"EX".lower()


# In[152]:


"next".upper()


# In[153]:


"sab moh maya h".split()


# In[154]:


"_".join(["sab","moh","maya","hai"])


# In[155]:


"Good Morning".find("in")


# In[156]:


"Bad Morning".replace("Bad","Good")


# In[157]:


s1 = "Bad Morning"
s2 = s1.replace("Bad","Good")
print(s1)
print(s2)


# ### Python Program to check Palindrome

# In[ ]:


myStr = "Nitin"
myStr = myStr.lower()
revStr = reversed(myStr)
if list(myStr) == list(revStr):
    print("Palindrome")
else:
    print("Not a Palindrome")


# In[174]:


mystr = "Python Program to sort word in Alphabetical order"
words = mystr.split()
words.sort()
for word in words:
    print(word)


# ## Set Data Structure

# #### Set are used to store multiple items in a single variable

# In[175]:


s = {1,2,3}
print(s)
print(type(s))


# In[177]:


# set from a list
s = set([1,2,3,4,1,5,6,7])
print(s)


# In[179]:


#empty set
s = set()
print(type(s))


# In[180]:


s = {1,2,3,4,5,}
s.add(8)
print(s)


# In[185]:


s = {1,2,3,4,5,}
s.update([6,7,8])
print(s)


# In[186]:


s = {1,2,3,4,5,}
s.discard(4)
print(s)


# In[187]:


s = {1,2,3,4,5,}
s.remove(3)
print(s)


# In[188]:


s = {1,2,3,4,5,}
s.pop()
print(s)


# In[189]:


s = {1,2,3,4,5,}
s.clear()
print(s)


# In[190]:


set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}

print(set1|set2)


# In[191]:


print(set1.union(set2))


# In[192]:


print(set1.intersection(set2))


# In[193]:


print(set1 - set2)


# In[194]:


print(set1^set2)


# ## Dictionary Data Structure

# ####
#  Dictionary are used to store data values in key:value pairs.
#  A Dictionary is a collection which is ordered, changeable and do not allow duplicates.

# In[195]:


my_dict = {"Name" : "Aman","Course": "B.tech"}
print(my_dict)


# In[196]:


mydict = dict()


# In[197]:


mydict = {"Name" : "Nibba",
          "Age" : 14,
          "Address" : "Bhopal"}

print(mydict["Name"])


# In[198]:


print(mydict.get("Address"))


# In[199]:


print(mydict.get("Course"))


# In[200]:


mydict = {"Name" : "Nibba",
          "Age" : 14,
          "Address" : "Bhopal"}
mydict["Name"] = "Nibbi"
print(mydict["Name"])


# In[201]:


mydict["Degree"] = "B.tech"
print(mydict)


# In[202]:


mydict = {"Name" : "Nibba",
          "Age" : 14,
          "Address" : "Bhopal"}

print(mydict.pop("Age"))  #removes particular item
print(mydict)


# In[203]:


mydict = {"Name" : "Nibba",
          "Age" : 14,
          "Address" : "Bhopal"}

mydict.popitem()  #remove an arbitrary key
print(mydict)


# In[205]:


squares = {2:4, 3:9, 4:16, 5:25}
del squares[2]
print(squares)


# In[207]:


squares.clear()
print(squares)


# In[208]:


squares = {2:4, 3:9, 4:16, 5:25}
mydict = squares.copy()
print(mydict)


# In[213]:


subjects = {}.fromkeys(["Math","English","Hindi"],2)
print(subjects)


# In[214]:


subjects = {2:4, 3:9, 4:16, 5:25}
print(subjects.items())


# In[216]:


print(subjects.keys())


# In[217]:


print(subjects.values())


# In[218]:


d = {}
print(dir(d))


# In[220]:


d = {"a" : 1, "b" : 2, "c" : 3}
for pair in d.items():
    print(pair)


# In[221]:


d = {"a" : 1, "b" : 2, "c" : 3, "d" : 4}
newdict = {k:v for k,v in d.items() if v>2}
print(newdict)


# In[222]:


d = {"a" : 1, "b" : 2, "c" : 3, "d" : 4}
d = {k + "c":v*2 for k,v in d.items() if v>2}
print(d)


# ## Python Functions

# ####
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameter, into a function.
# A function can return data as a result.

# In[1]:


def enter_name(name):
    # Enter your name
    print("Hello " + name)
    
enter_name("Aman")


# In[2]:


def enter_sum(lst):
    
    # Enter the values and get their sum
    
    sum = 0
    for num in lst:
        sum = sum + num
    return sum

s = enter_sum([1,3,5,6,8,9,3])
print(s)


# In[4]:


global_var = "I am a global variable"
def test_life_time():
    local_var = "I am a local variable"
    print(local_var)
    print(global_var)
    
#calling function
test_life_time()

#print global variable
print(global_var)

#print local variable
print(local_var)


# #### Program to find hcf of  a number

# In[6]:


def find_HCF(a,b):
    smaller = b if a > b else a
    
    hcf = 1
    for i in range(1, smaller + 1):
        if(a % i == 0) and (b % i == 0):
            hcf = 1
    return hcf

num1 = 34
num2 = 56

print("HCF of {0} and {1} is {2}".format(num1,num2,find_HCF(num1,num2)))


# ## Built-in functions in Python

# In[7]:


# find the absolute value

num = -100
print(abs(num))


# In[8]:


lst = [1,2,3,4]
print(all(lst))
# if 0 is present then it returns true other wise it return false


# In[9]:


lst = (0,1,2,3,4)
print(all(lst))


# In[10]:


lst = []
print(all(lst))


# In[11]:


lst = [False,1,2]
print(all(lst))


# In[12]:


number = [10,20,30,40]
for index,num in enumerate(number,10): 
    print("index {0} has value {1}".format(index,num))
    
#enumerate(number,start = 0)


# In[14]:


def greet (*names):
    print(names)
    for name in names:
        print("Hello, {0}".format(name))
greet("Chintu","Mintu","Chinti","Minti")


# ### Lambda Function
# 
# 

# In[15]:


double = lambda x: x*2
print(double(5))


# In[18]:


def double(x):
    return x*2
print(double(5))


# In[19]:


lst = [1,2,3,4,5,6]
new_list = list(map(lambda x: x**2, lst))
print(new_list)


# In[22]:


#Lambda function with reduce()

from functools import reduce

lst = [1,2,3,4,5]
product_lst = reduce(lambda x,y: x*y, lst)
print(product_lst)


# ## Questions Solving

# ### Q.) Check whether a year is leap year or not

# In[26]:


n = int(input("Enter the year: "))
if n % 400 == 0:
    print("Leap Year")
elif n % 4 == 0 and n % 100 != 0:
    print("Leap Year")
else:
    print("Non Leap year")


# ### Q.) Remove duplicates from list 

# In[28]:


l = [10,30,20,10,40,30,10,50,60,20]
s = set(l)
lst = list(s)
print(lst)

sorted_list = sorted(lst)
print(sorted_list)


# ### Taking input from user in any list

# In[30]:


l = [eval(i) for i in input().split()]
print(l)


# ### Q.) Print first 10 natural numbers

# In[32]:


for i in range(1,11):
    print(i)


# In[34]:


i = 1
while i<= 10:
    print(i,end=' ')
    i+=1


# ### Q.) How to print next prime

# In[ ]:


def NextPrime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%1 == 0:
                break
        else:
            return n
               
print(NextPrime(11))


# ### Q.) How to reverse a tuple ?

# In[ ]:


t = input("Enter some numbers: ")
l = list(t)
l.reverse()
print(tuple(l))


# ### Q.) How to remove duplicates from string?

# In[ ]:


s = input("Enter the string: ")
s1 = " "
i = 0
for x in s:
    if(s.index(x)==i):
        s1+=x
        
    i+=1
print(s1)


# ### Q.) Sum of Squares using Recursion

# In[ ]:


def sum(n):
    if n==1:
        return 1
    return n**2 + sum(n-1)
print(sum(5))


# ### Q.) Reverse a string using slicing

# In[ ]:


s = input("Enter a string: ")
s1 = s[len(s)-1::-1]
print(s1)


# ### Q.) Check divisibility of a number
# 

# In[ ]:


n = int(input("Enter the number: "))
d = int(input("Divide wala number: "))
if (n%d)==0:
    print("Divide ho gya")
else:
    print("Divide nhi hua")


# ### Q.) Sort in dictionary order

# In[ ]:


[x for x in sorted("enter three strings separated by commas").split(',') if print(x,end=' ')]


# ### Q.) How to sort a list

# In[ ]:


l = [eval(x) for x in input("enter the number").split(',')]
l1 = sorted(l)
print(l1)


# In[ ]:


l = [eval(x) for x in input("enter the number").split(',')]
l.sort()
print(l)


# ### Q.) Sum of n natural numbers

# In[41]:


def sum1(n):
    return n*(n+1)//2
def sum2(n):
    s = 0
    for i in range(1,n+1):
        s = s+1
    return s
n = int(input("Enter the number: "))
print(sum1(n))
print(sum2(n))
    


# ### Q.) Euclid's Algorithm

# In[42]:


a = int(input())
b = int(input())

if a>b:
    l = a
else:
    l = b
for i in range(1,(a*b)+i,1):
    if(i%a==0 and i%b==0):
        break
        
lcm = i
hcf=(a*b)//lcm

print("Lcm is: ",lcm)
print("HCF is: ",hcf)


# ## File Handling

# ###
#     File Operations:-
#     1. Open a file
#     2. Read or write
#     3. Close the file
# 

# In[43]:


import os
os.getcwd()


# In[44]:


f = open('file','w') #open file in current directory


# In[45]:


f = open('file','w')
f.close()


# In[46]:


try:
    f = open("file.txt",'w')
finally:
    f.close()


# In[52]:


#write to a file
f = open("file","w")
f.write("Hehehehe \n")
f.write("dusri file m dhund le bhai \n")
f.close()


# In[53]:


f = open("file","r")
f.read()


# In[54]:


f = open("file","r")
f.read(2)


# In[55]:


f = open("file","r")
f.tell()


# In[56]:


f = open("file","r")
f.seek(0)


# In[58]:


f = open("file","r")
f.seek(0)
for line in f:
    print(line)


# In[59]:


f = open("file","r")
f.readline()


# In[60]:


f = open("file","r")
f.readline()


# In[61]:


f.readline()


# In[ ]:


os.listdir(os.getcwd()) 


# ## Exception Handling

# In[63]:


dir(__builtins__)


# In[64]:


import sys

lst = ['a',0,2]
for entry in lst:
    try:
        print("M aagya",entry)
        r = 1 / int(entry)
    except:
        print("Ooh bhai!",sys.exc_info()[0],"occured.")
        print("Agla kon h")
        print("******************************")
print("Reciprocal of",entry, "is ",r)


# ## OOPS Concept in Python

# In[1]:


class phone:
    def call(self):
        print("Call kro kisi ko")
    def game(self):
        print("Game khelte h bhai aa ja")


# In[3]:


p1 = phone()
p1.call()


# In[5]:


class phone:
    def set_color(self,color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def call(self):
        print("Call kro")
    def game(self):
        print("Game khel le")
        
p1 = phone()

p1.set_color("White")
p1.set_cost(20000)


# In[7]:


p1.show_color()


# In[8]:


p1.show_cost()


# ### The __init__ function

# In[9]:


class Employee:
    
    def __init__ (self,name,age,salary,gender):
        self.name = name 
        self.age = age
        self.salary = salary
        self.gender = gender
        
    def employee_details(self):
        print("Name of Employee is",self.name)
        print("Age of Employee is",self.age)
        print("Salary of Employee is",self.salary)
        print("Gender of Employee is",self.gender)
        


# In[10]:


e1 = Employee("Ramesh",24,10000,"Male")
e2 = Employee("Suresh",28,15000,"Male")


# In[11]:


e1.employee_details()


# 

# ### Types of Variables in OOPS:-
#         1. Instance Variable
#         2. Static(Class) Variable

# In[13]:


class car:
    wheels = 4
    def __init__(self):
        self.mil = 10
        self.comp = "KIA"
        
c1 = car()
c2 = car()
c1.mil = 8
car.wheels = 6
print(c1.comp,c1.mil,c1.wheels)
print(c2.comp,c2.mil,c2.wheels)


# ## Polymorphism

# In[15]:


class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def info(self):
        print("I am a cat.My name is{self.name}.I am{self.age}years old")
        
    def make_sound(self):
        print("Meow")
        
class Dog:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def info(self):
        print("I am a Dog.My name is{self.name}.I am{self.age}years old")
        
    def make_sound(self):
        print("Bark")
        
cat1 = Cat("Kitty",2.5)
dog1 = Dog("Sheru",3)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
    


# In[16]:


class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
        
class Intellij:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Debugging")
        print("Code Runner")
        
class Laptop:
    def code(self,ide):
        ide.execute()
        
ide = Pycharm()

lap1 = Laptop()
lap1.code(ide)
        


# In[ ]:





# ### Operator Overloading

# In[18]:


class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)
        return s3
    
s1 = student(98,59)
s2 = student(75,57)
s3 = s1 + s2
print(s3.m1)
print(s3.m2)


# ## Inheritance

# In[19]:


class vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
        
    def show_details(self):
        print("Vehicle")
        print("Mileage: ",self.mileage)
        print("cost: ",self.cost)
        
        
v1 = vehicle(10,1000000)
v1.show_details()


# In[21]:


class car(vehicle):
    def show_car(self):
        print("kia Seltos")
        
c1 = car(25,1000000)
c1.show_details()
c1.show_car()


# In[25]:


#overriding init method

class car(vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres = tyres
        self.hp = hp
    
    def show_car_details(self):
        print("creta")
        print("Mileage:",self.mileage)
        print("Price:",self.cost)
        print("no. of tyres:",self.tyres)
        print("Horse Power:",self.hp)
        
c3 = car(10,800000,4,450)
    
c3.show_car_details()


# ## Regular Expression

# In[33]:


import re
s = '''Chintu is 24 and Mintu is 22
Pintu is 21 and Shintu is 20'''


# In[34]:


s


# In[35]:


ages = re.findall(r'\d{1,3}',s)


# In[36]:


ages


# In[37]:


names = re.findall(r'[A-Z][a-z]*',s)


# In[38]:


names


# In[39]:


dict = {}
x = 0
for i in names:
    dict[i] = ages[x]
    x += 1
print(dict)


# In[40]:


import re
s = ("Kyu bhai kat gya kya? bhai ko lga tha uski wali alag hai")
if re.search("bhai",s):
    print("Mil Gya")


# In[41]:


a = re.findall("bhai",s)
for i in a:
    print(i)


# In[42]:


for i in re.finditer("bhai",s):
    l = i.span()
    print(l)


# In[44]:


import re
str = 'sat,hat,mat,pat'
s1 = re.findall('[shmp]at',str)
for i in s1:
    print(i)


# In[45]:


import re 
f = "hat rat mat pat"
regex = re.compile('[r]at')
f = regex.sub("food",f)
print(f)


# In[46]:


import re 
phn = '888-999-6666'
if re.search("\w{3}-\w{3}-\w{4}",phn):
    print("Sahi number h bhai")


# ## Numpy, Matplotlib and Pandas

# In[47]:


import numpy as np
a = np.array([1,2,3,4,5])
print(a)


# In[49]:


import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)


# In[50]:


import numpy as np
a = np.arange(1,10)
print(a)


# In[51]:


import numpy as np
a = np.arange(1,10,2)
print(a)


# In[52]:


import numpy as np
a = np.arange(5,10,dtype = "complex")
print(a)


# ### Matplotlib

# In[55]:


import numpy as np
import matplotlib.pyplot as plt

data = {'c':200, 'c++':300, 'Java':300, 'Python':400}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (12, 5))

plt.bar(courses, values, color='Maroon', width = 0.4)

plt.xlabel("Course offered")
plt.ylabel("No. of Students enrolled")
plt.title("No. of Students in different course")
plt.show()


# In[58]:


import matplotlib.pyplot as plt

w = 0.4
x = ["CSE","IT","ECE","EE","MECH","CIVIL"]
boys = [100,20,80,60,300,400]
girls = [100,80,40,20,10,20]

plt.bar(x, boys, w, label = "boys")
plt.bar(x, girls, w, bottom = boys, label = "girls")

plt.xlabel("courses")
plt.ylabel("Students")
plt.title("Ratio")
plt.legend()
plt.show()


# In[61]:


import numpy as np
import matplotlib.pyplot as plt

data = [[30,25,50,20],
        [40,23,51,17],
        [35,22,45,19]]
x = np.arange(4)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x + 0.00, data[0], color = 'blue', width = 0.25)
ax.bar(x + 0.25, data[1], color = 'red', width = 0.25)
ax.bar(x + 0.50, data[2], color = 'green', width = 0.25)


# In[62]:


import numpy as np
import matplotlib.pyplot as plt

cars = ["Audi","BMW","Volvo","Ford","Tata","Kia"]
data = [25,30,5,12,70,50]

fig = plt.figure(figsize = (10,7))
plt.pie(data, labels = cars)

plt.show()


# In[ ]:




