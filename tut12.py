"""List Comprehension, Functions as Objects, Testing, Debugging"""
'''Applying a function to every element of a sequence, then creating
    a new list with these values is a common concept.
--> Python provides a cocise one-linear way to do this, called a 
    "List Comprehension"
    Syntax:
    [expression for elem in iterable if test]
    '''
# def f(L):
#     Lnew = []
#     for e in L:
#         Lnew.append(e**2)
#     return Lnew
# print(f([3,4,5,2,7]))
# OR
# L = [3,4,5,2,7]
# Lnew = [e**2 for e in L]
# print(Lnew)
# def f(L):
#     Lnew = []
#     for e in L:
#         if e%2==0:
#             Lnew.append(e**2)
#     return Lnew
# print(f([3,4,2,7,5]))
# OR 
# L = [3,4,2,7,5]
# Lnew = [e**2 for e in L if e%2==0]
# print(Lnew)

# Practice Qs
# W = [len(x) for x in ['xy', 'abcd', 7, '4.0'] if type(x) == str]
# print(W)

'''Functions can return Functions'''
# def make_prod(a):
#     def g(b):
#         return a*b
#     return g    # g is function object
# val = make_prod(2)(3)
# print(val)
# OR
# doubler = make_prod(2)
# val = doubler(3)
# print(val)
# NOTE: definition of g is done within scope of make_prod, so binding
#       of g is within that frame/scope
#   Since g is bound in this frame, can't access it by evaluation
#   in global frame

"""TESTING AND DEBUGGING """

''' Defensive Programming
> Write specifications for functions
> Modularize programs
> Check conditions on inputs/outputs(assertions)
'''

'''
Testing/Validaation
> Compare input/output pairs to specification
> It's not working!
> How can i break my program?
'''

'''
Debugging
> Study events leading up to an error
> Why is it not working?
> How can i fix my program?
'''

# CLASSES OF TESTS
'''
1) Unit testing 
    > Validate each piece of program 
    > Testing each function separately
2) Regression testing
    > Add test for bugs as you find them
    > Catch reintroduced errors that were previously fixed
3) Integration testing
    > Does overall program work?
    > Tend to rush to do this
'''

# NOTE: Error messages are easy. eg, IndexError,TYpeError,SyntaxxError,etc
#       Logic error are harder.

# Finger Exercise
# def count_sqrts(nums_list):
#     count = 0
#     for e in nums_list:
#         if e*e in nums_list:
#             count += 1
#     return count
# print(count_sqrts([3,4,2,1,9,25]))