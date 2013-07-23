#Calculates the value of Pi to the Nth decimal place
# Uses Bailey–Borwein–Plouffe formula - http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
def calc_pi(num):
    limit = 10**-(num+1)
    current = 0
    previous = 1
    k = 0
    while abs(current-previous) > limit:
        previous = current
        addition = 4. / ((16.0**k) * (8*k+1)) - 2./((16**k) * (8*k + 4)) - 1. / ((16**k) * (8 * k + 5)) - 1. / ((16**k) * (8 * k + 6))
        current = current + addition
        k += 1
    return "Pi to the {}th decimal place is {:.{precision}f}".format(str(num), current, precision = num)

decimals = raw_input("To how many decimals do you want to calculate the value of Pi?: ")
print calc_pi(int(decimals))
