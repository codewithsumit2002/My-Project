"""
i=int(input("enter the number:"))
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
    print("Reverse of the number:",rev)
"""
"""
i=int(input("enter the number:"))
rev=0
x=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
    print("Reverse of the number is:",rev)
if(x==rev):
    print("polindrome number")
else:
    print("Non polindrome number")
"""
"""
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
def fib(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_series=[0,1]
        while len(fib_series)<n:
            next_num=fib_series[-1]+fib_series[-2]
            fib_series.append(next_num)
        return fib_series
n=int(input("Enter the terms:"))
fib_series=fib(n)
print(fib_series)
"""
"""
n=int(input("Enter the number:"))
s=0
sqr=n**2
while(sqr>0):
    digit=sqr%10
    s=s+digit
    sqr=sqr//10
    if(s==n):
        print("Neon")
    else:
        print("Not neon number")
"""
"""
n=int(input("Enter the number:"))
if(n%1==0 and n%n==0):
    print("Prime")
else:
    print("Not Prime")
"""
"""
#def is_prime(n):

n=int(input("Enter the number:"))
if (n%1==0 or n%(n/2+n/2)==0):
    print("prime")
else:
    print("not prime")

"""

"""
num = int(input("Enter the number:"))
# If given number is greater than 1
if num >1:
	# Iterate from 2 to n / 2
	for i in range(2, 100):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")
"""
#create a list using user input:

"""
n=int(input("Enter the length of list:"))
a=[]
for i in range(n):
    a.append(int(input("Enter the value:")))
print(a)
"""
#finding the index position in given element:-
"""
tup=(23,45,56,78,99,54,65,12,43,57)
a=int(input("Enter the element to search:"))
print("Found on index:",tup.index(a))
"""
#tuple generator:-
"""
tpl=(x*3 for x in range(1,11))
for x in tpl:
    print(x)
print(type(tpl))
"""
"""
a="153"
s=0
for i in a:
    b=int(i)
    s=b**3
    print(b**3)
if s==b:
    print(i+a)
else:
    print("armsstrong number")
"""

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
board = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]
for row in board:
    for piece in row:
        print(piece, end=" ")
    print()

board[0][1] = ' ' # clear the source square
board[2][1] = 'N' # place the knight on the destination square

