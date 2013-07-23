#Have the user enter a number and find all Prime Factors (if there are any) and display them.

def find_prime(num):
    factors = []
    i = 1
    limit = num**0.5
    while i <= limit:
        if num %i == 0:
            divider = num / i
            if divider == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(divider)
        i += 1
        #print i, factors
    return "Factors are: " + str(sorted(factors))

stevka = raw_input("Please enter the number for which you want to determine prime factors: ")

print find_prime(int(stevka))
