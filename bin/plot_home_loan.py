import home_loan as hl 

def plot_repayments(hl. p):
    xValues = hl.create_array(p)
    yValues = [hl.loan_balance(p) for p in xValues]
    hl.make_plot(xValues, yValues, 'Debt Value ($)', 'Time (Months)', 'Debt Repayment')

def plot_cummulative_interest(hl.p):
    xValues = hl.create_array(p)
    yValues = [hl.cummulative_interest(p) for p in xValues]
    hl.make_plot(xValues, yValues, 'Cummulative Interest', 'Time (Months)', 'Interest Paid')

def make_plot(hl. x, y, xlabel, ylabel, title):
    plt.plot(xValues, yValues)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

