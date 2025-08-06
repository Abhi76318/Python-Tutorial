"""Floats and Approximation Methods"""

# x=0
# for i in range(10):
#     x+=0.1
#     print (x==1)
#     print (x, '==', 10*0.1)

# error accumulate and make big difference

'''Convert Integers to Binary'''

# num= int(input("Enter a no.: "))
# if num < 0:
#     is_neg = True
#     num = abs(num)
# else:
#     is_neg = False
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = result + str(num%2)
#     num = num // 2
# if is_neg:
#     result = '-' + result
# print(int(result[::-1])

'''Fraction into Binary'''
# x = 0.525
# p = 0
# while ((2**p)*x) % 1 != 0:
#     print ('Remainder= ' + str((2**p)*x - int((2**p)*x)))
#     p += 1

# num = int (x*(2**p))

# result = ''
# if num == 0:
#     result = '0'
# while num >0:
#     result = str(num%2) + result 
#     num = num // 2

# for i in range (p- len(result)):
#     result = '0' + result

# result = result[0:-p] + '.' + result[-p:]
# print ("The Binary representation of the decimal "+ str(x) + "is " + str(result))

'''
--> Never use == to test floats
-->instead test wheter they are within small amount of each other
-->whatmgets printed isn't always what is in memory
-->Need to be careful in designing algorithms that Use floats
'''

'''Approxiation Method Implementatiion'''
# x = 36
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001

# while abs (guess**2 -x) >= epsilon:
#     guess += increment
#     num_guesses += 1

# print ('num_guesses =', num_guesses)
# print(guess, 'is close to square root of', x)

'''Sometimes we overshot the Epsilon
 - due to which it grow bigger and infinite
-->We can fix it by adding Stopping condition'''

#Finger Exercise

# my_str = "Abhishek"
# result = ''

# for i in range(0,len(my_str),2):
#     result += my_str[i]
# print(result)
