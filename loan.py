# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime as dt
from dateutils import month_start, relativedelta
import matplotlib.pyplot as plt
import numpy as np
import numpy_financial as npf
import pandas as pd

sync = month_start(dt.date.today() + dt.timedelta(30))



loan = 360000
rate = 5.875
term = 30
months = term * 12
pmt = npf.pmt(rate / 1200, term * 12, -loan)
pmt_format = f'${pmt:,.2f}'
periods = [sync + relativedelta(months = x) for x in range(months)]
interest = np.array([npf.ipmt(rate / 1200, month, term * 12 , -loan) for month in range(1, months + 1)])
interest_total = f'${interest.sum():,.2f}'
principal = [npf.ppmt(rate / 1200, month, term * 12 , -loan) for month in range(1, months + 1)]

print("Summary")
print("-" * 30)
print(f'Payment: {pmt_format:>21}')
print(f'{"Payoff Date:":19s} {periods[-1]}')
print(f'Interest Paid: {interest_total:>15}')
print("-" * 30)


amort = pd.DataFrame({"Payment" : pmt, 'Interest': interest, 'Principal' : principal}, index = pd.to_datetime(periods))








