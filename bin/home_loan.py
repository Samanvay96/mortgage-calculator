import matplotlib.pyplot as plt
import numpy as np

# class HomeLoan:

#    def __init__(self, principal, interest_rate, loan_period):
#        principal = principal
#        self.i = interest_rate
#        self.loan_period = loan_period

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

#    def plot_repayments(self, p):
#        xValues = self.create_array(p)
#        yValues = [self.loan_balance(p) for p in xValues]
#        self.make_plot(xValues, yValues, 'Debt Value ($)', 'Time (Months)', 'Debt Repayment')
#
#    def plot_cummulative_interest(self,p):
#        xValues = self.create_array(p)
#        yValues = [self.cummulative_interest(p) for p in xValues]
#        self.make_plot(xValues, yValues, 'Cummulative Interest', 'Time (Months)', 'Interest Paid')

def r(i):
    return self.i / 12

def n(loan_period):
    return loan_period * 12.0

def create_array(p):
    return np.add(range(p), 1)

#    def make_plot(self, x, y, xlabel, ylabel, title):
#        plt.plot(xValues, yValues)
#        plt.xlabel(xlabel)
#        plt.ylabel(ylabel)
#        plt.title(title)
#        plt.show()

#if __name__ == "__main__": 
#    HomeLoan(500000, 0.0465, 30).plot_repayments(12*30)
