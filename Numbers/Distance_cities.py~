#A program to calculate the distance between two Slovenian cities. Needs to fetch coordinates of a city.
import math
import sys

def calc_dist(lat1, long1, lat2, long2):
    
    dtr = 2 * math.pi / 360
    theta1 = (90 - lat1) * dtr
    theta2 = (90 - lat2) * dtr

    psi1 = long1 * dtr
    psi2 = long2 * dtr
    
    dist = math.acos(math.sin(psi1)*math.sin(psi2)*math.cos(theta1-theta2) + math.cos(psi1)*math.cos(psi2)) * 6373
    return dist

def get_coordinates(city):
    with open("SI.txt", "r") as baza:
        dat = baza.read()
        #print dat
        b = dat.split("\t")        
        for i in range(0, len(b)):
            if b[i] == city:
                prva = b[i+3]
                druga = b[i+4]
                prva_a = float(prva)
                druga_a = float(druga)                                
                return prva_a, druga_a
                break
                

mesto1 = raw_input("Please enter 1st city: ")
mesto2 = raw_input("Please enter 2nd city: ")

koord1 = get_coordinates(mesto1)
koord2 = get_coordinates(mesto2)

print "Distance is " + str(calc_dist(koord1[0], koord1[1], koord2[0], koord2[1])) + " km"
