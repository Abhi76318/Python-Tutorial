"""Recursion : Fibonacci, Fibonacci with a dict, recursion on non numerics,
recursion on lists, Tower of Hanoi"""

# Fibonacci code
# def fib (x):
#     if x == 1 or x == 2:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)
    
# print(fib(7))
# NOTE: Very inefficient code bcz we have to same calculation twice or more

# def fib_efficient(n, d):
#     if n in d:
#         return d[n]
#     else:
#         ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
#         d[n] = ans
#         return ans
# d = {1:1, 2:1}
# print(fib_efficient(6,d))

# Calling fib(34) results in 11,405,773 recursive calls But
# Calling efficient_fib(34) results in 65 recursive calls
# Using dictionaries to capture intermediate results can be very efficient
# NOTE: this onlys works for procedures  without side effects i.e,
# it will always produce the same result for a specific argument independent
# of any other computations between calls

#Example of basketball score
# def score_count(x):
#     """Returns all the ways to make a score of x by adding 
#     1, 2, and/or 3 together. Order doesn't matter. """
#     if x == 1:
#         return 1
#     elif x == 2:
#         return 2
#     elif x == 3:
#         return 3
#     else:
#         return score_count(x-1)+score_count(x-2)+score_count(x-3)
    
# ans = score_count(6)
# print(ans)
#NOTE: we can use dictonaries to store for efficient code

"""Lists are naturally recursive"""

# def total_iter(L):
#     result = 0
#     for e in L:
#         result += e
#     return result

# test = [30, 40, 50]
# print(total_iter(test))

# NOTE: Each case (base cases, recursive steps) must return the same
# type of object. Function returns build upon each other!
# If the base case returns a bool and the recursive step returns an int,
# this gives a type mismatch error at runtime.

"""Reverse a list of elements: All elements get reversed"""
# def deep_rev(L):
#     if len(L) == 1:
#         if type(L[0]) != list:
#             return L
#         else:
#             return [deep_rev(L[0])]
#     else:
#         if type(L[0]) != list:
#             return deep_rev(L[1:]) + [L[0]]
#         else:
#             return deep_rev(L[1:]) + [deep_rev(L[0])]

# Finger exercise
# def flatten(L):
#     """L: a list
#     Returns a copy of L, which is flattened version of L
#     """
#     result = []
#     for i in L:
#         if type(i) == list:
#             result.extend(flatten(i))
#         else:
#             result.append(i)
#     return result

# L = [[1,4,[6],2],[[[3]],2],4,5]
# print(flatten(L))