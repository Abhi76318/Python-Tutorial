"""Exceptions, Assertions"""
'''Unexpected Conditions get an Exception. Its is of different form:
    IndexError, TYpeError, NameError, TypeError
--> Typically exception causes an error to occur and execution to stop
--> Python code can provide handlers for exceptions'''
# try:
#     # do some potentially
#     # problematic code
# except:
#     # do something to
#     # handle the problem
# If expressions in try block all succeed
#  evaluation continues with code after except block
# Exceptions raised by any statement in body of try are handled by the 
#   except statement
#   Exution continues with the body of the except statment
#   Then other expressions aftervthat block of code
# def sum_digits(s):
#     total = 0
#     for char in s:
#         if char in '0123456789':
#             val =int(char)
#             total += val
#     return total
# print(sum_digits("123"))
# print(sum_digits("123abc"))

# def sum_digits(s):
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except :
#             print("can't convert", char)
#     return total
# print(sum_digits("1234"))
# print(sum_digits("1234adc"))

# What to do with exceptions?
# In Python : raise an exception
# raise ValueError("something is wrong")
#  
# def sum_digits(s):
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             raise ValueError("string contained a character")
#     return total
# print(sum_digits("123"))
# print(sum_digits("1234abc"))

# Practice Qs
# def pairwise_div(Lnum, Ldenom):
#     """Lnum and Ldenom are non-empty lists of equal lengths containing numbers
#     Returns a new list whose elements are the pairwise division of
#     an element in Lnum by an element in Ldenom
#     Raise a ValueError if Ldenom contains 0.
#     """
#     L = []
#     try:
#         L = [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
#     except:
#         raise ValueError("Ldenom contain 0.")
#     return L
# Lnum = [6,4,2]
# Ldenom = [2,4,1]
# print(pairwise_div(Lnum,Ldenom))

'''Asssertions: Defensive Programming Tool'''
# Use an assert statement to raise an AssertionError exception 
# if assumptions not met
# assert <statement that should be true>, "message if not true"

# An example of good defensive programming
# Assertions don't allow a programmer to control response to unexpected conditions
# Ensure that execution halts whenever an expected condition is not met
# Typically used to check inputs to functions, but can be used anywhere
# Can be used to check outputs of a function to avoid propagating bad values
# Can make it easier to locate a source of a 

# def sum_digits(s):
#     assert len(s) != 0, "s is empty"
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             raise ValueError("string contained a character")
#     return total
# # print(sum_digits("123"))
# print(sum_digits(""))

# def get_stats(class_list):
#     new_stats = []
#     for stu in class_list:
#         new_stats.append([stu[0],stu[1],avg(stu[1])])
#     return new_stats
# def avg(grades):
#     return sum(grades)/len(grades)

# If a student haven't any grades, give error message
# def avg(grades):
#     try:
#         return sum(grades)/len(grades)
#     except ZeroDivisionError:
#         print('warning: no grades data')
# class_list  = [[['peter','parker'],[80.0,70.0,85.0]],[['bruce','wayne'],[100.0,80.0,74.0]],[['abhi','kumar'],[]]]
# print(get_stats(class_list))
# return none as avgerage
# warning: no grades data
# [[['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333333333333], 
# [['bruce', 'wayne'], [100.0, 80.0, 74.0], 84.66666666666667], [['abhi', 'kumar'], [], None]] 

