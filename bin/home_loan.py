import matplotlib.pyplot as plt
import numpy as np

class HomeLoan:

    def __init__(self, principal, interest_rate, loan_period):
        self.principal = principal
        self.i = interest_rate
        self.loan_period = loan_period

    def monthly_repayment(self):
        num = self.r()*(1 + self.r())**self.n()
        den = (1 + self.r())**self.n() - 1
        print(self.principal * (num/den))
        return self.principal * (num/den) 

    def loan_balance(self, p):
        num =  (1 + self.r()) ** self.n() - (1 + self.r()) ** p
        den =  (1 + self.r()) ** self.n() - 1
        return self.principal * (num/den)

    def cummulative_interest(self, p):
        return (self.principal*self.r - monthly_repayment())* \
                    ((1 + self.r()) ** p - 1)/self.r() + monthly_repayment * p

    def plot_repayments(self, p):
        xValues = self.create_array(p)
        yValues = [self.loan_balance(p) for p in xValues]
        self.make_plot(xValues, yValues, 'Debt Value ($)', 'Time (Months)', 'Debt Repayment')

    def plot_cummulative_interest(self,p):
        xValues = self.create_array(p)
        yValues = [self.cummulative_interest(p) for p in xValues]
        self.make_plot(xValues, yValues, 'Cummulative Interest', 'Time (Months)', 'Interest Paid')

    def r(self):
        return self.i / 12

    def n(self):
        return self.loan_period * 12.0

    def create_array(self,p):
        return np.add(range(p), 1)

    def make_plot(self, x, y, xlabel, ylabel, title):
        plt.plot(xValues, yValues)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

if __name__ == "__main__": 
    HomeLoan(500000, 0.0465, 30).plot_repayments(12*30)
