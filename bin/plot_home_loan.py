import home_loan as hl 

class HomeLoan:

    def __init__(self, principal, interest_rate, loan_period):
        self.principal = principal
        self.i = interest_rate
        self.loan_period = loan_period
        self.p = loan_period * 12

    def plot_repayments(self):
        xValues = hl.create_array(self.p)
        yValues = [hl.loan_balance(self.principal, self.i, self.loan_period, p) for p in xValues]
        hl.make_plot(xValues, yValues, 'Debt Value ($)', 'Time (Months)', 'Debt Repayment')
    
    def plot_cummulative_interest(self):
        xValues = hl.create_array(self.p)
        yValues = [hl.cummulative_interest(self.principal, self.i, self.loan_period, p) for p in xValues]
        hl.make_plot(xValues, yValues, 'Cummulative Interest', 'Time (Months)', 'Interest Paid')
    
    def make_plot(x, y, xlabel, ylabel, title):
        plt.plot(x, y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

if __name__ == "__main__": 
    HomeLoan(500000, 0.0465, 30).plot_repayments()
