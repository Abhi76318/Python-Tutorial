"""Functions as Objects"""

#Python return the value None, if there is no return given
# def is_even(i):
#     i%2 == 0
#     return None  --> Python add this implicitly if not return

# def is_even_with_return(i):
#     print('with return')
#     remainder = i%2
#     return remainder == 0

# print(is_even_with_return(3))

# def is_even_without_return(i):
#     print('without return')
#     remainder = i%2
#     has_rem = (remainder == 0)
#     print(has_rem)

# print(is_even_without_return(3))

# print(print(5)) # -->give output 5 and None 

# function call create a new environment
# Environment disappear when return a value also the variables disappear
# Global Scope --> Can't disappear 
# Function Scope --> Disappear after return a value
# Changes in function scope can't affect value of global scope

def f(x):
    x=x+1
    print('in f(x): x= ',x)
    return x

x = 3
z = f(x)
print(x)