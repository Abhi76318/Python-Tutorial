"""Recursion"""
# Algorithmically a way to design solutions to problems by 
# divide-and-conquer or decrease-and-conquer
# Semantically a programming tchnnique where a function calls itself


# def mult_recur(a,b):
#     if b == 1:
#         return a
#     else:
#         return a + mult_recur(a, b-1)
    
# print(mult_recur(4,7))

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(4))

# Finger Exercise
# def recur_power(base,exp):
#     if exp == 0:
#         return 1
#     else:
#         return base * recur_power(base,exp-1)
    
# print(recur_power(2,5))