'''
---Strings and Loops---

'''
#Code to check for the letter i or u in a string

# s="Abhishek Kumar is motivating u" 
# for  index in range (len(s)) :
#     if s[index] == 'i' or s[index] == 'u' :
#         print("There is an i or u")

# for char in s :
#     if char == 'i' or char == 'u' :
#         print("There is an i or u")

# for char in s :
#     if char in 'iu' :
#         print ("there is an i or u")

#ROBOT CHEERLEADERS

# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input ("I will cheer for you! Enter a word: ")
# times = int(input ("Enthuasiasm level (1-10): "))

# for c in word :
#     if c in an_letters :
#         print(f'Give me an {c}: {c}')
#     else:
#         print(f'Give me a {c}: {c}')
# print("What's that spell? ")
# for i in range(times):
#     print(word, '!!!')


'''Assume you are given a string of lowercase letters in variable s.
    Count how many unique letters there are in the sring. '''

# s = "abhishek"
# seen = ''
# count = 0
# for c in s : 
#     if c not in seen : 
#         seen += c
#         count += 1
# print(count)

'''Check wheter perfect square or not'''

# guess =0
# x= int (input("Enter an integer: "))
# while guess**2 < x :
#     guess += 1
# if guess**2 == x:
#     print ("Square root of ",x,"is",guess)
# else :
#     print(x, "is not a perfect square")

'''Binary Number'''

# num = 1507
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = result + str(num % 2)
#     num = num // 2
# print(int(result[::-1]))

'''Fingertips Exercise'''

N = int(input("Take a positive integer: "))
i=1
while i**3 < N:
    i += 1
if i**3 == N:
    print(f'{i} is cube root of {N}')
else:
    print("error")
