"""
print("Good morning")
#F5 - To execute the program
# Use "#" to comment a program
print(2+5/6*9-5)
a=5
b=6
print("The sum of a and b is: ",a+b)

# type() is used to check the data type.
a=5 #int
b=5.69 #float
c="Hello" #string
d=[1,2,3] #list
e=(10,20,30) #tuple
f={4,5,6} #set
g={'name':"Sumit",'roll':123} #dict
h=True #boolean (True or False)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

#area of circle:-
#3.14*r*r
r=10
area=3.14*r*r
print("Area of circle is: ",area)
"""
"""
perimeter
radius
diameter
subtraction of two numbers
multiplication of two numbers
division of two numbers
"""

#02/02/2024
"""
#concatenation:-  (Addition /merge of string)
a="Good "

b='Morning'
c=a+b
print(c)
#slicing:-

#syntax:- a[start:stop:step]
#forward indexing strat form 0.
#backward indexing start from -1.
a="Pizza"
#find the slice of pizza
print(a)
print(a[3:6])
print(a[:])
print(a[0:6:2])
print(a[::-1])



firstname="Satyam"
print(firstname)

lastname="Gautam"
print(lastname)

print(firstname+lastname)
"""
"""
x=9
y=3
print("x+y= ",x+y)
print("x-y= ",x-y)
print("x*y= ",x*y)
print("x/y= ",x/y)
print("x%y= ",x%y)
print("x//y= ",x//y)
print("x+y= ",x+y)
print("x**y= ",x**y)
print(x)

"""
"""
#Bitwise operator:-
op. name               descrip. 
&   AND               sets each bit to 1 if both bits are 1
|   OR                sets each bit to 1 if one of two bits is 1
^   XOR               sets each bit to 1 if only one of two bits is 1
~   NOT               Inverts all the bits.
<<  left shift op.    shifts the bits to left/ bitwise left shift.
>>  right shift op.   shift the bts to right/ bitwise right shift.
"""
#19/02/2024:-
#circle,elipse,triangle,rectangle,square,hexagon,pentagon (area)
#sphere,elipsoid,cuboid,cube (area+volume),cylinder

#Conditional Statement:-
#If ()Take one conditonal only;-
"""
a=int(input("Enter the number: "))
if(a<50):
    print("A is less than 50")
elif(a==50):
    print("A is equal to 50")
else:
    print("A is greater than to 60.")
"""
#write a python program to check the number is even or odd.
"""
num=int(input("Enter the number: "))
if (num%2==0):
    print("Even")
else:
    print("Odd")
"""
"""
#write a python program to check the year is leap or not?
year=int(input("Enter the Year: "))
if(year%4==0):
    print("leap year.")
else:
    print("Not leap year.")
"""
"""
#write a python program to check the age eligibilty.
age=int(input("Enter the Year: "))
if(age>=18 and  age<=75):
    print("Elig.....")
else:
    print("Not Elig.....")
"""
#write a python program to check the number the prime or not?

#While loop:-
"""
#initialization,condition,increament/decreament
x=0
while(x<101):
    print(x)
    x=x+1
"""
#for loop:-
"""
for i in range(0,100,1):   
    print(i)
"""
#Series of even and odd.
"""
#factorial of a number;-
num=int(input("Enter the number: "))
fact=1
while(num>1):
    fact=fact*num
    num=num-1
    print("Factorial: ",fact)
"""
"""
#sum of digit:- (2468=20)
i=int(input("Enter the number: "))
Sum=0
while(i>0):
    Sum=Sum+i%10
    i=i//10
    print("The sum is ",Sum)
"""

"""
num=int(input("Enter the number: "))
for i in range(2,num):
    if(num%i==0):
        print("Not Prime")
        break
    else:
        print("Prime")
        break
"""
"""
if(num==0 or num==1 ):
    print("Not prime")
    
else:
    print("Not prime")
"""
"""
#Conditon Statement;-
#if statement=>
        In statement ka use ye check  kerne ke liye kiya jata hai ki ,
        kya kuch conditions puri ki ja rhi hai ya nhi,  if conditions ka palan
        kiya jata hai to statement ke andar ka code chalaya jata hai.
        example->
                    a=33
                    b=200
                    if(b>a):
                        print("b is greather than a")

#if-else=>
        This is pretty much similar to the if statement the only difference is
        that another block of code ia written inside the else statement which is
        run when the condition of the "if" statement is found to be false.
        example->
                    a=200
                    b=33
                    if(b>a):
                        print("b is greater than a.")
                    else:
                        print("a is greater than b.")
#elif=>
        elif is keyword in python. if recent conditon of "if" was not true then
        interpreater will check this condition.
        example=>
                    a=200
                    b=33
                    if(b>a):
                        print("b is greater than a.")
                    elif(a==b):
                        print("a and b are equal.")
                    else:
                        print("a is greater than b.")



#Loop:-
        python has two primitive loop commands.
        ->While Loop
        ->For Loop
#While Loop=>
        while loop ke saath hum statement ke ek set ko tb tk chala sakte hai
        jb tk ki koi condition sahi ho. jbki loop phele ek condition ko test
        kerta hai yadi condition sahi lagti hai to loop test karta hai ki kya
        uski condition fir se sahi hai ?
        iss process ko tb tk continue rakha jata hai jb tk ki condition false
        na ho jaye. jabki loop ko taiyar hone ke liye relevent variable ko
        define kerne ki need hoti hai, jise i=1 per set kerte hai.
        example->
                #print i as long as i less than 6:
                i=1
                while(i<6):
                    print(i)
                    i=i+1

                #whle loop with break statement:
                    i=5
                    while(True):
                        print("Value of i is ",str(i))
                        i=i+1
                        if(i>=10):
                            break
                    #output:
                            Value of i is 5
                            Value of i is 6
                            Value of i is 7
                            Value of i is 8
                            Value of i is 9
#For Loop=>
            Ek For loop ka use ek order (jo ya to ek list , ek tuple, ek dict
            ek set ya ek str hai ) per punravritti (iterating) ke liye kiya
            jata hai .
            yah other programming languages main paye jane wale iterate method
            ki tarah work kerta hai.
            loop ke liye hum statement ke ek set ko execute ker sakte hai ek
            bar list main pratyek (each) item ke liye , tuple,set aadi(etc..).
            example->
                #print each fruit in a fruit list:

                Fruits=["apple","banana","cherry"]
                for x in Fruits:
                    print(x)
                #note-->the for loop doesn't require an indexing varible to set
                before hand.
#The Break keyword:-
            break keyword ka use loop ke flow ko rokne ke liye  kiya jata hai
            break keyword ke saath hum ek loop ko firse chalne ke liye rok
            sakte hai, bhale hi condition sahi ho 
            
#The Continue keyword:-
            continue keyword ka use loop ke flow k ek step ko skip krne ke liye
            use kiya jata hai or baki ke steps execute hote hai.
#The pass keyword:-
            python programing main pass keyword ek null statement hai. python
            main ek comment or pass keyword main difference hai ki jb
            interpreater kisi comment ko puri tarah se ignore kerta hai jbki
            pass ko ignore nhi kiya jata sakta.

            suppose we have a loop or function  which is not executed yet.
            but we will execute in future but loop or function cannot have an
            empty body. interpreater will raise an error. so we can create an
            empty body using pass keyword which do NOTHING!
            nothing happens when a pass keyword execute.
            It result is NoP(No Operation).

#The assert keyword:-
            code debug "hona chahiye" kerte time assert keyword ka use kiya
            jata hai ("Use assert keyword to create an error."). assert keyword
            aapko test kerne deta hai ki kya aapko code main koi condition true
            hai, if yes, to program ek Asseration Error uthayega (raise) yadi
            code galat hai to aap ek message likh sakte hai.
            #-------------FINISHED!-------------#

"""

#reverse,#palindrome,Neon number
#2468  24642

#palindrome

"""
i=int(input("Enter the number: "))
rev,num=0,i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
    print(rev)
if(num==rev):
    print("Palindrome number")
else:
    print("Not palindrome")
"""
"""
#Neon Number:-
#9**2=81=8+1=9

n=int(input("Enter the number: "))#9
Sum,digit=0,0
sqr=n**2 #81
while(sqr>0):
    digit=sqr%10 #d=1 d=8
    Sum=Sum+digit#s=1 s=9
    sqr=sqr//10#sq=8 sqr=0
if(Sum==n):
    print("Neon number")
else:
    print("Not neon number")
"""
"""
#Simple Marksheet;-
phy=int(input("Enter the number: "))
chm=int(input("Enter the number: "))
mth=int(input("Enter the number: "))
total=phy+chm+mth
per=total/3
print(f"Total={total} and Percentage={per}")
print("Total= ",total,"and Percentage= ",per)
if(per>=95 and per<=100):
    print("top")
elif(per>=60 and per<95):
    print("First")
elif(per>=45 and per<60):
    print("Second")
elif(per>=33 and per<45):
    print("Third")
elif(per>=0 and per<33):
    print("Fail")
else:
    print("Inavild Marks")
"""
#star pattern

"""
#nested loop;-
for i in range(1,6):
    for j in range(1,6):
        print("*",end=' ')
    print()
"""
"""
*****
*****
*****
*****
*****
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
"""
"""
*
**
***
****
*****
"""
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=' ')
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
    *
   **
  ***
 ****
*****
"""
"""
for i in range(0,5):
    for j in range(5,i,-1):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    print()
"""
#DIY
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
"""
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
"""
"""
#math methods:-
import math
print(math.sqrt(196))
print(math.pow(2,3))
print(round(45.6))
print(math.ceil(45.1))
print(math.floor(47.8))
print(math.factorial(5))
print(math.pi)

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




"""
#datetime module:-

import datetime
today=datetime.datetime.now()
print(today)

#Q-1=>write a python program to display date, month and year partially.

from datetime import date
today=date.today()
print("Day:",today.day,)
print("Month:",today.month)
print("Year:",today.year)

#Q-2=> write a python program to display DD-MM-YYY (H.W).

#Q-3=> write a python program to display calendar.
import calendar
print(calendar.month(2024,2))
print(calendar.calendar(2024))
"""
"""
#string methods:-
a="SUMIT"
print(a.capitalize())
print(a.casefold())
print(a.count('u'))
print(a.encode())
print(a.format())
print(a.lower())
"""
"""
 method              description
    
capitalize() ->
casefold() ->
count()
encode()
format()
index()
join()
lower()
replace()
swapcase()
title()
upper()
translate()
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
        print(j,end=' ')
        #print(i,end=" ")
    print()



print()
"""
"""
11111
2222
333
44
5
"""

#functions:-(Set of statments)
#function  no argument with no return value:-
#function  no argument with return value:- 
#function  with argument with no return value:- 
#function  with argument with return value:- 
#syntax
#function  no argument with no return value:-

"""
def abc():
    print("Hello")
    print("Hello ,Good Morning")
    print("Hello, Good Evening")
    print("Hello, What's up")
    print("Hello")
    

abc()
abc()
abc()


def loop():
    for i in range(1,11):
        print(i)
loop()
"""
#function  with argument with no return value:- 
"""
def add_value(a,b):
    c=a+b
    print("Sum:",c)

x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
add_value(x,y)
"""
#add_value(2,3)
#fucntion overloading:- (research about it)


#set of statement-> function 
#set of functions->  module/package/library
"""
1
22
333
4444
55555

1
12
123
1234
12345

11111
2222
333
44
5

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
        #print(i,end=" ")
    print()

#x=15
x=1
for i in range(1,6):
    for j in range(1,i+1):
        print(x,end=" ")
        x=x+1
        #x=x-1
    print()
"""
"""
#km to meter:-
def km_to_m(km):
    m=km*1000
    print(m,"meter")
km_to_m(2)

#Feet_to_inch:-
#function with argument with return value:-
#Square_value:-
def sqr_value(num):
    return num*num
a=sqr_value(9)
print("Square value:",a)

#Feet_to_inch,km_to_m:-


"""
"""
#max three value
def maxthree(a,b,c):
    if(a>b and a>c):
        print("A is Max")
    elif(b>a and b>c):
        print("B is Max")
    else:
        print("C is Max")
maxthree(2,10,8)
#max two value:-(DIY)
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
        if((i+j)%2==0):
            print("0",end="")
        else:
            print("1",end="")
    print()
"""
"""
01010
10101
01010
10101
01010
"""
"""
11111
22222
33333
44444
55555

12345
12345
12345
12345
12345

55555
44444
33333
22222
11111

54321
54321
54321
54321
54321

"""
"""
for i in range(5,0,-1):
    for j in range(1,6):
        print(i,end="")
    print()

"""
"""
#write a program to print a table of two in python.
#write a program to print each element of a string.
a="School"
for i in a:
    print(i)
print(len(a))
#write a program to print cube of first five natural number in descending.
for i in range(5,0,-1):
    print(i**3)
#find the meter from KM
#feet to inch and inch to feet.
x=1.001
y="A"
print(id(x))
print(id(y))
"""
"""
import mylib
a=mylib.kmtom(3)
b=mylib.feettoinch(6)
print(a,"meter")
print(b,"inches")
"""
"""
#write a python program to input the value of x and calculate the result of
#the following  equation.          i**x+cosx+x**1/2  
import math
x=float(input("Enter the value of x:"))
a=math.exp(x)
b=math.cos(x+3.14/180)
c=math.sqrt(x)
d=a+b+c
print("Result:",d)
"""
"""
#write a python program to input the value of the x and y and caluculate the
#result of the following equation.       log((x/y)**1/2)
import math
x=float(input("Enter the value of x:"))
y=float(input("Enter the value of y:"))
a=x/y
b=math.sqrt(a)
c=math.log(b)
print("Result: ",c)
"""
"""
#PEMDAS
exp()
sin()
cos()
tan()
log()
"""
"""

import geometryformulas
a=geometryformulas.circle_area(2)
b=geometryformulas.circle_circum(2)
c=geometryformulas.rec_area(2,5)
d=geometryformulas.rec_peri(2,5)
print("Area of circle is:",a)
print("Circumference ofcircle is:",b)
print("Area of rectangle is:",c)
print("Perimeter of rectangle is:",d)
"""


"""
def abc():
    print("Hello!")
    abc()
abc()
"""
#factorial of number using recursion.
"""
def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)
a=fact(5)
print(a)
"""

#write aprogram to print the fibonacci series without recursion function.
#0,1,1,2,3,5,8,13,21,34,55,......
"""
n=int(input("Enter the number: "))
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
x	y	z	output
0	1	0	0
1	0	1	1
0	1	1	1
1	1	2	2
1	2	3	3
2	3	5	5
3	5	8	8
5	8	13	13
8	13	21	21
13	21	34	
"""
#prime number:-
"""
n=int(input("Enter the number:")) #5
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
"""
method              description
count()     
capitalize()
find()
lower()
islower() 
istitle()
isupper()
replace()
swapcase()
rfind()
strip()
lstrip()
rstrip()
title()
spilt()
isalnum()
isaplha()
isdecimal()
isdigit()
Startswith()
endswith()
encode()

Numeric module:-
Method              Description
input()
eval()
print()
max()
min()
pow()
round()
int()
ceil()
floor()
sqrt()
random()

"""
#random:-
import random
"""
a=random.randint(1,5)
print("Random Number:",a)

a=random.randrange(1,6)
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
#lambda Functions;-
"""
a=lambda a:a+10
print(a(40))

res=lambda a,b:a+b
print("Add:",res(5,7))

res=lambda a,b,c:a+b+c
print("Add:",res(5,7,2))

def table(n):
    return lambda a:a*n
tab=table(int(input("Enter the table number: ")))
for i in range(1,11):
    print(tab(i))

"""
"""
#print natural number 1 to 50. using recursion (DIY)
#type conversion:-
a=[1,2,3]
print(type(a),a)
b=tuple(a)
print(type(b),b)

"""
#List:-
"""
#modifing the element in list:-
a=[10,20,30,40,50,60,70,80,90,100]
print("old list:",a)
a[2]=1000
print("new list",a)

#Adding element in list:-  append()  
a.append(200)
print(a)
a.append(300)
print(a)

#Adding element in list:-  extend([a,b,c]) 
a.extend([1000,2000,3000])
print(a)

#Adding element in list:-  insert(<position>,<argument>) 
a.insert(5,"Sumit")
print(a)


print(a.index("Sumit")) #know the value in which position is stored.

a.reverse() #reverse the list.
print(a)
print("Length:",len(a)) #know the length of list


#Removing element from list:-  pop()
a.pop() #remove element of last indexed
print(a)

a.remove(1000) #remove element from starting index (first find element) 
print(a)

b=[10,10,10,20,30,40]

print(b.count(10)) #count the element.


del(a[2])
print(a) #remove element from it's position
"""
#tuple:-
"""
a=10,20,30,40,50,60
print(type(a),a)
#a.append(80)
print(a[2:4:1])

b=100,
print(type(b),b)
"""

#prolist:-
#check the even and odd element in a given list:
#concatenation op. in list:-
"""
list1=[10,20,30]
list2=[40,50,60]
list3=list1+list2
print(list3)
"""
#Repetition op. in list:-

"""
list1=[10,20,30]
z=list1*3
print(z)
"""
#List comprehension:-

#Syntax:
"""
Output_list= Output_expression for var in inputlist
    if(var satisfies this condition):
"""
"""
list=[]
for i in range(1,11):
    list.append(i**2)
print(list)

"""



"""
a=[45,63,25,94,75,63,26,24,47]
for i in a:
    if(i%2==0):
        print("Even No:",i)
    else:
        print("Odd No:",i)
"""
"""
n=int(input("How many elements you want in a list?"))
num=[]
for i in range(n):
    num.append(int(input("Insert the Element:")))
print("Elements are:")
print(num)
"""
#check the even and odd element in a given list using lambda function:
"""
a=[45,63,25,94,75,63,26,24,47]
res1=list(filter(lambda x:(x%2==0),(a)))
res2=list(filter(lambda x:(x%2==1),(a)))
print("Even:",res1)
print("Odd:",res2)
"""

#get the lenght of a given list without using count() and len():
"""
a=[45,63,25,94,75,63,26,24,47]
count=0
for i in a:
    count=count+1
print(count)
"""
"""
a=[45,63,25,94,75,63,26,24,47]
sval=int(input("Enter the element to search:"))
for i in a:
    if(i==sval):
        print("Element found")
else:
    print("not found")
"""

#tuple generator:
"""
tpl=(i*2 for i in range(1,15))
for i in tpl:
    print(i)
print(type(tpl))
"""

#tuple packing and unpacking:
"""
a=10
b=2.45
c=True
d="Hello"
e=3j
tup=(a,b,c,d,e)
print(type(tup),tup)
"""
"""
tup=(10,2.26,"hi",True)
a,b,c,d=tup
print(f"a={a} b={b} c={c} d={d}")
"""
#set
"""
s={10,20,30,40,50}
s
{50, 20, 40, 10, 30}
s
{50, 20, 40, 10, 30}
s
{50, 20, 40, 10, 30}
s
{50, 20, 40, 10, 30}
s
{50, 20, 40, 10, 30}
s
{50, 20, 40, 10, 30}
s
{50, 20, 40, 10, 30}
s={10,20,30,40,50,60}
s
{50, 20, 40, 10, 60, 30}
print(type(s))
<class 'set'>
s.add(11)
s
{50, 20, 40, 10, 11, 60, 30}
s,add(12)
Traceback (most recent call last):s
  File "<pyshell#14>", line 1, in <module>
    s,add(12)
NameError: name 'add' is not defined
s.add(12)
s
{50, 20, 40, 10, 11, 60, 12, 30}
for i in s:
    print(i)

    
50
20
40
10
11
60
12
30
print(s[2])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(s[2])
TypeError: 'set' object is not subscriptable
a=list(s)
a
[50, 20, 40, 10, 11, 60, 12, 30]
s
{50, 20, 40, 10, 11, 60, 12, 30}
b=tuple(s)
b
(50, 20, 40, 10, 11, 60, 12, 30)
a
[50, 20, 40, 10, 11, 60, 12, 30]
s
{50, 20, 40, 10, 11, 60, 12, 30}
#removing element:
s.remove(40)
s
{50, 20, 10, 11, 60, 12, 30}
s1={10,20,30}
s2={40,50,60}
s1.update(s2)
s1
{50, 20, 40, 10, 60, 30}
s2.update(s1)
s2
{40, 10, 50, 20, 60, 30}
test={1,2,1,5,6,2,4,5,3,4,8,9,2}
test
{1, 2, 3, 4, 5, 6, 8, 9}
s1.union(s2)
{40, 10, 50, 20, 60, 30}
set1={10,20,30,10,40,50}
set2={50,60,80,10,90,70}
set1.union(set2)
{70, 40, 10, 80, 50, 20, 90, 60, 30}
set1.intersection(set2)
{50, 10}
x={1,2,3}
y={}
x.intersection(y)
set()
s1={10,20,30,40,50}
s2={10,15,20,25,30}
s1.difference(s2)
{40, 50}
s2.difference(s1)
{25, 15}
s1|s2
{40, 10, 15, 50, 20, 25, 30}
s1&s2
{10, 20, 30}
s1-s2
{40, 50}
s2-s1
{25, 15}


"""
#dictionary:-
"""
dict1={1:"Sumit","roll_no.":1467639}
print(type(dict1),dict1)

data={
    "Name":{"name1":"sumit","name2":"akash","name3":"raj"},
      "course":"A Level",
      "Roll_no.":1467675
      }
print(data["Name"]["name2"])
print(data["course"])
print(data["Roll_no."])

"""
"""
#pop():-
d={1:100,2:200,3:300}
print(d)
print(d.pop(2))
print(d)

#popitem():-
d={1:100,2:200,3:300}
print(d)
print(d.popitem())
print(d)

#clear():-
d={1:100,2:200,3:300}
print("old dict:",d)
d.clear()
print("new dict:",d)

#del keyword:-
d={1:100,2:200,3:300}
print(d)
del d[2]
print(d)
"""
"""
#update():-
dict1={'a':10,'b':20}
dict2={"c":30,"d":40}
dict2.update(dict1)
print("dict2:",dict2)
"""
"""
name=["Shreya","Soumya","Anamika","KK","Prateek","Om"]
age=[19,20,23,21,20,21]
course=["CCC","DCA","PGDCA","12th","O level","O level"]
roll=[101,102,103,104,105,106]

student={"Name":name,"Age":age,"Course":course,"Roll_no":roll}
for data in student.values():
    
    for val in data:
        print(val,end="")
    print()


"""
"""
List=[(2,3,8),(4,7,1),(6,5,2),(9,2,4)]
print("The max of index 0:",max(List[0]))
print("The max of index 1:",max(List[1]))
print("The max of index 2:",max(List[2]))
print("The max of index 3:",max(List[3]))
"""

#File Handling with Python:-
#Access Modifier:-

"""
r=read the file
w=write the data
a=append the data
r+=read and write the data
w+=write and read the data
a+=append,read and write
x=create data

read(5):-

"""
#how to write data in python.
"""
file=open("xyz.txt","w")
file.write("This is an example of how to write data in python.\n")
file.write("This is an example of how to write data in python.\n")
file.write("This is an example of how to write data in python.\n")
file.close()
print("Data written successfully.")
"""
#how to read data in python. (using functions)
"""
file=open("abc.txt","r")
print(file.read())
#print(file.read(6))
#print(file.readline())
#print(file.readlines())

file.close()
print("file read successfuly")
"""
"""
#how to read data in python. (without functions)
file=open("xyz.txt","r")
for i in file:
    print(i)

#how to create file usign python.
file=open("def.html","x")
print("file has been created.")
    
file=open("def.html","w")
file.write("<html><head></head><body><h1>This is a heading</h1></body></html>")
file.close()
print("file reading......")
"""
"""
#writelines():-
file=open("mnop.txt","w")
file.writelines(["This is a first line\n","This is a secind line.\n","this is a third line"])
file.close()
print("Data written.")
"""

#write a python program to write a list to a file.
#method 1
"""
language=["Python ","JAVA ","c++ ","c ","Ruby ","perl ","GO ","Swift ","C# "]
file=open("lang.txt","w")
file.writelines(language)
file.close()
print("Data written.")


file=open("lang.txt","r")
print(file.read())
file.close()
"""
#method 2
"""
language=["Python ","JAVA ","c++ ","c ","Ruby ","perl ","GO ","Swift ","C# "]
with open("tkd.txt",'w') as  myfile:
    for i in language:
        myfile.write("%s\n"%i)
content=open("tkd.txt")
print(content.read())
"""
"""
#write a python program to copy the content of a file to another.
new_file=open("demo.txt","w")
with open("tkd.txt","r") as f:
    new_file.write(f.read())    
new_file.close()
"""
#write a python program to read a random line from a file:-
"""
import random
def random_line(fname):
    lines=open(fname).read().splitlines()
    return random.choice(lines)
print(random_line("demo.txt"))
"""
#write a python program to check the file is close or not?
"""
file=open("demo.txt","r")
print(file.closed)
file.close()
print(file.closed)
"""


#write a python program that read the content of string and count the number
#of alphabets, lower case and upper case, digits and number of words.
"""
def Count(str):
    alpha=0
    upper=0
    lower=0
    digit=0
    word=0
    for i in range(len(str)):
        if str[i]>="A" and str[i]<="Z":
            upper+=1
            alpha+=1
        elif str[i]>="a" and str[i]<="z":
            lower+=1
            alpha+=1
        elif str[i]>="0" and str[i]<="9":
            digit+=1
        elif str[i]==():
            word=0
        print("Total character:",len(str))
        print("Total Alphabets:",alpha)
        print("Total Upper case:",upper)
        print("Total Lower case:",lower)
        print("Total Digits:",digit)
        print("Total Words:",len(str.split(" ")))
str="Naini Prayagraj Pin 211008"
Count(str)
"""
"""
Str="Naini Prayagraj Pin 211008"
print(Str.split(" "))

"""
#shuffle()
"""
import random
a=["Stawberry","Dragon fruit","Kiwi","Black grapes"]
random.shuffle(a)
print(a)
"""
 
"""
import random
#Game 1:-  (Head or Tail)
coin=["Head","Tail"]
print("Coin:",random.choice(coin))

#Game 2:- (Choose Dice)
dice=[1,2,3,4,5,6]
print("Dice:",random.choice(dice)

"""
"""
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

"""
"""
#Command line argument:-
from sys import argv
Sum=0
args=argv[1:]
for i in args:
    Sum=Sum+int(i)
print(Sum)
"""
#tell()
"""
file=open("abc.txt","r")
print("File position:",file.tell())
print("First Line:",file.readline())
print("File position:",file.tell())
print("Second Line:",file.readline())
print("File position:",file.tell())
print("Third Line:",file.readline())

file.close()
print('\nSeek():-\n')
#seek()
file=open("abc.txt","r")
print("File position:",file.tell())
print("First old Line:",file.readline())
print("File position",file.seek(7))
print("First new Line:",file.readline())

file.close()
"""
"""
#Scope:
pi="Outer pi value"
def pifun():
    pi="inner pi value"
    print(pi)
pifun()
print(pi)

#LEGB Rule:-
def outer_function():
    a=20
    def inner_function():
        a=30
        print("a:",a)
    inner_function()
    print("a",a)
a=10
outer_function()
print("a:",a)
"""
#to install numpy module:-
#open command prompt and type the below code
#python -m pip install numpy
#or
#pip install numpy

#Creating array using array():-
"""
import numpy as np
a=np.array([[10,20,30],[40,50,60],[70,81,90]])
#b=np.array([21,48,23])
print(a)
#print(b)
"""
#Creating array using arange():-
"""
import numpy as np
x=np.arange(2,4,2);
print(x)
"""

#Creating array using linspace():-
"""
import numpy as np
x=np.linspace(1,3,5)
print(x)
"""

"""
import numpy as np
age=[15,13,20,12,22,35,49,20,14,23]
mj=0
mn=0
for a in age:
    if (a>=18):
        mj=mj+1
        
    else:
        mn=mn+1
        
print("No. of Major:",mj,"\nNo. of Minor:",mn)

for i in age:
    if(i%2!=0):
        print("ODD:",i)
"""
#N-D Array:-
"""
#single  dimensional Numpy array:-
import numpy as np
a=np.array([1,2,3])
print(a)

#Two dimensional Numpy array:-
import numpy as np
a=np.array([(10,20,30),(40,50,60)])
print(a)


#Thre dimensional Numpy array:-
import numpy as np
a=np.array([(10,20,30),(40,50,60),(70,80,90)])
print(a)
"""

#write a python program to find the transpose of a matrix
"""
import numpy as np
a=np.array([[1,2],[3,4]])
print("Original matrix:\n",a)
print("Transpose of a Matrix:\n",a.T)
"""


"""
#shape():-
import numpy as np
a=np.array([[10,20,30],[40,50,60]])
print("The Matrix is:\n",a)
a.shape=(3,2)
print("\n")
print(a)

"""
"""
#ndim:-
import numpy as np
a=np.arange(24)
print(a)
a.ndim
print(a)
b=a.reshape(2,4,3)
print(b)
"""
#some function:-
"""
import numpy as np
a=np.zeros(5)
b=np.ones(5)
c=np.eye(3)
d=np.empty(5)
print(a)
print(b)
print(c)
print(d)
"""
"""
import random
import numpy as np
num=np.random.random((1,5))
n=np.random.normal(1,5,(2,3))
print(num)
print(n)
"""
import numpy as np
#copy():
"""
a=np.array([10,20,30,40,50])
print("A:",a)
b=a.copy()
print("B:",b)
"""

#empty()
"""
x=np.empty([3,2],dtype=int)
print(x)
print(np.ones(5,dtype=int))
print(np.zeros(5,dtype=int))
print(np.identity(5,dtype=int))
print(np.eye(2,dtype=int))
"""
"""
a=np.array([10,20,30,40,50])
print(a[1:3])


l=[1,2,3,4,56,0,7,8,9]
print(type(l),l)
x=np.asarray(l)
print(type(x),x)
"""

"""
x=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(x)
arr=np.asmatrix(x)
print(arr)
#change the value
x[0,2]=55
print(x)
arr=np.asmatrix(x)
print(arr)
"""










