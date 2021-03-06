# -*- coding: utf-8 -*-
#Ideja za več operacij. Ustvari prazen seznam v katerega se appenda posamezne dele.
#Pred appendanjem iz vnesenega izraza pobriši whitespace in ko zaznaš operacijo preskoči en znak (s tem skenslaš *- in podobno)

#All basic calculations
def addition(a,b):
    return a + b

def division(a,b):
    return float(a)/ b

def multiplication(a,b):
    return a * b

def subtraction(a,b):
    return a - b

def power(a,b):
    return a**b

"""print Welcome to a simple calculator.
 Please enter the expression you want to calculate.
 Allowed operations are +, -, *, /.

stevka = raw_input(">: ")
result = 0"""


def calculation(calc, operacije, stevilke): #Performes all the calculations in sequence
    nove_stevilke = []
    nove_operacije = []
    print operacije, stevilke
    if len(operacije) != 0:
        for i in range(0, len(operacije)):
            print i, nove_stevilke
            seznam_operacij = {"**" : power(float(stevilke[i]), float(stevilke[i+1])),
                            "*" : multiplication(float(stevilke[i]), float(stevilke[i+1])),
                            "/" : division(float(stevilke[i]), float(stevilke[i+1])),
                            "+" : addition(float(stevilke[i]), float(stevilke[i+1])),
                            "-" : subtraction(float(stevilke[i]), float(stevilke[i+1]))}
            
            if operacije[i] == calc:
                nove_stevilke.append(seznam_operacij[calc]) #TREBA JE DODATI ŠE ZADNJI ČLEN PRI ŠTEVILKAH IN ZAGOTOVITI, DA SE ENA ŠTEVILKA OPERACIJI PO IZBRIŠE
            else:
                nove_stevilke.append(stevilke[i])
                nove_operacije.append(operacije[i])
    else:
        nove_operacije = operacije
        nove_stevilke = stevilke
    return nove_operacije, nove_stevilke

#Creates a list of operations and a list of numbers 
def interface(vnos):
    previous = 0
    stevilke = []
    operacije = []    
    vnos = vnos.replace(" ", "")
    for i in range(0, len(vnos)):
        #print vnos[i:i+2] 
        #Special condition for "**" because it has 2 chars 
        if vnos[i:i+2] == "**":
            stevilke.append(vnos[previous:i])
            operacije.append(vnos[i:i+2])
            previous = i+2
        #All the other operations            
        elif vnos[i] == "*" or vnos[i] == "/" or vnos[i] == "+" or vnos[i] == "-" :
            #To remove additional "*" if "**" is present            
            if vnos[i] == "*" and len(operacije) != 0:
                if operacije[-1] == "**":
                    pass
                else:
                    stevilke.append(vnos[previous:i])
                    operacije.append(vnos[i:i+1])
                    previous = i+1      
            else:
                stevilke.append(vnos[previous:i])
                operacije.append(vnos[i:i+1])
                previous = i+1
      
    stevilke.append(vnos[previous:]) #appends the final number
    operacije, stevilke =  calculation("**", operacije, stevilke)
    operacije, stevilke =  calculation("*", operacije, stevilke)
    operacije, stevilke =  calculation("/", operacije, stevilke)
    operacije, stevilke =  calculation("+", operacije, stevilke)
    operacije, stevilke =  calculation("-", operacije, stevilke)
    return stevilke

print interface("4 + 3.5 ** 3") == 29
"""print interface("3.2 - 4.5") == -1.3
print interface("4.2 * 2") == 8.4
print interface("4.2 / 2.1") == 2
print interface("5.3 * -1.7") == -9.01
print interface("3.24 - 2.3") == 0.94"""
