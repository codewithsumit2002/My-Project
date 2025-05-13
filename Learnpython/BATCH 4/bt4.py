#to install numpy module:-
#open command prompt and type the below code
#python -m pip install numpy
#or
#pip install numpy


#write a python program to add,sub,multipy,divide of two values.
"""
a=5
b=8
c=a+b
d=a-b
e=a*b
f=a/b
print("Addition",c)
print("Subtraction",d)
print("Multiply",e)
print("Division",f)
"""
"""
#write a python program to find simple interest.
p=500
r=10
t=5
si=p*r*t/100
print("Simple interest=",si)
"""
"""
#Area of circle:- diameter,circumference,radius
r=int(input("Enter the radius:"))
area=3.14*r*r
print("Area of circle=",area)

#Check datatypes
a=2
b=2.5
c="Hello"
d=True
e=1,2,3
f={2,3,5}
h=(10,20,30)
l=[100,200]

print("a=",type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(h))
print(type(l))
"""

"""
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print(a+b)
print(type(a))
"""
"""
firstnumber=int(input("Enter the first number:"))
secondnumber=int(input("Enter the second number:"))
total=firstnumber+secondnumber
print("Total=",total)
"""
"""
a=5 #int
b=2.56 #float
c="Hello" #string
d=False #kuch bhi
e={10,20,30} #set
f=[20,40,60] #list
g=(1,2,3) #tuple
h=10,20,30 #tuple
i={"a":12} #dict
k=2+6j #complex
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(k))
"""
# 16/10/2023 loop:-(Repeat)
"""
while (first execute the program then check the condition)
do while (first check the condition then execute the program)
for loop (condition and execution both run together)

print("sumit")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
"""
"""
a=0
while(a<=10):
    print(a)
    a=a+2 #a++
"""
"""
b=100 #variavle init..
while(b>=1):  #condition
    print(b)
    b=b-1 #increament/decreament
"""
"""
#for loop:-
for a in range(1,101):
    print(a)
"""
#18/10/2023
#if statement:-
"""
a=6
if(a==6):
    print("True")
else:
    print("False")
"""
"""
a=10
if(a==10):
    print("Value of a is 10")
else:
    print("Value of a is not 10")
"""
"""
#Q1:- Write a python program to initialize two numbers and do multiple operations
#+,-,/,*,//,%
a=2
b=3
c=a+b
d=a-b
e=a*b
f=a/b
g=a//b
h=a%b
print("Sum=",c)
print("Sub=",d)
print("multiply=",e)
print("divide=",f)
print("float division",g)
print("Modulus",h)
#Q2:- Write a python program to reverse the two number.

a=10
b=20
c=0

a=20
b=10
"""
#20/10/2023
#Reverse of two number:-
#Method 1st =>
"""
a=2
b=3
c=a
a=b
b=c
print("a=",a)
print("b=",b)
"""
#Method 2nd=>
"""
a=9
b=4
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)
"""
#Method 3rd =>
"""
a=5
b=2
a,b=b,a
print("a=",a)
print("b=",b)
"""
"""
#Q3:- write a program to give the value  to variables in one line and let the
#python take the values.
a,b,c=3,5,6
print("a=",a)
print("b=",b)
print("c=",c)
#Slicing:-
#forward slicing
a="Muskan"
print(a[2:4:1])
#backward slicing
b="Shivani"
print(b[-2:-5:-1])
"""
"""
#23/10/2023
#Q4:- write a python program find the addition,subtraction,multiplication,
#division of two number thorugh input().
x=int(input("Enter the first number="))
y=int(input("Enter the second number="))
print("Addition:",x+y)
print("Subtraction:",x-y)
print("Multiplition:",x*y)
print("Division:",x/y)
print("Modulus:",x%y)
print("Float Division:",x//y)
"""
"""
x="#Q4:- write a python program find the addition,subtraction,multiplication,division of two number thorugh input()."
print(x[])
"""
"""
a="sumit"
b="sumit"
print('u' in a)
print(a is b)
print(id(a),id(b))
"""
#25/10/2023
"""
#Q5-Q18 shapes program using input function:-
#3.14*r*r
r=int(input("Enter the radius:"))
area=3.14*r*r
print("Area of circle:",area)
"""
#26/10/2023
#if statement:-
"""
a=6
if(a==6):
    print("Yes")
else:
    print("No")
"""
#Q19:- Write a python a program to  find age eligibility
"""
age=int(input("Enter the Age:"))
if (age>=18):
    print("Eligible")
else:
    print("Not Eligible")
"""
#Q20:- Write a python a program to find year is leap or not.
"""
year=int(input("Enter the year:"))
if (year%4==0):
    print("Leap year")
else:
    print("Not leap year")
"""
#Q21:- Write a python a program to find number is even or odd.
"""
num=int(input("Enter the number:"))
if (num%2==0):
    print("Even")
else:
    print("Odd")
"""
#27/10/2023
#Check the number is greater and smaller using python.
"""
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
if (a>b):
    print("A is big")
elif (a<b):
    print("B is big")
else:
    print("A and B are equal")

"""
"""
#convertors:-
a=[10,20,30]
print(a,type(a))

c=set(a)
print(c,type(c))
"""
"""
phy=int(input("Enter the marks:"))
chm=int(input("Enter the marks:"))
mth=int(input("Enter the marks:"))
total=phy+chm+mth
print("Total",total)
per=total/300*100
print("Per",per)
if( total<=0 and total>300):
    print("invalid  marks")
elif (per>=95 and per<=100):
    print("Top")
elif (per>=60 and per<95):
    print("First")
elif (per>=45 and per<60):
    print("Second")
elif(per>=33 and per<45):
    print("Third")
else:
    print("Fail")
"""

"""
phy=int(input("Enter the marks:"))
if(phy<=100 and phy>=95):
    print("Top")
elif(phy<95 and phy>=60):
    print("First")
elif(phy<60 and phy>=45):
    print("Second")
elif(phy<45 and phy>=33):
    print("Third")
else:
    print("Fail.")

chm=int(input("Enter the marks:"))
if(chm<=100 and chm>=95):
    print("Top")
elif(chm<95 and chm>=60):
    print("First")
elif(chm<60 and chm>=45):
    print("Second")
elif(chm<45 and chm>=33):
    print("Third")
else:
    print("Fail")

mth=int(input("Enter the marks:"))
if(mth<=100 and mth>=95):
    print("Top")
elif(mth<95 and mth>=60):
    print("First")
elif(mth<60 and mth>=45):
    print("Second")
elif(mth<45 and mth>=33):
    print("Third")
else:
    print("Fail")
total=phy+chm+mth
print("Total:",total)
if(phy<33 or chm<33 or mth<33):
    print("Result Failed")
elif(phy>100 or chm>100 or mth>100):
    print("Invalid Markes")
else:
    print("Passed")
"""
#Q22:- write a python program to find the number is positive or negative.
# F string
"""
a=2
b=2.5
c="Hello"
d=True
e=2+3j
print(f"a={a} b={b} c={c} d={d} e={e}")
"""
#01/11/2023
#continue and break keyword:-
"""
#continue
for i in range(1,11):
    if(i==6 or i==8):
        continue
    else:
        print(i)

#break:
for i in range(1,11):
    if(i==6):
        break
    else:
        print(i)
"""
#Star pattern:-
"""
for i in range(1,7):
    for j in range(1,7):
        print("*",end=" ")
    print()
"""

"""
#Sum of digit:
i=int(input("Enter the number:"))
Sum=0
while(i>0):
    Sum=Sum+i%10
    i=i//10
    print("Sum of digit:",Sum)


#prime number:-
num = 11
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
"""

"""
#fibonacci Series:-
#0,1,1,2,3,5,8,13,.......
n=25
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
"""
"""
#Reverse of digit:-
i=int(input("Enter the number:"))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
    print("Reverse of number:",rev)

#polindrome number:-
#12321,456654,78987
"""
#prime numbers:
"""
n=int(input("Enter the number:"))
if n > 1:
    for g in range(2, int(n/2)+1):
        if(n % g)==0:
            print(n,"n is not prime")
            break
        else:
            print("n is prime")
            break
else:
    print("n is not prime")

"""
"""
n=int(input("Enter the number:"))
if (n==1 or n==0):
    print("Not prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not prime number")
            break
    else:
        print("Prime number")
"""

#Neon number:
"""
n=int(input("Enter the number:"))
sqr=n*n
sum=0
while(sqr>0):
    digit=sqr%10
    sum=sum+digit
    sqr=sqr//10
if(sum==n):
    print("Neon number")
else:
    print("Not neon number")
"""

"""
  j
i *
  **
  ***
  ****
  *****
  
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
"""
*****
****
***
**
*

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
"""
1
22
333
4444
55555
"""
#08/11/2023
#Math module
"""
import math
print("Square Root:",math.sqrt(25))
print("Power:",pow(2,3))
print("Round Off",round(45.6)) #round off
print("Ceil [GIF]",math.ceil(45.1)) #GIF
print("floor",math.floor(12.1)) # return int value
print("Factorial:",math.factorial(5)) #Give fact of number
print("Pi:",math.pi)
"""
# date time module:
"""
import datetime
today=datetime.datetime.now()
print(today)
"""
#Q : display date,month and year partially
"""
from datetime  import date
today= date.today()
print(today.day)
print(today.month)
print(today.year)
"""
#calender

import calendar
print(calendar.month(2023,11))
print(calendar.calendar(3050))

#DD-MM-YYYY
"""
from datetime import date
today=date.today()
print(today.day,'-',today.month,'-',today.year)
print(f"{today.day}-{today.month}-{today.year}")
"""
# Creating a function
"""
def country():
    print("India")
    print("America")
    print("Vietnam")
    print("greenland")
    print("finland")
    print("Turky")
country()
country()
country()
country()
"""
"""
def info():
    print("Ashu")
    print("O level")
    print("2643491221")
info()

#create a function of add_value with two argument,parametere:
def add_value(a,b):
    c=a+b
    print("Add:",c)
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
add_value(a,b)
"""
#Unit converters:
"""
def kmtom(km):
    m=km*1000
    print(m,"meters")
km=float(input("Enter the value in Km:"))
kmtom(km)
"""
"""
11111
2222
333
44
5

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end="")
    print()

"""
"""
k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
"""

    *
   **
  ***
 ****
*****

for i in range(0,5):
    for j in range(5,i-1,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
"""
"""
0
10
010
1010
01010
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

"""
"""
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0 
1 0 1 0 1
0 1 0 1 0


*****
****
  * * *
   * *
    *
"""
"""
for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()


for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
"""
#List:-
"""
List=[1,2,3,4,5,6]
print("List:",List)
List.append(7)
print(List)
List.insert(9,19)
print(List)
List.extend([11,12,13])
print(List)

"""
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
for i in range(5,0,-1):
    #for j in range(1,6):
    for j in range(5,0,-1):
        print(j,end=' ')
    print()
"""
#function with argument with return value:-
"""
def kmtom(km):
    m=km*1000
    return m
n=kmtom(5)
print(n,"Meter")

def squarevalue(num):
    return num*num
n=squarevalue(9)
print("Square Value:",n)


#Max Value of two argument:-
def maxvalue(a,b):
    if a>b:
        print("A is Large")
    elif(b>a):
        print("B is Large")
    else:
        print("both are equal")
maxvalue(7,8)
#Max Value of three argument:-
#Reverse of number using function
"""
"""
import mylib
print("Meter:",mylib.kmtom(2))
print(mylib.squarevalue(8))
"""
#lambda function:-
"""
a=lambda a:a+10
print(a(20))

res=lambda a,b:a+b
print(res(5,3))

res=lambda a,b:a-b
print(res(5,3))


p=lambda p:3.14
print(p(1))

"""
#write a python program to print table using lambda function:-
"""
def table(n):
    return lambda a:a*n
tab=table(3)
for i in range(1,11):
    print(tab(i))


for i in range(1,51):
    print("Table of:",i)
    for j in range(1,11):
        res=i*j
        print(res)
    print()

for i in range(1,21):
    print("table of:",i)
    for j in range(1,11):
        print(i*j,end=" ")
    print()
"""
#tuple:
#print tuple's element using for loop
"""
a=(10,20,40,30,50,60,70,80,90,100)
for i in a:
    print(i)
"""
#find the length of tuple:- condtion don't use len()
"""
tpl=(2,3,4,5,6,4,8,5)
counter=0
for i in tpl:
    counter+=1
print("Total tuple element:",counter)
"""
"""
for i in range(1,6):
    print("A",end=" ")
print()
for j in range(1,6):
    print("B",end=" ")
print()
for k in range(1,6):
    print("C",end=" ")
print()
for l in range(1,6):
    print("D",end=" ")
print()
for m in range(1,6):
    print("E",end=" ")

"""
"""
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E


E E E E E
D D D D D
C C C C C
B B B B B
A A A A A


A B C D E
A B C D E
A B C D E
A B C D E
A B C D E

A A A A A
B B B B
C C C
D D
E
"""
"""
for i in range(5,0,-1):
    print("A",end=" ")
print()

for j in range(4,0,-1):
    print("B",end=" ")
print()

for k in range(3,0,-1):
    print("C",end=" ")
print()
"""
"""
for i in range(1,6):
    for a in range(1,2):
        print("A",end=" ")
    for b in range(1,2):
        print("B",end=" ")
    print()
"""
#find the even odd in given list:-
"""
a=[54,2,6,45,9,8,62,354]
print(a)
for i in a:
    #print(i)
    if (i%2==0):
        print(f"{i}=Even")
    else:
        print(i,"="+"Odd")
"""
"""
num=[54,2,6,45,9,8,62,354]
print(num)
a=list(filter(lambda x:(x%2==0),(num)))
print("Even List:",a)
"""
#seprating odd and even elements:-
"""
List=[56,32,48,96,564,22,754,32,21,78]
even=[]
odd=[]
print(even)
print(odd)
for i in List:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("EVEN List:",even)
print("ODD List:",odd)
"""
#create a list using user input:-
"""
n=int(input("Enter the element you want in your list:"))
a=[]
for i in range(n):
    a.append(int(input("Enter the value:")))
print(a)

"""
#found the position of element in given list:-

"""
List=[25,65,32,48,96,53,2,24]
index()
"""


#random:-
import random

a=random.randint(1,5)
print("Random Number:",a)

"""
a=random.randrange(3,6)
print("Random Number:",a)
"""
"""
print("Random Number:",random.random())
"""
"""
a=random.uniform(1,5)
print("Random Number:",a)
"""




"""
Random Module-
a=randiant(x,y)  #x<=a<=y  x,y are integer 
a=randrange(x,y)  #x<=a<y  x,y are integer
a=random()  #0.1<=a<1.0
a=uniform(x,y) #give random floating number 
choice(x) 
shuffle(x)
"""

"""
#set:-
s={23,47,67}
s
{67, 47, 23}




]
print(type(s))
<class 'set'>
s={1,1,2,2,3,3}
s
{1, 2, 3}
s.add(11)

s
{11, 1, 2, 3}
s.add(12)
s
{1, 2, 3, 11, 12}
list=[1,2,3]
Set=set(list)
Set
{1, 2, 3}
list
[1, 2, 3]
Set1={10,20,30}
Set2={40,50,60}
Set1.update(Set2)
Set1
{50, 20, 40, 10, 60, 30}
#removing element:-
Set1.remove(40)
Set1
{50, 20, 10, 60, 30}
#Union of sets:-
S1={10,20,30,40,50}
S2={10,15,20,25,30}
S1.union(S2)
{40, 10, 15, 50, 20, 25, 30}
#intersection of sets:-
S1.intersection(S2)
{10, 20, 30}
S2.intersection(S1)
{10, 20, 30}
#difference of sets:-
S1.difference(S2)
{40, 50}
S2.difference(S1)
{25, 15}

S1|S2
{40, 10, 15, 50, 20, 25, 30}

S1&S2
{10, 20, 30}

6
x=x*3   x*=3
SyntaxError: invalid syntax
S1-S2
{40, 50}
day={"Monday","Tuesday","Wednesday","thursday","friday","saturday"}
day.add("Sunday")
day
{'Wednesday', 'Tuesday', 'saturday', 'Sunday', 'Monday', 'thursday', 'friday'}

"""
#28/11/2023:-
#dict:-
"""
student={"Name":"Sumit",
         "Age":21,
         "Course":"A level"}
print(type(student))
print("Name=",student["Name"])
print("Age=",student["Age"])
print("Course=",student["Course"])
"""
"""
name=["Sumit","Ashu","Satyam","Anjali","Himanshu","Akanksha","Somdatt","Satyam","Kavita","Kanchan","Pratima","Priyanka","Rupesh"]
age=[21,20,21,20,22,23,21,21,19,10,15]
course=["O level","O level","O level","O level","O level","O level","O level","O level","O level","O level","O level"]
contact=[1234456789,1234456789,1234456789,1234456789,1234456789,1234456789,1234456789,1234456789,1234456789,1234456789,1234456789]
student={"Name":name,"Age":age,"Course":course,"Contact":contact}
for data in student.values():
    for val in data:
        print(val)
    print()

"""
#30/11/23
#File processing (ch-7):-
"""
#Access mode=>
r=read the file
w=write the data create too
a=append the data create too
r+ = read and write data
w+ = write and read data
a+ append,read and write
x= create data does not create a new file.
"""

#write data into the page.
"""
file=open("jkl.txt",'w')
file.write("Python is easy to learn")
file.close()
print("Data wrote successfully")
"""
#read the data from file.
"""
file=open("jkl.txt",'r')
print(file.readline())
file.close()
"""
#create the file
"""
file=open("dca.txt",'x')
print("file is created")
file.close()
"""
"""
file=open("bt4revision.py","r")
print(file.read())
file.close()
"""
#read the data through looping:-
"""
file=open("abc.txt",'r')
for i in file:
    print(i)
file.close()
"""
#read(n), readlines(),writelines()
"""
file=open("abc.txt","a")
file.write("\nPython is interpreted language and simple language.")
file.close()
print("Data added successfully.")
"""
#read(n)
"""
file=open("abc.txt","r")
print(file.read(10)) #read 10 character from file.
file.close()
"""
#readlines()
"""
file=open("abc.txt","r")
print(file.readlines())
file.close()
"""
#writelines():-
"""
file=open("abc.txt","w")
file.writelines(["first line\n","second line\n","third line\n"])
file.close()
"""
"""
file=open("abc.txt","r")
print(file.readlines())
file.close()
"""
#write a python program to copy the content of a file to another file
#tell():-


"""
file=open("abc.txt","r")
print("File Position:",file.tell())
print("1st line:",file.readline())
print("File Position:",file.tell())
print("2nd line:",file.readline())
print("File Position:",file.tell())
print("3rd line:",file.readline())
file.close()
"""
#08/12/2023
#tell():-
"""
file=open("sumit.txt","w")
file.write("Welcome to W3schools")
file.close()
print("File created  successfully")
"""
"""
file=open("sumit.txt","r")
print(file.tell())
file.read(8)
print(file.tell())
print(file.seek(10))
file.close()
"""
#Recursion function():-
"""
def mno():
    print("")
mno()
def abc():
    print("This is a function")
    abc()
abc()
"""
"""
def factorial(n):
    if (n<=1):
        return 1
    else:
        return n*factorial(n-1)
print("Factorial:",factorial(5))
"""
"""
def series(val):
    if (val>=11):
        return 1
    else:
        print(val)
        val=series(val+1)
series(12)
"""
#numpy:-
#09/12/2023:-
#import numpy as np
#create an array:-
# array()
# arange()
# linespace()
"""
#create an array using arange():-
a=np.arange(0,10)
print(a)
"""
"""
#find the major and minor person in the given list:-
age_list=[56,12,53,48,58,32,24,16,64,13]
mj=mn=0
#
for i in age_list:
    if (i>18):
        mj=mj+1
    else:
        mn=mn+1
print("No. of Majors:",mj,"No. of Minors:",mn)
print(f"No. of Majors: {mj} No. of Minors: {mn}")
"""

#linspace():-
"""
import numpy as np
num=np.linspace(1,2,10)
print(num)
"""
"""
#write a python program to find the transpose of a matrix:-
import numpy as np
x=np.array([[1,2],[3,4]])
print("The matrix is:\n",x)
print()
print("Transpose of a given matrix is:\n",x.T)
"""
"""
#Addition of two matrix:-
import numpy as np
x=np.array([[10,20,30],[40,50,60],[70,80,90]])
y=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("The addition of two matrixs is:\n ",x+y)


#Multiplication of two matrix:-
import numpy as np
x=np.array([[10,20,30],[40,50,60],[70,80,90]])
y=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("The addition of two matrixs is:\n ",x*y)

"""
"""
a="s u m i t"
print(a)
b=a.split(" ")
print(b)
print(b[::-1])
"""


"""
a,b=input("Enter the Word:"),[]
for i in a:
    b.append(i)
print(b[::-1])
"""
"""
a="sumit"
print(a[::-1])
"""


"""
import random
pc=random.randint(0,2)

print('User Value:\n Press '0' for Rock \n Press '1' for Paper \n Press '2' for Sessior')
us=int(input("Enter the value:"))

if us==0:
    print("You pressed",us,"for Rock")
elif us==1:
    print("You pressed",us,"for Paper")
elif us==2:
    print("You pressed",us,"for Sessior")
else:
    print("Invalid Value")

if pc==0:
    print("computer pressed",us,"for Rock")
elif pc==1:
    print("computer pressed",us,"for Paper")
elif pc==2:
    print("computer pressed",us,"for Sessior")
else:
    print("Invalid Value")
print("Computer Value",pc)
if (us==0 and pc==0):
    print("Game Draw")
elif (us==0 and pc==1):
    print("Comput win")
elif (us==0 and pc==2):
    print("user win")
elif (us==1 and pc==0):
    print("user win")
elif (us==1 and pc==1):
    print("Game Draw")
elif (us==1 and pc==2):
    print("Computer win")
"""
a={"sumit":10,
   "anjali":20,
   "ashu":30,
   "muskan":40,
   "anchal":50,
   "pratima":60,
   "priyanka":70,
   "rupesh":80,
   "somdatt":90,
   "satyam":100
   }
print(a)
b=[]
print(a["sumit"]+a["anjali"]+a["ashu"])
for i in a:
    if (a[i]>50):
        b.append(i)
print(b)
c=tuple(b)
print(c)
x,y,z,m,n=c
print(x)
print(y)
print(z)
print(m)
print(n)
print()
if (y.startswith("p")==True):
    print(y)
"""
a=["ashu","anjali"]
for i in a:
    if (a.startswith("a")==True):
        print(a)


"""







