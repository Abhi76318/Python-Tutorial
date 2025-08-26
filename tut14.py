"""Dictionaries"""
# def get_grades(student, name_list, grade_list):
#     i = name_list.index(student)
#     grade = grade_list[i]
#     return(student, grade)
# Alternative might be to use a list of lists
# eric = ['eric', ['ps',[8,4,5]],['mq', [6,7]]]
# ana = ['ana', ['ps',[10,10,10]],['mq', [9,10]]]
# john = ['john', ['ps',[7,6,5]],['mq', [8,5]]]
# grades = [eric,ana,john]

# A Python dictionary has entries that map a key:value
# Store pairs of data as an entry 
# key -> any immutable object eg, str,int,float,bool,tuple,etc
# value -> any data object eg, any above plus lists and other dicts!

# my_dict = {}
# d = {4:16}
# grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
# grades['John']  #evaluates to 'B'
# grades['Grace']  #gives a KeyError

# def find_grades(grades, students):
#     """grades is a dict mapping student names(str) to grade and 
#     students is a list of student names
#     Returns a list containing the grades for students"""

#     Lnew = []
#     for elem in students:
#         grade = grades[elem]
#         Lnew.append(grade)
#     return Lnew
# d = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
# print(find_grades(d,['Matt','Katy']))
'''Dictionary Operations'''
# Add an entry
# d['Grace'] = 'A'

# Change entry
# d['Grace'] = 'C'

# Delete entry
# del(d['Ana'])

# CAn iterate over dictionaries but assume there is no guaranteeed order
# Get an iterable that acts like a tuple of all keys
# d.keys()  --> returns dict_keys(['Ana', 'Matt', 'John', 'Katy'])
# list(d.keys())  --> returns ['Ana', 'Matt', 'John', 'Katy']
# Get an iterable that acts like a tuple of all dict values
# d.values()  --> returns dict_values(['B', 'A', 'B', 'A'])
# list(d.values()) --> returns ['B', 'A', 'B', 'A']
# Get ... like a tuple of all items
# d.items()  --> returns dict_items([('Ana','B'),('Matt','B')])
# list(d.items())
# typical use
# for k,v in d.items():
    # print(f"key{k} has value {v}")

# Creating a Dictionary
# song = "RAH RAH AH AH AH ROM MAH RO MAH MAH"
# def generate_word_dict(song):
#     song_words = song.lower()
#     word_list = song_words.split()
#     word_dict = {}
#     for w in word_list:
#         if w in word_dict:
#             word_dict[w] += 1
#         else:
#             word_dict[w] = 1
#     return word_dict

# word_dict = generate_word_dict(song)
# print(word_dict)

# def find_frequent_word(word_dict):
#     words = []
#     highest = max(word_dict.values())
#     for k,v in word_dict.items():
#         if v == highest:
#             words.append(k)
#     return (words, highest)
# word_dict = {'rah': 2, 'ah': 3, 'rom': 1, 'mah': 3, 'ro': 1}
# most_freq = find_frequent_word(word_dict)
# print(most_freq)
# def occurs_often(word_dict,x):
#     freq_list = []
#     word_freq_tuple = find_frequent_word(word_dict)
#     while word_freq_tuple[1] > x:
#         word_freq_tuple = find_frequent_word(word_dict)
#         freq_list.append(word_freq_tuple)
#         for word in word_freq_tuple[0]:
#             del (word_dict[word])
#     return freq_list
# print(occurs_often(word_dict,1))