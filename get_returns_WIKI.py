__author__ = 'joeross'
# Method for computing log-returns for US Equities

import Quandl as q
import numpy as np
import pandas as pd
import sys

# Quandl API authorization Token
token = "fstXS14pB2xK_pS3zxs6"


def ret_f(ticker, start, end, freq="daily"):
    prices = q.get('WIKI/'+ticker, trim_start=start, trim_end=end, collapse=freq,
                   authtoken=token)
    logret = np.log(prices['Adj. Close'].pct_change() + 1)
    logret = pd.DataFrame(logret)
    logret.columns = [ticker]
    return logret.dropna()

def main():
    symbols = ("IBM", "WMT", "C")
    start_date = "19900101"
    end_date = "20150101"

    print ret_f(symbols[0], start_date, end_date).head()

if __name__ == '__main__':
    main()



