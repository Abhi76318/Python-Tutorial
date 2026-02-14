"""More Python Class Methods: dunder methods"""
# class Circle(object):
#     def __init__(self, center, radius):
#         self.center = center
#         self.radius = radius

#     def is_inside1(self, point):
#         return point.distance(self.center) < self.radius

#     def is_inside2(self, point):
#         return self.center.distance(point) < self.radius

# Are these two methods in the Circle class functionally equivalent?

# Fraction: Need to create instances
# class SimpleFraction(object):
#     def __init__(self, n, d):
#         self.num = n
#         self.denom = d
#     def times(self, oth):
#         top = self.num*oth.num
#         bottom = self.denom*oth.denom
#         return top/bottom
#     def plus(self, oth):
#         top = self.num*oth.num + self.denom*oth.num
#         bottom = self.denom*oth.denom
#         return top/bottom
    
# f1 = SimpleFraction(3, 4)
# f2 = SimpleFraction(1, 4)
# print(f1.num)
# print(f1.denom)
# print(f1.plus(f2))
# print(f1.times(f2))

# Special operators implemented with dunder methods
# Define them with double underscores before/after
# __add__(self, other)        --> self + other
# __sub__(self, other)        --> self - other
# __mul__(self, other)        --> self * other
# __truediv__(self, other)    --> self/other
# __eq__(self, other)         --> self == other
# __lt__(self, other)         --> self < other
# __len__(self)               --> len(self)
# __str__(self)               --> print(self)
# __float__(self)             -->float(self)
# __pow__                     --> self ** other

# Print representation of an object
# >>> c = Coordinate(3,4)
# >>> print(c)
# <__main__.Coordinate object at 0x7fa918510488>
# Uninformative print representation by default
# Define a __str__ method for a class
# Python calls the __str__ method when used with print on your class object
# You choose what it does!Say that when we print a Coordinate object, want to show
# >>> print(c)
# <3,4>

"""Defining our own Print Method"""
# class Coordinate(object):
#     def __init__(self, xval, yval):
#         self.x = xval
#         self.y = yval
#     def distance(self, other):
#         x_diff_sq = (self.x - other.x)**2
#         y_diff_sq = (self.y - other.y)**2
#         return (x_diff_sq + y_diff_sq)**0.5
#     def __str__(self):
#         return "<"+str(self.x)+","+str(self.y)+">"
    
# c = Coordinate(3,4)
# print(c)
# print(type(c))

# print(Coordinate)
# print(type(Coordinate))
# print(isinstance(c, Coordinate))

# Print fraction using dunder method
# class Fraction(object):
#     def __init__(self, n, d):
#         self.num = n
#         self.denom = d
#     def __str__(self):
#         if self.denom == 1:
#             return str(self.num)
#         else:
#             return str(self.num) + "/" + str(self.denom)
    
# f1 = Fraction(3,4)
# f2 = Fraction(1,4)
# f3 = Fraction(5,1)
# print(f1)
# print(f2)
# print(f3)

# Class can hide details
# These are all equivalent
# print(a * b)
# print(a.__mul__(a,b))
# print(Fraction.__mul__(a, b))
# NOTE: Special operations we've been using are just methods behind
# the scenes. Things like: print, len, +, *, <,>,etc
