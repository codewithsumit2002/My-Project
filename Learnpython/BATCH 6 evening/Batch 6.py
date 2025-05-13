"""
#Evening batch:-
print("Hello world!")
a=5.6
b=6.9
print("The sum of two  number is:  ",a+b)
"""

#check data type:- : ->colon  ; ->semicolon
a=5 #int
b=6.2 #float
c="Hello" #string
d=True #boolean
e=[1,2,3] #List
f=(10,20,30)#tuple
g={1,2,3,4} #set
h={1:"Good",2:"morning"} #dict
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

"""
print("His father's name is")


#concatenation:- (Addition of string)
a="Hello "
b="Everyone"
print(a + b)


#Subtraction of two numbers
#Multiplication of two numbers
#Division of two numbers

#Area of circle:- (3.14*r*r)
r=5
area=3.14*r*r
print("Area of circle: ",area)

#parametre
#diametre
#radius

a="Concatenation"
print(a)
print(a[::-1])

#<strobj>[begin:end:step]


a=int(input("Enter the first no.:"))
b=int(input("Enter the Second no.:"))

print(a+b)
"""
"""
#arthmatic operation:-
x=15
y=4
print("x+y",x+y)
print("x-y",x-y)
print("x*y",x*y)
print("x/y",x/y)
print("x%y",x%y)
print("x**y",x**y)
print("x//y",x//y)

print("Hello")
print("The Additon of two number is: ",45+96)
a=63.25
b=54
c=a+b
print(c)


print(type(a))


#concatenation:-(merging of strings)

x="Good "
y='Afternoon'
z=x+y
print(z)

#Slicing:-

y='Afternoon'
print(y[1:5])
print(y[::-1])


#Area of circle:-(3.14*r*r)
r=3
area=3.14*r*r
print("Area of circle is : ",area)

#perimeter of rectangle:- 2(l+b)
l=5
b=7
peri=2*l+2*b
print("Perimeter of rectangle:",peri)

#circle,elipse,triangle,rectangle,square,hexagon,pentagon (area)
#sphere,elipsoid,cuboid,cube (area+volume),cylinder
"""
"""
#taking input from user:-
a=float(input("Enter the First No.: "))
b=float(input("Enter the Second No.: "))
print(a+b)
print(type(a))
"""
"""
#write a python program to reverse of two numbers.(with 3rd varibale)
a=20
b=13
c=a
a=b
b=c
print("a:",a)
print("b:",b)
"""
"""
#write a python program to reverse of two numbers.(without 3rd variable)
a=4
b=6
a=a+b #a=10
b=a-b #b=4
a=a-b #a=6
print("a:",a)
print("b:",b)
"""
"""
#conditional statement:- if
x=2
if (x==5):
    print("X is equal to 5")

else:
    print("X is not equal to 5")


#write a python program to check the age eligibility.
age=float(input("Enter your age: "))
if(age>=18):
    print("You are eligible.")
else:
    print("You are not eligible.")

"""
"""
#write a python program to check the number is even or odd.
num=int(input("Enter the number: "))
if(num%2==0):
    print("Even")
else:
    print("odd")
"""
"""
#write a python program to check the year is leap year or not?
year=int(input("Enter the year: "))
if(year%4==0):
    print("Leap year")
else:
    print("Not leap year")

#17/02/2024
#write a python program to check the number is positive or negative.
num=float(input("Enter the number: "))
if(num>0):
    print("positive")
elif(num==0):
    print("Zero")
else:
    print("Negative")
"""

#loop;- (initialization,condition,increament/decreament)
#while loop (first check the condition then execute the program.)
#do while loop (first execute the program then check the condition.)
#for loop (similar to while loop)
"""
#counting 1 to 10 using while loop:-
x=0
while(x<=100):
    print(x)
    x=x+1
"""
"""
#Back counting 10 to 1 using while loop:-
x=10
while(x>=1):
    print("X=",x)
    x=x-1
"""
"""
#counting 1 to 10 using for loop:-

for i in range(0,10,1):
    print(i)
"""



"""
#prime number:-
num = int(input("Enter the number: "))
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
#using of break,continue, pass keyword:-
#break:-
for i in range(0,10):
    if (i==8):
        break
    else:
        print(i)
#continue:-
for j in range(0,10):
    if(j==3 or j==5 or j==7):
        continue
    else:
        pass
"""
"""
#find the factorial of a number:- (without recursion function)
num=int(input("Enter the number: "))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
    print("Factorial: ",fact)
"""
#print table of 19 using while loop:
#print series of natural numbers till 1000.

"""
#sum of digit 4568
i=int(input("Enter the number: "))
Sum=0
while(i>0):
    Sum=Sum+i%10
    i=i//10
    print("Sum of Digit: ",Sum)
"""
"""
#reverse of digit 8654

i=int(input("Enter the number: "))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
    print(rev)
"""
#palindrome number:-   (12321)
"""
i=int(input("Enter the number: "))
rev=0
num=i

while(i>0):
    rev=(rev*10)+i%10
    i=i//10
    print(rev)
if(num==rev):
    print("Palindrome number")
else:
    print("Not Palindrome number")
"""
"""
#Simple Marksheet:-
chm=int(input("Enter the number: "))
phy=int(input("Enter the number: "))
mth=int(input("Enter the number: "))
total=chm+phy+mth
print("Total: ",total)
per=total/3
print("Percentage: ",per)
if (per>=95 and per<=100):
    print("Top")
elif(per>=60 and per<95):
    print("First")
elif(per>=45 and per<60):
    print("Second")
elif(per>=33 and per<45):
    print("Third")
elif(per>=0 and per<33):
    print("Fail")
else:
    print("Invalid")
"""
"""
#21/02/2024
#Conditional Statement;-
#if statement=>
        In statement ka use ye check  kerne ke liye kiya jata hai ki ,
        kya kuch conditions puri ki ja rhi hai ya nhi,yadi conditions ka palan
        kiya jata hai to statement ke andar ka code chalaya jata hai.
        example->
                    a=33
                    b=200
                    if(b>a):
                        print("b is greater than a")

#if-else=>
        This is pretty much similar to the if statement the only difference is
        that another block of code is written inside the else statement which is
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
        define kerne ki need (jarurat) hoti hai, jise i=1 per set kerte hai.
        example->
                #print i as long as i less than 6:
                i=1
                while(i<6):
                    print(i)
                    i=i+1

                #while loop with break statement:
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

                Fruits=["apple","banana","cherry","dragon fruit"]
                for x in Fruits:
                    print(x)
                #note-->the for loop doesn't require an indexing varible to set
                before hand.
#The Break keyword:-
            break keyword ka use loop ke flow ko rokne ke liye  kiya jata hai
            break keyword ke saath hum ek loop ko firse chalne ke liye rok
            sakte hai, bhale hi condition sahi ho .  
#The Continue keyword:-
            continue keyword ka use loop ke flow k ek step ko skip krne ke liye
            use kiya jata hai or baki ke steps execute hote hai.
#The pass keyword:-
            python programing main pass keyword ek null statement hai. python
            main ek comment or pass keyword main difference hai ki jb
            interpreter kisi comment ko puri tarah se ignore kerta hai jbki
            pass ko ignore nhi kiya jata sakta.

            suppose we have a loop or function  which is not executed yet.
            but we will execute in future, but loop or function cannot have an
            empty body. interpreater will raise an error. so we can create an
            empty body using pass keyword which do NOTHING!
            nothing happens when a pass keyword execute.
            It result is NoP(No Operation).

#The assert keyword:-
            code debug "hona chahiye" kerte time assert keyword ka use kiya
            jata hai ("Use assert keyword to create an error."). assert keyword
            aapko test kerne deta hai ki kya aapke code main koi condition true
            hai, if yes, to program ek Asseration Error uthayega (raise), yadi
            code galat hai to aap ek message likh sakte hai.
            #-------------FINISHED!-------------#by @epsilon.creations

"""
"""
#Neon Number:-
n=int(input("Enter the number: "))#9
Sum=0
sqr=n**2#81
while(sqr>0):
    digit=sqr%10#1 #8
    Sum=Sum+digit#1 #9
    sqr=sqr//10#8 #0

if(Sum==n):
    print("Neon Number")
else:
    print("Not Neon number.")
"""
#Nested loop
"""
*****
*****
*****
*****
*****
"""
"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end="")
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
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
"""
#23/02/2024:-
"""
*****
****
***
**
*
"""
"""
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

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
        print(i,end="")
        #print(j,end="")
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
#math methods in python:-
import math
print(math.sqrt(196))
print(math.pow(2,3))
print(round(45.5))
print(math.ceil(46.1))
print(math.floor(27.8))

print(math.factorial(5))
print(math.pi)
"""
#Date-time in python:-
"""
import datetime
today=datetime.datetime.now()
print(today)
"""
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end=' ')
    print()
 
print()
"""
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
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5  
"""
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
"""
#Q-1=> write a python program to display date,month and year partially.
from datetime import date
today=date.today()
print("Day= ",today.day)
print("Month= ",today.month)
print("Year= ",today.year)

#Q-2=>write a python program to display DD-MM-YYYY (H.W)
from datetime import date
today=date.today()
print(today.day,"-",today.month,"-",today.year)

#Q-3=> write a python program to display calendar.
import calendar
print(calendar.month(2024,2))
print(calendar.calendar(2024))
"""
#string methods in python:-
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
#functions:- (set of statements)
#function  no argument with no return value:-
#function  no argument with return value:- 
#function  with argument with no return value:- 
#function  with argument with return value:- 


#function  no argument with no return value:-
#syntax:-
"""
def function_name():
    statements......
    

function_name()
"""
"""
def abc():
    print("Python is easy to use")
    print("Free and open source")
    print("Dynamically typed")
    print("Interpreter language")
    print("GUI Based")
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
    print("Add: ",a+b)
x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
add_value(x,y)
"""
#find the area of rectangle using function:- and do with all shapes(hw)
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
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
"""
"""
0 1 0 1 0
1 0 1 0
0 1 0
1 0 
0 

"""
"""
def km_to_m(km):
    m=1000*km
    print(m,"meter")
x=float(input("Enter the number:"))
km_to_m(x)
"""
#feetttoinch:-
#function  with argument with return value:- 
"""
def kmtom(km):
    return 1000*km

a=kmtom(6)
print(a,"meters")

def feettoinch(ft):
    return ft*12
a=feettoinch(6)
print(a,"inchs")
"""
"""
def mtokm(m):
    return m/1000
a=mtokm(5000)
print(a,"Km")

def maxthree(a,b,c):
    if(a>b and a>c):
        print("A is max")
    elif(b>a and b>c):
        print("b is max")
    elif(a==b and a==c):
        print("All values are equal.")
    elif(a==b and a!=c):
        print("A and B are equal.")
    elif(b==c and b!=a):
        print("B and C are equal.")
    else:
        print("c is max")
maxthree(15,15,15)

#maxtwo:-(DIY)

"""
"""
#Creating a Module/Package;-
#accessing the module in the program:-
import xyz
a=xyz.sub_value(5,3)
b=xyz.add_value(5,6)
print(a)
print(b)
c=xyz.sqr_value(9)
print(c)
"""

"""
def reverse_digit(i):
    rev=0
    while(i>0):
        rev=(rev*10)+i%10
        i=i//10
        print(rev)
reverse_digit(1234)

#sum of digit:- (using function)
"""
"""
import math
#cos()
log()
b=math.cos(30)
print(b)
"""
#write a program to input the value of x and calculate the result of the
#following equation.   i**x+cosx+x**1/2
"""
import math
x=float(input("Enter the value of x: "))
a=math.exp(x)
b=math.cos(x+3.14/180)
c=math.sqrt(x)
d=a+b+c
print("Result: ",d)
"""
#write a program to input the value of x and y. Calculate and print the result
#of the following equation:-     log(x/y)**1/2
"""
import math
x=float(input("Enter the value of x: "))
y=float(input("Enter the value of y: "))
a=x/y
b=math.sqrt(a)
c=math.log(b)
print("Result",c)
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

#recursion function:-
"""
def abc():
    print("Rohan is a good boy :)")
    abc()
    
abc()
"""
"""
for i in range(1,21):
    print("table no.",i)
    for j in range(1,11):
        print(i*j)
    print()

"""
"""
#factorial of a number using recursion
def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)
print("Fact:",fact(5))

#print natural number 1 to 50. using recursion
"""
"""
from datetime import date
from datetime import time
import datetime
today=date.today()
print("Today's date: ",today)
today.day => current day
today.month => current month
today.year => current year
today.weekday() => (0-6)

"""
"""
calendar.calendar(<year>,<w>,<l>,<c>)
where,
c=
w=
l=
"""
"""
import calendar
print(calendar.calendar(2024,w=3,l=1,c=6))

time();- 12:00 am ,january 1,1970


time.time()
"""
"""
import time
t=time.time()
print("No. of seconds:",t)
"""
"""
localtime():- epoch


time.localtime()
import time
a=time.localtime()
print("Current time:",a)
"""

"""
ctime():-
"""
"""
time.ctime()


import time
a=time.ctime()
print("Current time:",a)
"""
"""
import time
print(time.sleep(5))
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
"""
import random

a=random.randint(1,5)
print("Random Number:",a)

a=random.randrange(1,6)
print("Random Number:",a)

print("Random Number:",random.random())

a=random.uniform(1,5)
print("Random Number:",a)
"""
"""
Random Module-
a=randint(x,y)  #x<=a<=y  x,y are integer 
a=randrange(x,y)  #x<=a<y  x,y are integer
a=random()  #0.1<=a<1.0
a=uniform(x,y) #give random floating number 
choice(x) 
shuffle(x)
"""

#print natural number 1 to 50. using recursion (DIY)

"""
import random
a=random.randint(1,5)
if(a==1):
    print("a is 1")
elif(a==2):
    print("a is 2")
elif(a==2):
    print("a is 3")
elif(a==2):
    print("a is 4")
else:
    print("a is 5")
"""
#type conversion:-
"""
a="6"
print(type(a),a)
b=int(a)
print(type(b),b)
c=float(b)
print(type(c),c)
x=True
print(type(x),x)
y=int(x)
print(type(y),y)

"""
"""
#lambda function():-
res=lambda a,b:a+b
print(res(2,3))

res=lambda a:a+10
print(res(20))

def table(n):
    return lambda a:a*n
tab=table(int(input("Enter the table no.:")))
for a in range(1,11):
    print(tab(a))
"""
#List:-
"""
array-> array is used to store multiple values in a single variable of same
data types

List-> array is used to store multiple values in a single variable of different
data types
"""
"""
a=[10,"hello",2.45,True]
print(type(a),a)
print(a[1])

a=[10,20,30,40,50,60,70,80,90,100]
print("Length",len(a))
"""
"""
#adding elements in a list:- append(52),extend([<values>]),insert(<pos>,<val>)
print(a)
a.append(300)
print(a)
a.extend([400,500,600])
print(a)
a.insert(2,1000)
print(a)

a[0]=4546
print(a)
print("Length",len(a))

#Removing elements  from a list:- del,pop(),remove()  
print(a)
a.pop() #remove element from last index
print(a)

a.remove(30) #remove first finding element.
print(a)

del (a[2]) #remove element from particular position.
print(a)

print(a.index(400)) #return the index of the value.

b=[10,10,10,20,30,40]
print(b.count(10))

a.reverse()
print(a)
print(a[::-1])


x=[[10,20,30],[40,50,60]]
print(x[0][1])
"""
#tuple:-
"""
a=(10,20,30,40,50,60,70,80,90,100)
print(type(a),a)
b=[40,50,60]
print(type(b),b)
#a[0]="hello"  #won't work
#print(a.append(50))  #won't work

x=list(a)   #changeing tuple into list.
print(type(x),x)

print(a[3:6]) #slicing on tuple
for i in a:
    print(i)
"""

#prolist
"""
num=[25,45,67,10,89,14,97,16,79,18,69,57,43]
for i in num:
    print("index of:",i,"=",num.index(i))
"""
#check the element is even or odd in given list:
"""
num=[25,45,67,10,89,14,97,16,79,18,69,57,43] 
for i in num:
    if(i%2==0):
        print("even no:",i)
    else:
        print("Odd no:",i)
"""
"""
num=int(input("How many element in the list you want?"))
n=[]
for i in range(num):
    val=int(input("Insert the value:"))
    n.append(val)
print("Elements are:")
for j in n:
    print(j)
""""""
n=int(input("Enter the element you want in your list:"))
a=[]
for i in range(n):
    a.append(int(input("Enter the value:")))
print(a)
"""
"""
#check the element is odd in given list using lambda function:-
num=[25,45,67,10,89,14,97,16,79,18,69,57,43]
a=list(filter(lambda x:(x%2==0),(num)))
b=list(filter(lambda x:(x%2==1),(num)))
print(a)
print(b)
"""
#check the lengthof list without any function
"""
num=[25,45,67,10,89,14,97,16,79,18,69,57,43]
count=0
for i in num:
    count=count+1
    #print(i)
print("Total element:",count)
"""
"""
num=[25,45,67,10,89,14,97,16,79,18,69,57,43]
sval=int(input("Enter the value to search:"))

for i in num:
    
    if(num.index(i)==i.index(sval)):
        print("Element Found")
        
else:
    print("Not found")
        
"""
"""
#concatenation operator in list:-
list1=[10,20,30]
list2=[40,50,60]
list3=list1+list2
print(list3)

#Repetition operator in list:-
list1=[10,20,30]
z=list1*4
print(z)

#list Comprehension:-
list=[]
for i in range(1,11):
    list.append(i**2)
print(list)
"""
#tuple generator:- iterating 
"""
tpl=(i*1 for i in range(1,11))
for i in tpl:
    print(i)
print(type(tpl))

"""

#tuple packing:-
"""
a=10
b=2.45
c="Hello"
d=True
e=3j
tpl=(a,b,c,d,e)
print(type(tpl),tpl)
"""
"""
#tuple unpacking:-
tpl=(20,"good",2.369,False,1+3j)
a,b,c,d,e=tpl
print(f"a={a} \nb={b} \nc={c} \nd={d} \ne={e}")
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
"""
#dictionary:-
#create a dictionary
dict={}
print()
dict[1]='aaa'
dict[2]='bbb'
dict[3]='ccc'

print(dict)
#Access data from dictionary
print(dict[1])
print(dict[2])
print(dict[3])
#updating element in a dictionary
dict[2]='hello'
print(dict)

"""


#{key:value}
"""
dict1={1:{100:"Hello",101:"Good"},
       "roll":101,
       "name":["Rohan","Anand","Raj","Prince"]
       }
print(type(dict1),dict1)
print(dict1["roll"])
print(dict1[1])
print(dict1["name"][3])
print(dict1[1][101])
"""
#pop():-
"""
d={1:100,2:200,3:300,4:400}
print(d)
print(d.pop(2))
print(d)
"""
#popitem():-
"""
d={1:100,2:200,3:300,4:400}
print(d.popitem())
print(d)
"""
"""
#clear():-
d={1:100,2:200,3:300,4:400}
d.clear()
print(d)
"""
#del keyword:-
"""
d={1:100,2:200,3:300,4:400}
del d[1]
print(d)
"""
#Dictionary concatenation:-
"""
#using update();-
d1={"a":10,"b":20}
d2={"c":30,"d":40}
d2.update(d1)
print(d2)
"""
"""
#Find the max value in the given list:-
List=[(2,5,9),(3,4,7),(1,0,6),(8,6,1)]
print("The List is:"+str(List))
res1=max(List[0])
res2=max(List[1])
res3=max(List[2])
res4=max(List[3])
print("The max index of 0:"+str(res1))
print("The max index of 1:"+str(res2))
print("The max index of 2:"+str(res3))
print("The max index of 3:"+str(res4))

"""


"""
name=["kajal","Mamta","Durga","Khusboo","Nandani","Vaibhav","Shivam","Subhas"]
age=[21,22,20,20,21,23,21,24]
course=["O level","PGDCA","BCA","ITI","IIT","ITI","DCA","A level"]
roll=[101,102,103,104,105,106,107,108]
student={"Name":name,"Age":age,"Course":course,"Roll":roll}

"""

#File Processing:- (File Handling in python)
#Access modifires=>
"""
w=write the data
r= read the data
a= append the data
w+ = write and read the data
r+ =read and write the data
x= create new file
"""
#create new file:
"""
file=open("rose.txt","x")
file.close()
print("File created.")
"""
#write the data in a file: (using write()) (for multiple lines)
"""
file=open("lily.txt","w")
file.write("Python is easy to learn.\n")
file.write("Python is open sourced.\n")
file.write("Python is GUI Based.\n")
file.close()
print("Data written.")
"""
#write the data in a file: (using writelines())
"""
file=open("Lotus.txt","w")
file.writelines(["Python\n","JS\n","C\n","PHP\n","c++\n","Ruby\n"])
file.close()
print("Data written.")
"""

#read the data from a file:(read(n))
"""
file=open("Lotus.txt","r")
print(file.read())
file.close()
"""
#read the data from a file:(readline())
"""
file=open("Lotus.txt","r")
print(file.readline())
print(file.readline())
file.close()
"""
#read the data from a file:(readlines())
"""
file=open("Lotus.txt","r")
print(file.readlines())
file.close()
"""
"""
#write a python program to write a list to a file:
language=["Python\n","JS\n","C\n","PHP\n","c++\n","Ruby\n"]
with open("sunflower.txt","w") as myfile:
    for i in language:
        myfile.write("%s"%i)
content=open("sunflower.txt")
print(content.read())
"""
#write a python program to copy the content of a file to another file:
"""
new_file=open("car2.txt","w")
with open("car1.txt","r") as f:
    new_file.write(f.read())
new_file.close()
"""
#write a python program to read a random line from a file:

"""
import random
def random_line(fname):
    lines=open(fname).read().splitlines()
    return random.choice(lines)
print(random_line("car1.txt"))
"""
#write a python program to check the file is close or not?
"""
f=open("car1.txt","r")
print(f.closed)
f.close()
print(f.closed)
"""
#Games:
"""
#Game 1: (coin toss)
import random
coin=["Head","Tail"]
print(random.choice(coin))


#Game 2: (Dice)
import random
dice=[1,2,3,4,5,6]
print("Dice:",random.choice(dice))

#print("Dice:",random.randint(1,7))
"""

#write a python program that read the content of string and count the number of
#alphabets ,lower and upper case letters ,digits and number of words:
"""
def Count(Str):
    alpha=0
    upper=0
    lower=0
    digit=0
    words=0
    for i in range(len(Str)):
        if Str[i]>="A" and Str<="Z":
            upper+=1
            alpha+=1
        elif Str[i]>="a" and Str[i]<="z":
            lower+=1
            alpha+=1
        elif Str[i]>="0" and Str[i]<="9":
            digit+=1
        elif Str[i]==():
            words+=1
        print("Total Character:",len(Str))
        print("Total Alphabets:",alpha)
        print("Total upper case letters:",upper)
        print("Total lower case letters:",lower)
        print("Total Digits:",digit)
        print("Total Words:",words)
Str="Naini Prayagraj Pin 211008"
Count(Str)

"""

#scope:-
"""
pi="Outer pi value"
def PiFun():
    
    pi="inner pi value"
    print(pi)
PiFun()
print(pi)

"""
#LEGB Rule:-
"""
def outer_function():
    a=20
    def inner_function():
        a=30
        print("a:",a)
    inner_function()
    print("a:",a)


a=10
outer_function()
print("a:",a)


x="a"
y="A"
print(id(x),id(y))
"""
"""
#import <module_name>
import mymod
mymod.carea(5)
mymod.tarea(4,3)


#<module_name>.<function_name>(<List_of_values>)

dir()
reload()
"""
#Numpy:-
#array():-
#<array_name>=<numpy_obj>.array([<list/tuple>])
"""
import numpy as np
age=np.array([21,18,25,31])
print(type(age))
"""

#arange():-
#<array_name>=<numpy_obj>.arange(start,stop,step)
"""
import numpy as np
even=np.arange(2,10,2)
print("Even:",even)
"""
#linspace():-
"""
#<array_name>=<numpy_obj>.linspace(start,stop,num=50,endpoint=True,restep=False)
import numpy as np
a=np.linspace(1,3,5)
print(a)
"""
"""
import numpy as np
age=[15,20,23,30,16,18,19,20,22,21]
mj=0
mn=0
age_array=np.array(age)
for i in age_array:
    if(i>=18):
        mj=mj+1
    else:
        mn=mn+1
print("No. of Major:",mj,"\nNo. of Minor:",mn)
"""
#N-D Array:-
"""
#one/single dimensional array:-
import numpy as np
x=np.array([10,20,30])
print("One Dim:\n",x)
"""
"""
#Two dimensional array:-
import numpy as np
x=np.array([(10,20,30),(40,50,60)])
print("Two Dim:\n",x)
"""
"""

#Three dimensional array:-
import numpy as np
x=np.array([(10,20,30),(40,50,60),(70,80,90)])
print("Three Dim:\n",x)
"""
#write a python prpgram to fing the Transpose of a matrix:
"""
import numpy as np
a=np.array([[1,2],[3,4]])
print("The Matrix is:\n",a)
print("Transpose of a Matrix:\n",a.T)
"""
#write a python program to add two matrix:

#import numpy as np
"""
#empty()
x=np.empty([3,2],dtype=int)
print(x)

#ones()
x=np.ones(6,dtype=int)
print(x)


#zeros()
x=np.zeros(6,dtype=int)
print(x)

#identity()
x=np.identity(4,dtype=int)
print(x)

#eye()
x=np.eye(2,dtype=int)
print(x)

#copy()

A=np.array([3,5,9,4,2,6])
B=A.copy()
print(B)


"""
"""
#asarray():
l=[10,20,30,4,5,6,50]
print(type(l),l)
arr=np.asarray(l)
print(type(arr),arr)
"""
"""
#asmatrix():-
x=np.array([[10,20,30],[40,50,60],[70,80,90]])
arr=np.asmatrix(x)
print(arr)
#change the value:
x[0,2]=100
print(x)

"""
#Oops in python:-
"""
class First:
    a:int
    def __init__(self):
        self.a=10
        print("a=",self.a)
        
f=First()
"""
#Add two number in Oops programing
"""
class Num:
    a:int
    b:int
    c:int
    
    def disp(self):
        self.a=10
        self.b=20
        self.c=self.a+self.b
        print(self.a)
    def output(self):
        print("Result:",self.c)
n=Num()
n.disp()
n.output()

"""
"""
#partition()
txt="I could bananas eat the bananas all bananas daay"
print(txt.partition("bananas"))


#maketrans()
#str.maketrans(x,y,z)
"""
"""
txt="Hi Sam!"
x="mSa"
y="eJo"
mytable=str.maketrans(x,y)
print(mytable)
print(txt.translate(mytable))
"""
"""
txt="Good night Sam!"
x="mSa"
y="eJo"
z="odnght"
mytable=str.maketrans(x,y,z)
print(txt.translate(mytable))
"""

#Convert decimal number to binary number:
"""
import numpy
binnum=[]
num=int(input("Enter the Number to convert into Binary Number:\n>>"))
while(num>0):
    i=num%2
    binnum.append(i)
    num=num//2
    rev=binnum[::-1]

print(rev)

print(bin(5))
print(oct(5))
print(hex(5))
"""
"""
vowel=['a','e','i','o','u','A','E','I','O','U']
user=input("Enter the character:")
for v in vowel:
    if(v==user):
        print("Vowel")
        break
else:
    print("Consonent")
"""
"""
def isVowel(ch):
    str="aeiouAEIOU"
    return (str.find(ch) !=-1)
print("a is " +str(isVowel('a')))
print("x is " +str(isVowel('x')))
"""
"""
user=int(input("enter the value: "))
item=["apple","banana","grapes"]
while (True):
    if(user==1):
        print("your items are:",item)
        break
    elif(user==2):
        item.append(user)
        print(item)
        break
    elif(user==3):
        pass
    elif(user==4):
        break
    else:
        break
"""
def display(n):
    if(n<=5):
        print(n)
        display(n+1)
display(1)
