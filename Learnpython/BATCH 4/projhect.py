"""
import os 
shutdown = input("Do you wish to shutdown your computer? (yes / no): ") 
if shutdown == 'no': 
	exit() 
else: 
	os.system("shutdown /s /t 1") 
"""

"""
for i in range(0,5):
        print(i)
print(dir())
exit()"""

"""
#Three ratio;-
a=12
b=20
B=10
c=16
C=b
A=B
ratio_a=a*A
ratio_b=b*B
ratio_c=c*C
print(ratio_a)
print(ratio_b)
print(ratio_c)
print()
"""




"""
if(ratio_a and ratio_b and ratio_c)%2==0:
        try:
                for i in range(True):
                        if(ratio_a or ratio_b or ratio_c)%i==0:
                                break
                        else:
                                print(int(ratio_a/i))
                                print(int(ratio_b/i))
                                print(int(ratio_c/i))
                        print()
        finally:
                print(f"\n{ratio_a} \n {ratio_b} \n {ratio_c}")
else:
        print(f" {ratio_a} \n {ratio_b} \n {ratio_c}")

"""


#Find the ratio's of 3 number
a=int(input("Enter the first {a} Ratio: "))
b=int(input("Enter the Second {b} Ratio: "))
B=int(input("Enter the Second (B) Ratio: "))
c=int(input("Enter the Third {c} Ratio: "))
n1=a*B
n2=b*B
n3=c*b
def hcf(a,b):
        while b:
                a,b=b,a%b
        return a
def fho3(n1,n2,n3):
        return hcf(n1,hcf(n2,n3))
list1=[]
for m in range(True):
        list1.extend([n1,n2,n3])   
print(f"Ratio are:{n1},{n2},{n3}\nHCF of the Ratio's:{fho3(n1,n2,n3)}")
for i in list1:
        print(int(i/fho3(n1,n2,n3)))




