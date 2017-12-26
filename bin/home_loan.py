import matplotlib.pyplot as plt
import numpy as np

def monthly_repayment(principal, i, loan_period):
    num = r(i)*(1 + r(i))**n(loan_period)
    den = (1 + r(i))**n(loan_period) - 1
    return principal * (num/den) 

def loan_balance(principal, i, loan_period, p):
    num =  (1 + r(i)) ** n(loan_period) - (1 + r(i)) ** p
    den =  (1 + r(i)) ** n(loan_period) - 1
    return principal * (num/den)

def cummulative_interest(principal, i, loan_period, p):
    return (principal * r(i) - monthly_repayment(principal, i, loan_period))* \
            ((1 + r(i)) ** p - 1)/r(i) + monthly_repayment(principal, i, loan_period) * p

def r(i):
    return i / 12

def n(loan_period):
    return loan_period * 12.0

def create_array(p):
    return np.add(range(p), 1)

