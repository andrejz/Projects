#Calculates the monthly mortage payment based on the value of a loan, interest rate and time of payment
# -*- coding: utf-8 -*-

loan = raw_input("Enter loaned amount in €: ")
rate = raw_input("Enter yearly interest rate in %: ")
years = raw_input("How many years do you plan to take the loan for?: ")

if rate == 0:
    rate = raw_input("Enter yearly interest rate in % (must be > 0): ")

m_rate = float(rate)/1200
months = int(float(years)*12)

payment = float(loan) * m_rate / (1 - (1 + m_rate)**-months)
print "You will need to pay {0:.{prec}f} € per month.".format(payment, prec=3)
