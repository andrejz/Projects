#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Shape Area and Perimeter Classes** – Create an abstract class called “Shape”
and then inherit from it other shapes like diamond, rectangle, circle, triangle etc.
Then have each class override the area and perimeter functionality to handle each shape type."""

class Shape():
	"""Basic shape class"""
	def __init__(self, name, a, b):
		self.name = name
		self.a = a
		self.b = b
		
	def area(self):
		"""Returns area"""
		self.area = self.a * self.b
		return "Area of shape {0} is {1} units.".format(self.name, self.area)
		
	def perimeter(self):
		"""Returns perimeter"""
		self.perimeter = 2 * self.a + 2 * self.b
		return "Perimeter of shape {0} is {1} units.".format(self.name, self.perimeter)
		
class Square(Shape):
	"""Square class"""
	def __init__(self, name, a):
		self.name = name
		self.a = a
		self.b = a
		
class Triangle(Shape):
	"""Triangle class (for unilaterral triangle)"""
	def __init__(self, name, a):
		self.name = name
		self.a = a
		self.b = a
		self.c = a
	
	def area(self):
		self.area = self.a * self.a * 0.86 / 2
		return "Area of shape {0} is {1} units.".format(self.name, self.area)
		
	def perimeter(self):
		self.perimeter = 3 * self.a
		return "Perimeter of shape {0} is {1} units.".format(self.name, self.perimeter)
		
coolish = Shape("dafaq", 3, 6)
example_tri = Triangle("triangle", 3)
print coolish.area()
print example_tri.area(), example_tri.perimeter()
