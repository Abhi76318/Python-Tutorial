"""Lamda Functions, Tuples, and Lists"""

# def apply(criteria,n):
#     """
#     * criteria: function that takes in a number and returns a bool
#     * n: an int
#     Returns  how many ints from 0 to n (inclusive) match the 
#     criteria (i.e. return True when run with criteria)
#     """
#     count = 0
#     for i in range(n+1):
#         if criteria(i):
#             count += 1
#     return count

# def is_even (x):
#     return x%2==0

# print (apply(is_even,10))
# print (apply(lambda x: x%2==0, 10))

# Instead of 
# def is_even(x):
#     return x%2==0
# use anonymous procedure by using lambda
# lambda x: x%2 == 0    x=parameter

#-->lambda creates a procedure/function object, but simply does
# not bind a name to it
#-->lambda function is one time use. it can't be reused because
#   it has no name!

# def do_twice(n, fn):
#     return fn(fn(n))

# print(do_twice(3, lambda x: x**2))

'''
Tuples --> Indexable ordered sequence of objects
        Objects can be any type - int, string, tuple, tuple of tuples,..
    Can't change element values, immutable
    te = ()
    ts = (2,)  extra comma means tuple with one element 
    t = (2, "mit", 3)
    t[0]   -->evaluates to 2
    (2,"mit",3)+(5,6) --> evaluates to a new tuple (2,"mit",3,5,6)
    t[1:2]  -->slice tuple, evaluates to ("mit",)
    t[1:3]  -->slice tuple, evaluates to ("mit",3)
    len(t)  -->evaluates to 3
    max((3,5,0))  --> evaluates to 5
    t[1] = 4   --> gives error, can't modify object
'''
seq = (2,'a',4,(1,2))
# print(len(seq))  --> 4
# print(seq[3])     -->(1,2)
# print(seq[-1])    -->(1,2)
# print(seq[3][0])  -->1
# print(seq[4])     -->error
# print(seq[1])     -->'a'
# print(seq[-2:])   -->(4,(1,2))
# print(seq[1:4:2]) -->('a',(1,2))
# print(seq[:-1])   -->(2,'a',4)
# print(seq[1:3])   -->('a',4)
# for e in seq:
#     print(e)

'''Used to return more than one value fromm a function'''
# def quotient_and_remainder(x,y):
#     q= x//y
#     r= x%y
#     return (q,r)

# both = quotient_and_remainder(10,3)
# print(both)
# (quot, rem) = quotient_and_remainder(5,2)
# print(quot,rem)

#Practice Qs
# def char_counts(s):
#     """s is a string of lowercase chars 
#     Returns a tuple where the first value is the number of 
#     vowels in s and the second value is the number of 
#     consonants in s
#     """
#     vowels ='aeiou'
#     (c,v) = (0,0)
#     for char in s:
#         if char in vowels:
#             v += 1
#         else:
#             c += 1
#     return (v,c)

# print(char_counts("abcd"))
# print(char_counts("abhishek"))

# def mean(*args):   --> *notation
#     tot = 0
#     for a in args:
#         tot += a
#     return tot/len(args)

# print(mean(1,2,3,4,5,6)) --> numbers is bound to a tuple
#                                of the supplied value

"""
Lists -> Indexable ordered sequence of objects
    usually homogeneous (i.e. all integers,all strings, all lists)
    But can contain mixed types(not common)
    -> Denoted by square brackets,[]
    -> Mutable, this means you can change values of specific elements of list
    -> same as tuple but using []
"""
# a_list = []
# L = [2,'a',4,[1,2]]

#Practice Qs
# def sum_and_prod(L):
#     """L is a list of numbers 
#     Return a tuple where the first value is the sum of all elements
#     in L and the second value is the product of all elements in L
#     """
#     sum=0
#     prod=1
#     for i in range(len(L)):
#         sum += L[i]
#         prod *= L[i]
#     return (sum, prod)

# print(sum_and_prod([2,3,4,5,6]))

# Finger Exercise
def dot_product(tA, tB):
    length = len(tA)
    dot = 0
    for i in range(len(tA)):
        dot += tA[i]*tB[i]
    return (length, dot)

tA = (2,4,7)  
tB = (3,2,5)
print(dot_product(tA, tB))