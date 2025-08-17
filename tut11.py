"""Aliasing, Cloning"""
'''Making a copy of the List --> by duplicating all elements 
    (top-level) into a new list object
    --> Lcopy = L[:]
    '''
# Loriginal = [4,5,6]
# Lnew = Loriginal[:]
# print(Lnew)

''' --> Delete element at a specific index with del(L[index])
    --> Remove element at end of list with L.pop(), returns the removed
        element (can also call with specific index: L.pop(3))
    --> Remove a specific element with L.remove(element)
        > If element occurs multiple times, removes first occurrence
        > If not in list, gives an error
'''
# L = [2,3,2,1,5,6,4,0]
# L.remove(2)
# L.remove(3)
# del(L[1])
# print(L)
# a = L.pop()
# print(L,a)

#Practice Qs
# def remove_dups(L1, L2):
#     L1_copy = L1[:]
#     for e in L1_copy:
#         if e in L2:
#             L1.remove(e)
# L1 = [10,20,30,40]
# L2 = [10,20,50,60]
# print(remove_dups(L1,L2))
# print(L1)

'''Alaising --> Giving differnt names for same memory value
    > When u pass a list as a parameter to a function, you 
        are making an alias.
'''
#Control Copying
# old_list = [[1,2],[3,4],[5,'foo']]
# new_list = old_list

# new_list[2][1] = 6
# print("New list:", new_list)
# print("Old list:",old_list)

# so mutating one object changes the other
'''1) Shallow copying does this at the top level of the list
    > Equivalent to syntax[:]
    > Any mutable elements are NOT copied
    --> Use this when ur list contains immutable objects only'''
# import copy
# old_list = [[1,2],[3,4],[5,6]]
# new_list = copy.copy(old_list)

# old_list.append([7,8])
# old_list[1][1] = 9
# print("New list:", new_list) #output [[1,2],[3,9],[5,6]]
# print("Old list:", old_list) #output [[1,2],[3,9],[5,6],[7,8]]

'''If we want all structures to be new copies, we need a deep copy
    > use ddep copy when ur list might have mutable elements to
        ensure every structure at every level is copied'''
# import copy
# old_list = [[1,2],[3,4],[5,6]]
# new_list = copy.deepcopy(old_list)

# old_list.append([7,8])
# old_list[1][1] = 9
# print("New list:", new_list) #output [[1,2],[3,4],[5,6]]
# print("Old list:", old_list) #output [[1,2],[3,9],[5,6],[7,8]]

# Finger Exercise
# def remove_and_sort(Lin, k):
#     Lin_new = Lin[:]
#     for e in Lin_new:
#         if e in Lin:
#             Lin.remove(e)
#             break
#     Lin.sort()
# L = [1,6,3,4]
# k = 1
# remove_and_sort(L, k)
# print(L)
#This solution is not correct for all cases
#Another solutions
# def remove_and_sort(Lin, k):
#     i = 0
#     while i<k and len(Lin)>0:
#         Lin.pop(0)
#         i += 1
#     Lin.sort()

# L = [6,3,4]
# k = 1
# remove_and_sort(L, k)
# print(L)