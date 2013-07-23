#Have the program find prime numbers until the user chooses to stop asking for the next one.

def is_prime(num):
    i = 2
    limit = num**0.5
    while i <= limit:
        
        if num %i == 0:
            return False
            break
        i += 1
    return True

def find_next(num):
    test = num + 1
    while not is_prime(test):
        test += 1
    return test

prime = 1 
while True:
    prime = find_next(prime)
    print "Next prime number is {}".format(prime)
    answer = raw_input("Do you want another prime? (Y/N): ")
    if answer == "N":
        print "You've chosen to end the program."
        break


