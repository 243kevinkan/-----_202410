pip install numpy-financial
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import numpy_financial as npf # import numpy-financial

tickers = ["SPY", "VOO", "IVV", "VTI", "QQQ", "IWM", "EEM", "EFA", "VEA", "XLU"]

# Create an empty dictionary to store the Sharpe ratios
sharpe_ratios = {}

# Create an empty dictionary to store the annualized returns
annualized_returns = {}

# Loop through each ticker
for ticker in tickers:
    # Download the historical price data for the past max years
    data = yf.download(ticker, period="max")
    
    # Calculate the daily returns
    data["daily_return"] = data["Adj Close"].pct_change()
    
    # Calculate the annualized Sharpe ratio
    sharpe_ratio = data["daily_return"].mean() / data["daily_return"].std() * np.sqrt(252)
    
    # Calculate the annualized return
    annualized_return = (1 + data["daily_return"].mean()) ** 252 - 1

    # Store the Sharpe ratio in the dictionary
    sharpe_ratios[ticker] = sharpe_ratio
    # Store the annualized return in the dictionary
    annualized_returns[ticker] = annualized_return

# Sort the dictionary by values in descending order
sorted_sharpe_ratios = sorted(sharpe_ratios.items(), key=lambda x: x[1], reverse=True)

# Get the top 3 tickers with the highest Sharpe ratios
top_3_tickers = [ticker for ticker, _ in sorted_sharpe_ratios[:3]]

# Print the top 3 tickers and their Sharpe ratios and annualized returns
# Calculate the required annual investment amount for the top 3 tickers to achieve the total amount of 15000000 
# The rate is annulized return, duration is 30 years and the future value is 15000000

for ticker, sharpe_ratio in sorted_sharpe_ratios[:3]:
    annual_investment_amount = npf.pmt(annualized_returns[ticker], 30, 0, -15000000) # use npf.pmt
    print(f"The top 3 tickers are: {top_3_tickers}")
    print(f"The annualized Sharpe ratio for {ticker} is {sharpe_ratio}")
    print(f"The annualized return for {ticker} is {annualized_returns[ticker]}")
    print(f"The required annual investment amount for {ticker} to achieve the total amount of 1500000 is {annual_investment_amount}")


# # Plot the price data for the top 3 tickers
# for ticker in top_3_tickers:
#     data = yf.download(ticker, period="10y")
#     plt.plot(data.index, data["Adj Close"], label=ticker)

# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.title("Price Data for Top 3 ETFs")
# plt.legend()
# plt.show()