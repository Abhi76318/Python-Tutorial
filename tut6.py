'''Bisection Search'''
#Log growth is better
#Log algorithm is much more efficient
#Bisection search takes advantage of properties of the problem
# 1) The search space has an order
# 2) We can tell whether the guess was too low or too high

# x=54321
# epsilon = 0.01
# num_guesses = 0
# low = 0.0
# high = x
# guess = (high+low)/2

# while abs(guess**2 - x) >= epsilon:
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2
#     num_guesses += 1

# print(f'num_guesses = {str(num_guesses)}')
# print(f'{str(guess)} is close to square root of {str(x)}')

#if x=0.5 then due to floating point error runs infinite
#if the no. b/w 0 to 1 then 
# low = x
# high = 1.0

# cube = 27 
# epsilon = 0.01
# low = 0
# high = cube
# num_guesses = 0
# guess = (high +low)/2

# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 > cube:
#         high = guess
#     else:
#         low = guess
#     guess = (high+low)/2
#     num_guesses += 1

# print(f'num_guesses = {str(num_guesses)}')
# print(f'{str(guess)} is close to cube root of {str(cube)}')

'''Newton Raphson Root Finder'''

# epsilon = 0.01
# k = 24.0
# guess = k/2.0 
# num_guesses = 0

# while abs(guess*guess - k) >= epsilon:
#     num_guesses += 1
#     guess= guess - (((guess**2)-k)/(2*guess))

# print('num_guesses = ' + str (num_guesses))
# print('Square root of '+ str(k) + 'is about' + str(guess))

#Specific to particular problem