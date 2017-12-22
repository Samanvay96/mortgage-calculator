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

    def r(self):
        return self.i / 12

    def n(self):
        return self.loan_period * 12.0

if __name__ == "__main__": 
    HomeLoan(500000, 0.0465, 30).monthly_repayment()
