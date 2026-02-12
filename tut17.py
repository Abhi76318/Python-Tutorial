"""Python Classes : Object oriented programming"""
# Python supports many kinds of data and each is an object
# An object is an instance of a type
# class Coordinate(object):
# define attributes here
"""Definining how to create an instance of a class"""
# Use a special method called __init__ to initialize some data attributes 
# or perform initialization operations
# Templete for a object type is:

# class Coordinate(object):
#     def __init__(self, xval, yval):
#         self.x = xval
#         self.y = yval

# self is parameter to refer to an  instance of the class without having
# created one yet. It allows you to create variables that belong to this
# object. Without self, you are just creating regular variables!
# NOTE: When defining a class, we don't have an actual tangible object
# here. It's only a definition.
"""Actually creating an instance of a class """
# Code to make actual tangible Coordinate objects(aka instances) is:
# c = Coordinate(3,4) # create a new object of type Coordinate and pass
#                     #   in 3 and 4 to the __init__
# origin = Coordinate(0,0)
# print(c.x)
# print(origin.x)

# NOTE: "Method" is a procedural attribute. Think of it like a function
# that works only with this class.
# Python always passes the the object as the first argument.
# Convention is to use 'self' as the name of the first argument of all methods.

# Define a method for the Coordinate class is:
# def distance(self, other):
#     x_diff_sq = (self.x-other.x)**2
#     y_diff_sq = (self.y-other.y)**2
#     return (x_diff_sq + y_diff_sq)**0.5

# How to call a method?
# Dot notation:
# <object_variable>.<method>(<parameters>)

# print(c.distance(origin))

# Finger Exercise
# class Circle():
#     def __init__(self, radius):
#         """Initializes self with radius"""
#         self.r = radius
#     def get_radius(self):
#         """Returns the radius of self"""
#         return self.r
#     def set_radius(self, radius):
#         """radius is a number 
#         Changes the radius of self to radius"""
#         self.r = radius
#     def get_area(self):
#         """Returns the area of self using pi = 3.14"""
#         return 3.14* self.r* self.r
#     def equal(self, c):
#         """c is a Circle object
#          Returns True if self and c have the same radius value """
#         return (c.r == self.r)
#     def bigger(self, c):
#         """c is a Circle object
#         Returns self or c, the Circle object with the bigger radius"""
#         if c.r > self.r:
#             return c
#         elif c.r < self.r:
#             return self
        