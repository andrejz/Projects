# -*- coding: utf-8 -*-
#The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

price = raw_input("Enter the price in €: ")
payment = raw_input("Enter the amount paid in €: ")

retrn = round(float(payment) - float(price), 2)
n_50 = retrn / 50 
if n_50 >= 1:
    n_50 = round(n_50-0.5, 0)
    retrn = retrn - n_50 * 50
else:
    n_50 = 0
n_20 = retrn / 20 
if n_20 >= 1:
    n_20 = round(n_20-0.5)
    retrn = retrn - n_20 * 20
else:
    n_20 = 0
n_10 = retrn / 10 
if n_10 >= 1:
    n_10 = round(n_10-0.5)
    retrn = retrn - n_10 * 10
else:
    n_10 = 0
n_5 = retrn / 5 
if n_5 >= 1:
    n_5 = round(n_5-0.5)
    retrn = retrn - n_5 * 5
else:
    n_5 = 0
n_2 = retrn / 2 
if n_2 >= 1:
    n_2 = round(n_2-0.5)
    retrn = retrn - n_2 * 2
else:
    n_2 = 0
n_1 = retrn / 1 
if n_1 >= 1:
    n_1 = round(n_1 - 0.5)
    retrn = retrn - n_1
else:
    n_1 = 0
n_05 = retrn / 0.5 
if n_05 >= 1:
    n_05 = round(n_05 - 0.5)
    retrn = retrn - n_05 * 0.5
else:
    n_05 = 0
n_02 = retrn / 0.2 
if n_02 >= 1:
    n_02 = round(n_02 - 0.5)
    retrn = retrn - n_02 * 0.2
else:
    n_02 = 0

n_01 = retrn / 0.1 
if n_01 >= 1:
    n_01 = round(n_01 - 0.5)
    retrn = retrn - n_01 * 0.1
else:
    n_01 = 0

n_005 = retrn / 0.05 
if n_005 >= 1:
    n_005 = round(n_005 - 0.5)
    retrn = retrn - n_005 * 0.05
else:
    n_005 = 0

n_002 = retrn / 0.02 
if n_002 >= 1:
    n_002 = round(n_002 - 0.5)
    retrn = retrn - n_002 * 0.02
else:
    n_002 = 0

n_001 = retrn / 0.01 
if n_001 >= 1:
    n_001 = round(n_001 - 0.5)
else:
    n_001 = 0


print """The amount returned is
         {0} x 50€,
         {1} x 20 €,
         {2} x 10€,
         {3} x 5€,
         {4} x 2 €,
         {5} x 1 € 
         {6} x 0,5 €
         {7} x 0,2 €
         {8} x 0,1 €
         {9} x 0,05 €
         {10} x 0,02 €
         {11} x 0,01 €""".format(int(n_50), int(n_20), int(n_10), int(n_5), int(n_2), int(n_1), int(n_05), int(n_02), int(n_01), int(n_005), int(n_002), int(n_001))
