# -*- coding: utf-8 -*-
#Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

def decimal_to_binary(d):
    return bin(d)

def binary_to_decimal(b):
    return int(str(b),2)

podano = raw_input("Please enter a number for conversion: ")

try:
    if int(podano):
        print "{decimalka} in binary form is {binarno}.".format(decimalka = podano, binarno = decimal_to_binary(int(podano)))
except:
    print "{binarno} in decimal form is {decimalka}.".format(binarno = podano, decimalka = binary_to_decimal(podano))
