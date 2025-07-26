'''concetation of the string
a+b=ab also 4*c=cccc'''

b=":"
c=")"
s1=b+2*c
print("hello")
print(s1)

f="a"
g=" b"
h="3"
s2=(f+g)*int(h)
print(s2)

#length of string

s="Abhishek"
z=len(s)
print(z) 

'''
Slicing in a string
-->Square brackets used to perform indexing to get value at certain position
-->s=Vishal
-->s[0]->V
-->s[4]->a
Also s[-1]-->Start froom last->l
and s[-4]-->s 
Slicing to get substring
-->Can slice string using [start:stop:step]
-->If give two numbers,[start:stop],step=1 by default 

'''

s="abcdefgh"
print(s[2:5])
print(s[1:6:2])
print(s[4])
print(s[:])        #s[0:len(s):1]
print(s[::-1])     #s[-1:-len(s):-1]
print(s[5:1:-2])
print(s[-4:-1:1])

#Input/Output
"""
print()-->To print output
x=input(s)-->To take input and assigned to variable x
"""

text=input("Type anything: ")
#input always returns an str, must cast if working with numbers
print(5*text)

#Practice Question

practice=input("Enter a verb: ")
print("I can ",practice," better than you!")
print(5*(' ' +practice))

#practice question

secret=6
choose=int(input("Make Your guess: "))
# print(choose==secret)

#Identation matters in python

if choose>secret :
    print("Too high")
elif choose==secret :
    print("Equal") 
else :
    print("Too low")  

#Finger Exercise

number=int(input("Choose a no.: "))
if number>0 :
    print("positive")
elif number<0 :
    print("negative")
else :
    print("zero")
