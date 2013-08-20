# -*- coding: utf-8 -*-
#""" (temp, currency, volume, mass and more)** – Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion."""

unit_one = raw_input("Enter initial unit \n Allowed values are 'ug', 'mg', 'g', 'dg', 'kg', 't', 'um', 'mm', 'cm', 'dm', 'm', 'km', 'um3', 'mm3', 'cm3', 'dm3', 'm3', 'km3'\n:")
value_one = float(raw_input("Enter a value: "))
if unit_one == "ug" or unit_one == "mg" or unit_one == "g" or unit_one == "dg" or unit_one == "kg" or unit_one == "t":
	unit_two = raw_input("Enter the second unit. \n Allowed values are 'ug', 'mg', 'g', 'dg', 'kg', 't'\n")
	if unit_one == "ug":
		value = value_one / 1000000
	elif unit_one == "mg":
		value = value_one / 1000
	elif unit_one == "g":
		value = value_one
	elif unit_one == "dg":
		value = value_one * 10
	elif unit_one == "kg":
		value = value_one * 1000
	elif unit_one == "t":
		value = value_one * 1000000
	if unit_two == "ug":
		value = value * 1000000
	elif unit_two == "mg":
		value = value * 1000
	elif unit_two == "g":
		value = value
	elif unit_two == "dg":
		value = value / 10
	elif unit_two == "kg":
		value = value / 1000
	elif unit_two == "t":
		value = value / 1000000
	print "%s %s is %s %s" % (str(value_one), unit_one, str(value), unit_two)  
