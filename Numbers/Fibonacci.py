#Calculates either the Nth fibonacci number or calculates which Fibonacci number is smaller than a given number


def fibonacci_n(num):
    if num == 1:
        return 0
    if num == 2 or num == 3:
        return 1
    i = 4
    current = 2
    previous = 1    
    while i < num:
        current = current + previous
        previous = current - previous
        i += 1
        print current, previous    
    return current


def fibonacci_max(num):
    if num == 1:
        return 2
    i = 2
    current = 1
    previous = 1
    while current < num:
        current = current + previous
        previous = current - previous
        i += 1    
    return i


#Prints out a Fibonacci sequence

input_type = raw_input("Do you want to input 'Nth' number of 'Max' number?: ")
while True:
    if input_type == "Nth":
        print "NTH"
        nth = raw_input("Choose the Fibonacci number, must be a number: ")
        print nth + ". Fibonacci number is " + str(fibonacci_n(int(nth)))
        break
    elif input_type == "Max":
        print "MAX"
        maxi = raw_input("Choose the max. Fibonacci number, must be a number: ")
        print "The largest fibonacci number below " + maxi + " is the " + str(fibonacci_max(int(maxi))) + "Fibonacci number"
        break
    else:
        input_type = raw_input("Wrong input. Do you want to input 'Nth' number of 'Max' number?: ")


