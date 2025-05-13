"""
print("Hey")
import pywhatkit as pwk
phn="+919129625253"
msg="Hi Ayush how are you?"
pwk.sendwhatmsg(phn,msg,13,35)
"""
#BMI Calclator:-
"""
weight=float(input("Enter the weight in kg:"))
height=float(input("Enter the height in meter:"))
bmi=round(weight/height**2)
#print(bmi)
if(bmi<18.5):
    print(f"Your BMI is {bmi} and you are underweight.")
elif(bmi<25):
    print(f"Your BMI is {bmi} and you are Normal.")
elif(bmi<55):
    print(f"Your BMI is {bmi} and you are Obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically Obese.")
"""

"""
#ride in fare:;-
height=float(input("Enter the height in ft."))
bill=0
if height>=3:
    print("Can Ride!")
    age=int(input("What's your age? "))
    if age<=12:
        bill=150
        print(f"Ticket price is {bill} Rs.")
    elif(age<=18):
        bil=250
        print(f"Tickt price is {bill} Rs.")
    else:
        bill=500
        print(f"Ticket price is {bill} Rs.")
    want_photo=input("Do you want to take photo(Y/N).")
    if(want_photo=="y" or want_photo=="Y"):
        bill+=50
    print(f"You Total Bill is {bill} \nThank You for a Ride")
else:
    print("Can't Ride!")
"""
#Pizza Order program:-
"""
Small pizza=100
medium pizza=200
large pizza=300

pepperoni for small pizza=30
pepperoni for large pizza=50
extra cheese for any pizza=20
"""

size=input("What size pizza you want(S/M/L)?")
bill=0
if(size=="s" or size=="S"):
    bill+=100
    print(f"Small pizza price is {bill} Rs.")
elif(size=="m" or size=="M"):
    bill+=200
    print(f"Medium pizza price is {bill} Rs.")
elif(size=="l" or size=="L"):
    bill+=300
    print(f"Large pizza price is {bill} Rs.")
else:
    print("Wrong Input! Please enter valid size.")
add_pepperoni=input("Do you want Pepperoni(Y/N).")
if(add_pepperoni=="y" or add_pepperoni=="Y"):
    if(size=="s" or size=="S"):
        bill+=30
    else:
        bill+=50

cheese=input("Do you want Extra Cheese (Y/N)?")
if(cheese=="y" or cheese=="Y"):
    print(f"Your final Bill is {bill+20} Rs.")


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
#pridict head or tail? #34
"""
import random
side=random.randint(0,1)
if(side==1):
    print("Head")
else:
    print("Tail")
"""
#who will pay the bill


