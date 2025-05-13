"""
first_value=256
second_value=146
total=first_value+second_value
print(total)
"""
#area,volume,
#area of circle:-
"""
#3.14*r*r (please define r in code)

r=5
area=3.14*r*r
print("Area of circle:",area)
"""
#area of elipse:-
"""
#3.14*a*b
a=3
b=5
area=3.14*a*b
print("Area of elipse:",area)
"""

#concate:-(adding string)
"""
print("Good Morning")
a="I"
b=" Love"
c=" my"
d=" India"
print(a+b+c+d)
"""
#slicing:-(to get sub-string or any character from given string)
"""
a="concatenation"
print(a[3:6]) #sub-string
print(a[::-1]) #reverse
"""

#python data types:-
"""
a=26 #int
b=24.63 #float
c="Hello" #string
d=True #False boolean
e=[1,2,3] #list
f=(4,5,6) #tuple
g={7,8,9} #set
h={1:"abc"} #dict
i=3+6j #complex numbers
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))
print(i,type(i))
"""
#age eligiblity
"""
a=int(input("Enter the age:"))
if (a>=18):
    print("Eligible")
else:
    print("Not Eligible")
"""

#leap year (leap year comes after 4 years):-
"""
a=int(input("Enter the year:"))
if (a%4==0):
    print("Leap Year")
else:
    print("Not leap year")
"""
#even odd:-
"""
a=int(input("Enter the number:"))
if (a%2==0):
    print("Even number")
else:
    print("Odd number")
"""
#greater or smaller:-
"""
a=float(input("Enter the first value:"))
b=float(input("Enter the second value:"))
if (a>b):
    print("A is greater")
elif(b>a):
    print("B is greater")
else:
    print("A and B are equal.")
"""
#loop:-
#while and for:-
"""
a=1
while(a<=1000):
    print(a)
    a=a+1
"""
#nested loop:-
"""
for i in range(0,6):
    for j in range(0,6):
        print("*",end=" ")
    print()
"""
#nested if:-
"""
if(a):
    if(b):
        if():
            if():

"""
#nested if-else:-
"""
if():
    if():
        #statement
    else:
        #statement
else:
    if():
        #statement
    else:
        #statement
"""
#find the number is positive or negative:-
"""
a=int(input("Enter the number:"))
if(a>0):
    print("Positive")
elif(a<0):
    print("Negative")
else:
    print("0 is neutral")
"""
"""
print("He's my friend")
print('"He said to me that",\n muskan is not studying')
"""
#series of number:-(while loop)
"""
a=0
while(a<=50):
    print(a)
    a=a+1
"""
"""
for i in range(0,51):
    print(i,"a")
"""
"""
a=50
while(a>0):
    print(a)
    a=a-1

for i in range(50,0,-1):
    print(i)
"""

#sum of digit:-
"""
i=int(input("Enter the number:"))
Sum=0
while(i>0):
    Sum=Sum+i%10
    i=i//10
    print("Sum of Digit:",Sum)
"""
#Reverse of digit:-
"""
i=int(input("Enter the number:"))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
    print("Reverse of digit:",rev)
"""

#create marksheet:-

    
#star pattern:-
"""
1 11 21 31 41
2 12 22 32 42
.
.
.
.
.
.
.
10 20 30 40 50
"""
"""
for i in range(0,3):
    for j in range(0,3):
        print("+",end=" ")
    print()


i=0
j=7

i=1
j=7

i=2
j=7
"""
#creating function:-
#1. with no arg no return value
#2. with no arg with  return value
#3. with arg no return value
#4. with arg with return value

"""
#1. with no arg no return value
def country():
    print("India")
    print("America")
    print("Finland")
country()
country()
country()
country()
country()
"""
#2. with no arg with  return value
"""
def abc():
    a=5
    return a
var=abc()
print(var)
"""
#3. with arg no return value
"""
def kmtom(km):
    m=km*1000
    print(m,"Meter")
kmtom(5)


"""
#4. with arg with return value
"""
def fit_to_inch(ft):
    inch=ft*12
    return inch
a=fit_to_inch(float(input("Enter the Feet:")))
print(a,"inch")
"""
#math module

#import math
#print(math.pow(2,3))


#calendar

#import calendar
#print(calendar.calendar(2050))


#datetime
#random


#list,tuple,set,dict
"""
a=[20,10,30]
print(a)
"""
#adding element:-
#append() Add single value  
#insert() Add value in particular index
#extend() Add multiple values
#modifying elements
"""
a[1]=50
print(a)
"""
#deleting element:-
"""
remove()
pop()

a=[10,20,30,20,40,50,60]
print(a)

print(a.pop())
print(a)


del a[5]
print(a)
"""
#lambda
a=lambda a:a+10
print(a(20))
c=lambda a,b,d:a+b+d
print(c(3,6,5))
#file processing
#numpy



