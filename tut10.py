"""Lists, Mutability:mutation, aliasing """
#Lists are mutable!  
# Assignning to an element at an index changes the value
# L = [2,4,7]
# L[1] = 5
# print(L)
'''Operation on Lists'''

'''1) append -> Add an element to end of list with "L.append(element)"'''

# Lc = [3,5,8]
# Lc.append(1)
# Lc = Lc.append(4)    #Lc binds with None
# print(Lc)
# L1 = ['re']
# L2 = ['mi']
# L3 = ['do']
# L4 = L1 +L2
# L3.append(L4)
# L = L1.append(L3)
# print(L1,L2,L3,L)

# Practice Qs
# def make_ordered_list(n):
#     """n is a positive int
#     Returns a list containing all ints in order from 0 to n(inclusive)
#     """
#     L = []
#     for  i in range(n+1):
#         # L += [i]   #or
#         L.append(i)
#     return L
# print(make_ordered_list(10))

#Practice Qs
# def remove_elem(L, e):
#     """L is a list
#     Returns a new list with elements in the same order as L but
#     without any elements equal to e
#     """
#     newlist = []
#     for i in L:
#         if i != e:
#             newlist.append(i)
#     return newlist
# L = [1,2,2,3]
# print(remove_elem(L, 2))

'''2) Convert string to list with list(s)
--> Use s.split(), to split a string on a character parameter,
    splits on spaces if called without a parameter'''

# s = "I<3 cs &u?"
# L = list(s)
# print(L)
# L1 = s.split(' ')
# L2 = s.split('<')
# print(L1)
# print(L2)

'''3) Convert a list of strings back to string
# Use ''.join(L) to turn a list of strings into a bigger string
# Can give a character in quotes to add char b/w every element '''

# L = ['a','b','c']
# A = ''.join(L)
# print(A)
# B = '_'.join(L)
# print(B)
# # C = ''.join([1,2,3])  #error
# # print(C)
# D = ''.join(['1','2','3'])
# print(D)

'''4) sort()-> sort the list with L.sort()'''

# L = [3,9,5]
# L.sort()
# print(L)

'''5) reverse()-> Reverse the list with L.reverse()'''

# L = [3,6,4]
# L.reverse()
# print(L)

'''6) sorted()-> Returns a sorted version of L (no mutation!)'''

# L = [3,7,2]      #Remains in storage
# L_new = sorted(L) #change binding i.e no mutation
# print(L_new)

#Practice Qs
# def sort_words(sen):
#     """sen is a string representing a sentence
#     Returns a list containing all the words in sen but
#     sorted in alphabetical order."""
#     L1 = sen.split(' ')
#     L1.sort()
#     return L1
# print(sort_words("look at this photograph"))
    
#Functions with side efffects mutates inputs
'''7) --> Concatenation, + operator, creates a new list, with copies
   --> Mutate list with L.extend(some_list) (copy of some_list)
'''
# L1 = [2,1,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# # print(L3)
# L1.extend([0,7])
# L2.extend([[1,2],[2,4]])
# print(L1)
# print(L2)

'''8) Empty out a list and checking that it's the same object
        ---> Use L.clear()
        ---> You can mutate a list to remove all its elements
         --> This doesn't make a new empty list
        ---> How to check that it's the same object in memory?
        --->9) Use the id() function
'''
