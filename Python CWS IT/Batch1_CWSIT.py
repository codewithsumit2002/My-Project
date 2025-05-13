"""
#Add two number
#first_number=15#number (int)
#second_number=20#number (int)
#addition=first_number+second_number
#print(addition)

#Sub of Two no.
x=100
y=10
z=x-y
print("Subtraction:",z)

#Multiplication and division of two number
a=10
b=2
c=a/b#c=a*b
print(c)
"""
#26/01/2025
"""
#Formula
#cirle (parameter[2*pi*r], area[pi*r*r], radius[d/2])
r=6
para=2*3.14*r
print("Parameter:",para)

r=10
area=3.14*r*r
print("Area:",area)
"""


"""
a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
print(a+b)
print(type(a))
print(type(b))


#concatenation=merging or two or more string
a=2
b=3
c=4
d=a+b+c #addition
print(d)

m="Ankita "
n="Shreya "
o="Prachi"
p=m+n+o#merge ,concatenation
print(p)
"""
"""

#rectangle (area[h*l],diagonal[2(h+l)])
h=int(input("Enter the heigth:"))
l=int(input("Enter the length:"))
area=h*l
print("Area:",area)

#homework (radius,diagonal)

"""

#backward indexing:-
#Syntax:  <strobj>[begin:end:step]
#slicing
"""
a="concatenation"

c=-13
o=-12
n=-11
c=-10
a=-9
t=-8
e=-7
n=-6
a=-5
t=-4
i=-3
o=-2
n=-1

print(a[::-1])
"""
#by default value
"""
forward:
    begin:0
    end:length of string
    step:+1

Backward:
    begin:-1
    end:length

"""
#noitanetacnoc
#Q:- write a python program to get
#substring from a string. that is given by-
# string->"python is easy to learn"
#substring->"is easy"
"""
a="python is easy to learn"
print(a[-7:-14:-1]) #is easy
print(a[2:9:1])
print(a[-2:-9:-1])
#Q:- write a python program to get
#substring from a string. that is given by-
# string->"python is easy to learn"
#substring->"ot ysae","thon is","rael ot"
"""
"""
#rectangle:
#parameter: (2(h+w))-> 2*h+2*w
h=int(input("enter the height:"))
w=int(input("enter the width:"))
para=2*h+2*w
print("Parameter:",para)

#square:
#area[s*s]
s=int(input("enter the side:"))
a=s*s
print("area: ",a)

#triangle area[(b*h)/2]
h=int(input("enter the height:"))
b=int(input("enter the base:"))
area=(b*h)/2
print("Area of triangle:",area)
"""
"""
#arthmatic operation:-
x=17
y=5
print("x+y",x+y)
print("x-y",x-y)
print("x*y",x*y)
print("x/y",x/y)#quotient
print("x%y",x%y)#remainder / modulus
print("x**y",x**y)#exp
print("x//y",x//y)#floor division
"""


#circle,elipse,triangle,rectangle,square,hexagon,pentagon (area)
#sphere,elipsoid,cuboid,cube,cylinder,(area+volume)
"""
#write a python program to reverse of two numbers.(with 3rd varibale)
a=6 #b->8
b=8 #a->6
c=a
a=b
b=c
print("A:",a)
print("B:",b)
"""
"""
import math
s=9
area=(3*math.sqrt(3)*s*s)/2
print(area)

print(math.pow(2,3))

a=8
b=3
a=a+b #a=11
b=a-b #b=8
a=a-b #a=3
print("a:",a)
print("b:",b)
"""
"""
a=19
if(a>=18):
    print("you are eligible for vote.")
else:
    print("Not eligible")
"""
"""
a=100
b=100
if(a>b):
    print("A is greater")
elif(a==b):
    print("equal")
else:
    print("B is greater")

"""
"""
age=int(input("Enter the Number: "))
if(age>18):
    print("You are slected")
elif(age==18):
    print("Equal")
else:
    print("Not Selected")
"""
"""
val=input("Enter the Character: ")
if(val=='Shreya'):
    print("Shreya is selected")
elif(val=="Prachi"):
    print("Prachi is selected")
elif(val=="Ankita"):
    print("Ankita is selected")
else:
    print("Someone else is selected")
"""
#greater and smaller
#positive and negative
"""
a=int(input("Enter the Value of a: "))
b=int(input("Enter the Value of b: "))
if(a>b):
    print("A is greater")
elif(b>a):
    print("B is greater")
else:
    print("Both are Equal.")
"""
"""
x=int(input("Enter the number: "))
if(x>0):
    print("Positive")
elif(x<0):
    print("negative")
else:
    print("neutral")
"""
#check the number is even or odd.
"""
number=int(input("Enter the number: "))
if(number%2==0):
    print("Even")
else:
    print("Odd")
    """
#check the year is leap or not.
"""
year=int(input("Enter the year: "))
if(year%4==0):
    print("Leap year.")
else:
    print("Not leap year.")
"""


#Loop:-(Repeat)
#while loop
#for loop
"""
for i in range(1,6):
    print("sumit ",end='')
"""
"""
#marksheet:-
chm=int(input("Enter the number: "))
math=int(input("Enter the number: "))
phy=int(input("Enter the number: "))
total=chm+math+phy
print("Total:",total)
per=total/3
print("Per: ",per)
if(per>=100):
    print("Top")
elif(per>=60):
    print("Second")
elif(per>=40):
    print("Third")
else:
    print("Fail")

"""
"""
for i in range(0,5):
    for j in range(0,5):
        print("*",end=' ')
    print()
"""
"""
a=float(input("Enter the number: "))
if(a>0):
    print("Number is Positive")
    print("COlOR")
    print("Computer")
elif(a<0):
    print("Number is Negative")
else:
    print("Number is Neutral")
"""
"""
Fruits=["Apple","Banana","Kiwi","Cherry"]
for i in Fruits:
    if(i=="Kiwi" or i=="Apple"):
        pass
    else:
        print(i)
"""
"""
x=5
assert x>10,"x should be greater than 10."
"""
#18/02/2025
"""
#Q:- Write a program to find the series of numbers
i=50
while(i<=100):
    print(i,end=",")
    i+=1 #i=i+1

for i in range(1,101):
    print(i)
"""
#Q;- write a program to find the table of any number.
"""
x=19
while(x<=190):
    print(x)
    x=x+19

"""

#write a program to find the sum of digit.[57143=20]
"""
i=int(input("Enter the number: "))
Sum=0
while(i>0):
    Sum=Sum+i%10
    i=i//10
    print("Sum of Digit=",Sum)

"""
"""
#Q:- write a program to get the factorial of the number
#6!=6*5*4*3*2*1=720
#5!=120=5*4*3*2*1
x=int(input("Enter the number:"))#3
fact=1
while(x>0):
    fact=fact*x
    x=x-1
    print("Factorial:",fact)
    
"""
#20/02/2025
#print series of even numbers:
"""
for i in range(2,101,2):
    print(i)
"""
#print series of odd numbers:
"""
for i in range(1,101,2):
    print(i)
"""
#palindrome number: [19891,2354532]
#Reverse of digit: [1234 => 4321,8542=>2458]
"""
i=int(input("Enter the number:"))#5871
rev=0
num=i
while(i>0):
    rev=(rev*10)+i%10 #sum=sum+i%10   1
    i=i//10 #587
print(rev)
if(rev==num):
    print("Palindrome Number")
else:
    print("Not Palindrome number")
"""

#using break and continue keyword:
"""
for i in range(1,11):
    if(i==6):
        continue #break
    else:
        print(i)
"""


#Neon number: [9**2=81=9]
"""
n=int(input("Enter the number:")) #9
Sum=0
i=n
sqr=n**2
#print(sqr)
while(sqr>0):
    Sum=Sum+sqr%10
    sqr=sqr//10
if(Sum==i):
    print("Neon number")
else:
    print("Not neon number")

"""
#Sum of digit
#reverse of digit
#palindrome number
#Neon number
#21/02/2025
#Star Patterns:-
#Nested loops: (The loop inside another loop is called nested loop)
"""
for i in  range(1,6):
    for j in range(1,6):
        print("*",end=' ')
    print()
"""
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
"""
*
**
***
****
*****
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()
"""
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end='')
    print()
"""
"""
*****
****
***
**
*
"""
"""
1
22
333
4444
55555
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()
"""
"""
1
12
123
1234
12345
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()
"""
"""
11111
2222
333
44
5
"""
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end='')
    print()
"""
#22/02/2025
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
"""
k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end=' ')
        k=k+1
    print()
"""
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
"""
for i in range(0,5):
    for j in range(5,i,-1):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end=' ')
    print()
"""
"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
#24/02/2025
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
        if((i+j)%2==0): 
            print("0",end='')
        else:
            print("1",end='')
    print()

"""
#h.w.
"""
01010
10101
01010
10101
01010
"""
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
"""
for i in range(1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()
"""

"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
"""
for i in range(1,6):
    for j in range(1,6):
        print(j,end=' ')
    print()
"""
#h.w.
"""
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
"""

"""
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
"""
"""
for a in range(1,6):
    print("A",end=' ')
print()
for b in range(1,6):
    print("B",end=' ')
print()
for c in range(1,6):
    print("C",end=' ')
print()
for d in range(1,6):
    print("D",end=' ')
print()
for e in range(1,6):
    print("E",end=' ')
print()
"""
#H.W.
"""
E E E E E
D D D D D
C C C C C
B B B B B
A A A A A
"""
"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
"""
"""
for i in range(1,6):
    for a in range(1,2):
        print("A",end=' ')
    for b in range(1,2):
        print("B",end=' ')
    for c in range(1,2):
        print("C",end=' ')
    for d in range(1,2):
        print("D",end=' ')
    for e in range(1,2):
        print("E",end=' ')
    print()
"""
#H.W.
"""
A A A A A
B B B B
C C C
D D
E
"""
#25/02/2025
#math module (library,package=> set of functions,instructions,statements)
"""
import math
print(math.sqrt(25))
print(math.pow(2,3))
print(round(45.7))
print(math.ceil(51.5))
print(math.floor(45.1))
print(math.factorial(6))
print(math.pi)

print(dir(math))
"""
#calendar module
"""
import calendar
print(calendar.month(2025,2))
print(calendar.calendar(2063))
"""

#datetime module
"""
from datetime import date
today=date.today()
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

import datetime
today=datetime.datetime.now()
print(today)
print(dir(datetime))
"""
#26/02/2025
#List: (seqn data type ,list dynamic,list mutable h)
"""
#How to create a list
integer=[1,2,3,4,5,6,7,8,9,10,11,12,13]
Float=[1.25,2.35,25.6,45.9]
String=["Sumit","Shreya","Ankita","Ankita","Prachi","Aryan","Priya"]
Bool=[True,False]
Complex=[2+6j,5-8j]
Mix=[1,2.5,"Aryan",True]

#How to access the value
print(Mix[3])

num=[5,2,18,5,6]
print(num)
print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])

#To Change the value of a list:
num[0]=10
num[1]=20
num[2]=30
num[3]=40
num[4]=50
print(num)
#To add the value in a list:
#append(),insert(),extend()
#append(): add a single value at a time at last
num.append(60)
print(num)
num.append(70)
num.append(80)
print(num)
#insert(): add a single value in a specific position/index
num.insert(2,"Sumit")
num.insert(4,"Apple")
print(num)
#extend(): add a multiple values at last
num.extend(["hi","Hello","hlo","hey","Hola"])
print(num)
print(len(num))
rep=[10,10,20,30,10,20,30,50]
print(rep.count(30))
#to delete a value
#remove(),pop()
#remove(): removes a specific value from list
print(num)
num.remove("Apple")
print(num)
print(rep)
rep.remove(10)
print(rep)


rep.remove(10)
print(rep)

rep.remove(10)
print(rep)

#pop(): removes a value from last
print(num)
num.pop()
print(num)

print(num[4:7])
print(num[::-1])

for i in num:
    print(i)

"""
"""
number=[10,20,30,40,50,60]
print(number[0]+number[1])#30
#h.w.
#Q-1: number[-5]+number[5] 80
#Q-2: print(num[6]-number[3]) Error
#Q-3: print(number[2]*number[-3]) 1200
"""

#prolist:
"""
num=[25,67,85,25,45,24,65,89]
for i in num:
    if(i%2==0):
        print("Even",i)
    else:
        print("Odd",i)
"""
"""
#dynamic user input list:
n=int(input("How many element in the list?:"))
num=[] #empty list
for i in range(n):
    val=int(input("Enter the value:"))
    num.append(val)
print("Elements are:",num)
"""
#find the binary number of decimal
"""
binnum=[]
num=int(input("Enter the number:")) #7
while num>0:
    i=num%2
    binnum.append(i)
    num=num//2
print(binnum[::-1])

"""
#H.W.
"""
#find the octal and hex of decimal
print(bin(10))
print(oct(14))
print(hex(15))
"""
"""
num=[34,12,34,45,77,65,89,32,15,12]
oddlist=list(filter(lambda x:(x%2==1),(num)))
print(oddlist)
"""
#04/03/2025
#tuple:-
"""
tpl=(10,20,30)
print(tpl)
print(type(tpl))
print("tpl[0]:",tpl[0])
print("tpl[1]:",tpl[1])
print("tpl[2]:",tpl[2])
"""
"""
#tuple packing:
a=10
b=2.2
c="hello"
d=3+4j
e=True
tpl=(a,b,c,d,e)
print(tpl)

#tuple unpacking
tple=(11,2.25,6+7j,"CWS IT",False)
a,b,c,d,e=tple
print("a=",a,"b=",b,"c=",c,"d=",d,"e=",e)
#f_string
print(f"a={a} \nb={b} \nc={c} \nd={d} \ne={e}")

r=5
area=3.14*r*r
print(f"Area {area}")
"""
"""
#tuple comprehension:
tpl=(x*5 for x in range(1,11))
for x in tpl:
    print(x)
print(type(tpl))
"""
#counţ the number of elements in tuple without using len():
"""
tpl=(10,20,30,40,50,60)
counter=0 #0+1=1,1+1=2,2+1=3,.....,5+1=6
for i in tpl: #i=iteration
    counter=counter+1
    print(i)
print(f"Total Number of element is:{counter}")
"""
#check the element is exist in the given tuple or not?
"""
tup=(23,45,56,16,95,36,24,56,16,35,75)
sval=int(input("Enter the element to search: ")) #53
idx=0
for i in tup:
    if(i==sval):
        print("Found on index:",idx)
        break
    idx=idx+1
else:
    print("Not found")
        
"""
#type conversion:-
#number <--> str,list <-->tuple,set
"""
list()
tuple()
set()
dict()
int()
float()
str()
bool()
"""
"""
a=5
print("Value=",a,type(a))
b=float(a)
print("Value=",b,type(b))
c=str(a)
print("Value=",c,type(c))
List=[10,50,20,6,30]
print("Value=",List,type(List))
tpl=tuple(List)
print("Value=",tpl,type(tpl))
Set=set(List)
print("Value=",Set,type(Set))
"""
#Dictionary:-
"""
dct={1:"Amit","Name":"Sumit",3:"Dipanshu",4:"Zaheer"}
print(dct)
print(dct["Name"])
dct[5]="Gaurav"
print(dct)
#delete
print(dct.pop(3))
print(dct)
print(dct.popitem())
print(dct)
print(dct.clear())
print(dct)
"""
"""
#find the maximum value in the list:-
List=[(2,3,8),(4,7,1),(8,11,12),(3,6,8)]
print("The list iṡ:"+str(List))
print("The max of index 0:",max(List[0]))
print("The max of index 1:",max(List[1]))
print("The max of index 2:",max(List[2]))
print("The max of index 3:",max(List[3]))
"""
#08/03/2025
#dict:- collection of items(key and value)
#key must be unique,key can not be duplicate
#use braces {} and comma to separate items
"""
ADCA={
    "Amit":{
        "ID":1001,
        "NAME":"AMIT BADAL",
        "COURSE":"ADCA",
        "ADD":"URUWA",
        "MOB":6598563241
        },
   " Prachi":{
        "ID":1002,
        "NAME":"PRACHI",
        "COURSE":"ADCA",
        "ADD":"URUWA",
        "MOB":6598543241
        },
    "Ankita":{
        "ID":1003,
        "NAME":"ANKITA GUPTA",
        "COURSE":"ADCA",
        "ADD":"URUWA",
        "MOB":9856343241
        }
}
print(ADCA)
print("Details:-")
print(ADCA["Ankita"])
"""
"""
name=["Priya","Preeti","Shreya","Mahima"]
age=[18,19,18,19]
course=['BCA','B.TECH','MCA','M.TECH']
contact=[9632587456,8563256985,5698524569,8598745236]
Student={'Name':name,"Age":age,"Course":course,"Contact":contact}
print(Student)
for data in Student.values():
    for val in data:
        print(val)
    print()
"""
#Set:- collection of items,duplicates are not allowed,indexing is not allowed
#==== RESTART: C:\Users\Sumit\OneDrive\Desktop\Python CWS IT\Batch1_CWSIT.py ====
"""
Set1={10,20,30,40,50}
Set2={10,15,20,25,30}
Set1
{50, 20, 40, 10, 30}
Set2
{20, 25, 10, 30, 15}
Set1.union(Set2)
{40, 10, 15, 50, 20, 25, 30}
Set1.intersection(Set2)
{10, 20, 30}
Set2.difference(Set1)
{25, 15}
Set1.difference(Set2)
{40, 50}
Set1|Set2
{40, 10, 15, 50, 20, 25, 30}
Set1&Set2
{10, 20, 30}
Set1-Set2
{40, 50}
Set2-Set1
{25, 15}
Set1*Set2
"""
#Prime number:


#Functions:-
"""
def my_function():
    print("Hello world")


my_function()


def my_fun(fname):
    print("Hello "+fname)

my_fun("Shreya")
my_fun("Ankita")
my_fun(input("Enter the name:"))
"""
#Add two number
"""
def add(a,b):
    print(a+b)


x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))

add(x,y)
    

def area(r):
    area=3.14*r*r
    print(area)

area(5)
"""

"""
def info():
    print("Sumit")
    print("A level")
    print("630771")
info()

info()

def python():
    print("Easy to use and learn.")
    print("Expressive lang or interpreter based")
    print("Free and open source")
    print("GUI")

python()
info()
"""
#18/03/2025
"""
def sumValue(a,b,c,e,f,g):
    d=a+b+c+e+f+g
    print(d)
sumValue(2,3,4,4,5,6)
def area_of_circle(r):
    a=3.14*r*r
    print("Are of circle:",a)
area_of_circle(6)

def area_of_rectangle(h,l):
    a=h*l
    print("Area of Rectangle:",a)
area_of_rectangle(4,6)
"""
#Converter:
"""
def ktm(k):
    m=k*1000
    print(m,"meter")
ktm(float(input("Enter the kilometre:")))


def fti(f):
    i=f*12
    print(i,"inch")
fti(float(input("Enter the fit:")))

def dtr(d):
    r=d*87.06
    print(r,"Rupees")
dtr(float(input("Enter the Doller:")))
"""
"""

def mtk(m):
    k=m/1000
    print(k,"km")
mtk(500)


def itf(i):
    f=i/12
    print(f,"fit")
itf(36)
"""
#function with arguments with no return value
#function with arguments with return value
#function with no arguments with no return value
#function with no arguments with return value
"""
def fti(f):
    i=f*12
    return i
print(fti(6))

def sqr(n):
    return n*n
print(sqr(9))
"""
"""
def maxValue(a,b):
    if (a>b):
        print(a)
    elif(b>a):
        print(b)
    else:
        print(f"{a} and {b} are Equal.")
maxValue(9,9)

"""
#19/03/2025
"""
def maxthree(a,b,c):    
    if(a>b and a>c):
        print("A is Large.")
    elif(b>a and b>c):
        print("B is Large.")
    else:
        print("C is Large.")

x=int(input("Enter the value of a:"))
y=int(input("Enter the value of b:"))
z=int(input("Enter the value of c:"))

maxthree(x,y,z)
"""
"""
if(4>8 and 4>10):
    print("True")
else:
    print("False")
"""
"""
T and T ->T
T and F ->F
F and T ->F
F and F ->F

T or T->T
T or F->T
F or T->T
F or F->F

"""
"""
if(4>8 or 4>10):
    print("True")
else:
    print("False")
"""
"""
1->True,On
0->False,Off
And Gate:
Y=A.B,'.'->and gate


A.B=Y
1.1=1
1.0=0
0.1=0
0.0=0



or Gate:
Y=A+B, '+'->or Gate


A+B=Y
1+1=1
1+0=1
0+1=1
0+0=0

not Gate:
A Y
0 1
1 0

"""

#Reverse of digit
"""
def reverse(num):
    i,rev=0,0
    while(num>0):
        i=num%10
        rev=rev*10+i
        num=num//10
    print(rev)
reverse(1234)
"""

#Accessing the module/package/library in the program
"""
import testfunction
print("meter",testfunction.ktm(5))
print("inch",testfunction.fti(10))
"""
#21/03/2025
#lambda function:iss fucntion m ek line m code ko likha ja skta h
"""
add=lambda a,b,c:a+b+c
print(add(2,5,3))

#print table:
def table(n):
    return lambda a:a*n
tab=table(5)
for i in range(1,11):
    print(tab(i))
"""
"""
#print the table from 1 to 20
for i in range(1,21):
    print("Table no.=",i)
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()
"""
#prolist:
"""
num=[25,66,85,22,45,24,65]
even=[]
odd=[]
for i in num:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
"""
"""
n=int(input("How many element you want in the list?:"))
num=[]
for i in range(n):
    num.append(int(input("Insert the value:")))
print("Element are:",num)
"""


#28/03/2025

#Access mode:
"""
r=Read the file
w=write the data
a=append the data
r+=read and write data
w+=write and read data
a+=append,read and write data
x=create data.
"""

#read the data from the file:
"""
file=open("prachi.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
"""
#write the data onto the file
"""
file=open("my_student.txt","w")
file.write("Ankita gupta is a Good student.\n")
file.write("Amit is a Good student.\n")
file.write("Ankita is a Good student.\n")
file.write("Preeti is a Good student.\n")
file.write("Prachi is a Good student.\n")
file.write("Shreya is a Good student.\n")
file.close()
print("Data written successfully")
"""
#append/add data onto the file:
"""
file=open("my_student.txt","a")
file.write("This line will be added to your existing file.")
file.close()
"""
#create the file:-
"""
file=open("new_file.txt","x")
print("File created.")
"""
#read the data from loop:
"""
file=open("my_student.txt","r")
for i in file:
    print(i)
file.close()
"""
#29/03/2025
#readlines:-
"""
file=open("my_student.txt","r")
print(file.readlines())#returns the list of lines
file.close()
"""
#writelines:
"""
Car=["BMW ","AUDI ","MINI COOPER ","VOLKSWAGON ","MERCEDES "]
file=open("mycars.txt","w")
file.writelines(Car)
file.close()

f=open("mycars.txt","r")
for i in f:
    print(i)
f.close()
"""
"""
file=open("mycars.txt","r")
print(file.tell()) #return the cursor position in a file
print(file.read(10))
print(file.read(2))
print(file.tell())
print(file.read(8))
print(file.tell())
#cursor position is 20

#seek()->set the cursor position in a file

print("Old Cursor position:",file.tell())
file.seek(15)
print("New cursor position:",file.tell())
file.close()
"""

"""
alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"]
file=open("alpha.txt","w")
file.writelines(alphabets)
file.close()
"""
"""
f=open("alpha.txt","r")
for i in f:
    print(i)
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read(4))
print(f.tell())
f.seek(2)
print(f.tell())
print(f.read(5))
f.close()
#write a python program to write a list to a file.
lang=["python ","java ","Net ","HTML ","C++"]
with open("language.txt","w") as mylang:
    for i in lang:
        mylang.writelines(lang)
content=open("language.txt")
print(content.read())
"""
#01/04/2025
#prime numbers
"""
Num=int(input("Enter the number:"))#21
if Num>1: #21 prime ho bhi skta h or nhi bhi
    for i in range(2,int(Num/2)+1):#2,3,4,5,6,7,8,9,10
        if(Num%i==0):#21%2==0
            print(Num,"is not a prime number.")
            break
    else:
        print(Num,"is a prime number.")
else:
    print(Num,"is not a prime number")
"""
"""
#check the character is vowel or not?
#intermediate
def isVowel(ch):
    str="aeiouAEIOU"
    return (str.find(ch)!=-1)
print(isVowel('U'))

#easy
vowel=['a','e','i','o','u','A','E','I','O','U']
user=input("Enter the character:")
for v in vowel:
    if(v==user):
        print("Vowel")
        break
else:
    print("Consonent")
"""
#02/04/2025
#recursion fucntion: when a function calls iteself is called recusion fucntion
"""
def abc():
    print("Shreya is a good girl.")
    abc() #recursive call
abc() #function call
"""
"""
def Series(val):
    if(val>=11):
        return 1
    else:
        print(val)
        val=Series(val+1)
Series(1)
"""
#factorial
"""
def fact(a):
    if(a<=1):
        return 1
    else:
        return a*fact(a-1)
print("factorial:",fact(5))

"""

#03/04/2025
#local Scope
"""
x=20 #global
def abc():
    print("Local:",x)
abc()
print("global:",x)
"""
"""
def abc():
    x=10 #local
    print("Local:",x)
abc()
print("Global:",x)
"""

#nonlocal scope
"""
def outer():
    x=30
    def inner():
        nonlocal x
        x=40
        print("Inner x:",x)
    inner()
    print("Outer x:",x)
outer()
"""
#07/04/2025
#BMI Calculator:- (Body mass index)=w/h*h
"""
weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in meter:"))
bmi=weight/height**2
print("You BMI is:",bmi)
if(bmi<=18):
    print("You are underweight")
elif(bmi>18 and bmi<25):
    print("Your are normal")
else:
    print("You are overweight.")

"""

#Love Calculator:-
"""
name1=input("What's your name?")
name2=input("What's your partner name?")
name=name1+name2
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
true=t+r+u+e
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
love=l+o+v+e
true_love=str(true)+str(love)
love_score=int(true_love)
if(love_score<10 or love_score>=80):
    print(f"Your score is {love_score}%. and you go together like coke and mentos")
elif(love_score>=40 and love_score<=50):
    print(f"Your score is {love_score}%. and you are alright together.")
else:
    print(f"Your score is {love_score}%.")

"""
#numpy
#08/04/2025
import numpy as np

#array():-
"""
age=np.array([10,20,30,40,50])
print(age)
"""
#arange():
"""
even=np.arange(0,20,2)
print(even)
print(np.arange(0,10,2))
"""
#linspace():-
"""
x=np.linspace(0,1,10)
print(x)
"""
#09/04/2025
#Single dimensional array:
#print(np.array([10,20,30]))


#Two dimensional array:
#print(np.array([[10,20,30],[40,50,60]]))

#Three dimensional array:
#a=np.array([[10,20,30],[40,50,60],[70,80,90]])
#print("The Original Matrix is:\n",a)
#print("The Transpose of a Matrix is:\n",a.T)
import numpy as np
"""
print(np.array([10,20,30],dtype=int))
print(np.zeros(6))
print(np.ones((3,3)))
print(np.full((3,3),5))
print(np.eye(3))
print(np.empty(3))

num=np.array([[10,20,30],[40,50,60]])
print(num)
print(num.reshape(3,2))
"""
#random:-
import random
#a=random.randint(1,5)
#print("Random Number:",a)
#a=random.randrange(1,6)
#print("Random Number:",a)
#print("Random Number:",random.random())
#a=random.uniform(1,5)
#print("Random Number:",a)
"""
Random Module-
a=randiant(x,y)  #x<=a<=y  x,y are integer #1-a-10
a=randrange(x,y)  #x<=a<y  x,y are integer #1,6
a=random()  #0.1<=a<1.0
a=uniform(x,y) #give random floating number 
choice(x) 
shuffle(x)
"""
#shuffle()
"""
import random
a=["Stawberry","Dragon fruit","Kiwi","Black grapes"]
print("Original:",a)
random.shuffle(a)
print("Shuffle:",a)
"""

#Game 1:-  (Head or Tail)
#coin=["Head","Tail"]
#print("Coin:",random.choice(coin))

#Game 2:- (Choose Dice)
#dice=[1,2,3,4,5,6]
#print("Dice:",random.choice(dice))


#Game 3:- Rock Paper Scissor:
import random
com=["Rock","Paper","Scissor"]
user=["Rock","Paper","Scissor"]
random.shuffle(com)
random.shuffle(user)
#print("Com:",com)
#print("User:",user)
c=random.choice(com)
u=input("Enter Your Choice:")
if(c=="Rock" and u=="Rock"):
    print("Draw\n","Computer choice:",c,"\nand\n","User choice:",u)
    
elif(c=="Rock" and u=="Paper"):
    print("User wins\n","Computer choice:",c,"\nand\n","User choice:",u)

elif(c=="Rock" and u=="Scissor"):
    print("Computer wins\n","Computer choice:",c,"\nand\n","User choice:",u)

elif(c=="Paper" and u=="Rock"):
    print("Computer wins\n","Computer choice:",c,"\nand\n","User choice:",u)

elif(c=="Paper" and u=="Paper"):
    print("Draw\n","Computer choice:",c,"\nand\n","User choice:",u)
    
elif(c=="Paper" and u=="Scissor"):
    print("User wins\n","Computer choice:",c,"\nand\n","User choice:",u)

elif(c=="Scissor" and u=="Rock"):
    print("User wins\n","Computer choice:",c,"\nand\n","User choice:",u)
    
elif(c=="Scissor" and u=="Paper"):
    print("Computer wins\n","Computer choice:",c,"\nand\n","User choice:",u)
    
elif(c=="Scissor" and u=="Scissor"):
    print("Draw\n","Computer choice:",c,"\nand\n","User choice:",u)
    
else:
    pass
print("Thanks For playing\n Never come again  ")









