Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\NDICD\Desktop\learnpython\bt4.py
l=[10,20,30]
l
[10, 20, 30]
print(type(l))
<class 'list'>
t=(40,50,60)
t
(40, 50, 60)
print(type(t))
<class 'tuple'>
a=10,
a
(10,)
t1=100,200,3000
t1
(100, 200, 3000)





============================== RESTART: Shell =============================
Tuple=(100,200,300,400,500,600)
Tuple
(100, 200, 300, 400, 500, 600)
print(Tuple[1])
200
Tuple[2]=15
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    Tuple[2]=15
TypeError: 'tuple' object does not support item assignment
>>> List=[1,2,3,4]
>>> List[1]=100
>>> List
[1, 100, 3, 4]
>>> Tuple=(01,10,20,30)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> Tuple(10,20,30,40)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Tuple(10,20,30,40)
TypeError: 'tuple' object is not callable
>>> Tuple=(10,20,30,40)
>>> Tuple[1]=400
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Tuple[1]=400
TypeError: 'tuple' object does not support item assignment
