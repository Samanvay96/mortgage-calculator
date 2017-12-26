import numpy as np
import home_loan as hl

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure

# Set up data
p = 360
x = hl.create_array(p)
y = [hl.loan_balance(500000, 0.05, 30, p) for p in x]

source = ColumnDataSource(data=dict(x=x, y=y))

# Set up plot
plot = figure(plot_height=600, plot_width=700, title="Outstanding Loan Balance w.r.t Time",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 500], y_range=[0, 500000*2])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
plot.xaxis.axis_label = 'Time (Months)'
plot.yaxis.axis_label = 'Outstanding Amount ($)'

# Set up widgets
interest_rate = Slider(title="Interest Rate", value=0.05, start=0.01, end=0.1, step=0.01)
principal_amount = Slider(title="Principal ($)", value=500000, start=50000, end=500000*2, step=50000)
t = Slider(title="Loan Period (Years)", value=30, start=10, end=40, step=1)

# Set up callbacks
def update_data(attrname, old, new):

    # Get the current slider values
    i = interest_rate.value
    principal = principal_amount.value
    loan_period = t.value

    # Generate the new curve
    x = hl.create_array(loan_period*12)
    y = [hl.loan_balance(principal, i, loan_period, p) for p in x]

    source.data = dict(x=x, y=y)

for w in [interest_rate, principal_amount, t]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = widgetbox(interest_rate, principal_amount, t)

curdoc().add_root(row(plot, inputs, width=800))
