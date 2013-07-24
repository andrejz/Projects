#Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
# -*- coding: utf-8 -*-

width = raw_input("Please enter width in m: ")
height = raw_input("Please enter height in m: ")
cost = raw_input("Please enter cost in € / m2: ")

print "The cost to cover the floor is " + str(int(width) * int(height) * int(cost)) + "€."
