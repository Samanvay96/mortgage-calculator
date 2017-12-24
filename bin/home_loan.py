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

    def loan_balance(self,p):
        num =  (1 + self.r()) ** self.n() - (1 + self.r()) ** p
        den =  (1 + self.r()) ** self.n() - 1
        return self.principal * (num/den)

    def plot_repayments(self, p):
        xValues = self.create_array(p)
        yValues = [self.loan_balance(p) for p in xValues]
        plt.plot(xValues, yValues)
        plt.ylabel('Debt Value')
        plt.xlabel('Time (Months)')
        plt.show()
    
    def r(self):
        return self.i / 12

    def n(self):
        return self.loan_period * 12.0

    def create_array(self,p):
        return np.add(range(p), 1)

if __name__ == "__main__": 
    HomeLoan(500000, 0.0465, 30).plot_repayments(12*30)
