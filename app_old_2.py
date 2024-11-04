import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import sys
import numpy_financial as npf # import numpy-financial

#Step 1: 理財目標設定

#Let the user input his/her current age and the age he/she wants to retire. Then calculate the number of years left until retirement
current_age= eval(input("Please enter your current age: "))
retire_age= eval(input("Please enter the age you want to retire: "))
years_left = retire_age - current_age
print("The number of years left until retirement: ", years_left)

#Let the user input how much money he/she wants to spend each year during the retirement. Then calculate the total amount of money needed for retirement
annual_spending = eval(input("Enter the amount of money you want to spend each year during retirement: "))
expected_return_after_retirement = 0.04
total_amount_needed = int(annual_spending /expected_return_after_retirement)
print("The　expected_return is 4% after retirement")
print(f"The total amount needed for retirement is: ${total_amount_needed:,.0f}")

#Step 2: 標的篩選
# Ask the user if the system to select the top 5 ETFs for the user
select_top_ETFs = input("Do you want the system to select the top 5 ETFs for you? (yes/no): ")  
# Loop until the user does not input year or no
while select_top_ETFs != "yes" and select_top_ETFs != "no":
    select_top_ETFs = input("Invalid input. Please enter yes or no: ")
# If the user wants the system to select the top 5 ETFs for the user, print "The system will select the top 5 ETFs for you."
if select_top_ETFs == "yes":
    print("The system will select the top 5 ETFs for you.")
# If the user does not want the system to select the top 5 ETFs for the user, print "You have chosen not to let the system select the top 5 ETFs for you."
else:
    print("You have chosen not to let the system select the top 5 ETFs for you.")
    print("Goodbye!")
    sys.exit(0)

# Define a top 10 list of US stock ETF tickers by assets under management (AUM)
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

# Get the top 5 tickers with the highest Sharpe ratios
top_5_tickers = [ticker for ticker, _ in sorted_sharpe_ratios[:5]]
# Get the top 5 tickers' annualized returns 
top_5_annualized_returns = {ticker: annualized_returns[ticker] for ticker in top_5_tickers}

# Print the top 5 tickers
# Print their Sharpe ratios and annualized returns round to 2 decimals
print("The top 5 tickers are: ", top_5_tickers)
print("")

for ticker, sharpe_ratio in sorted_sharpe_ratios[:5]:
    print(f"The annualized Sharpe ratio for {ticker} is {sharpe_ratio:.2f}")
    print(f"The annualized return for {ticker} is {annualized_returns[ticker]:.2f}")
    print("")

# Plot the price data for the top 5 tickers
for ticker in top_5_tickers:
    data = yf.download(ticker, period="max")
    plt.plot(data.index, data["Adj Close"], label=ticker)

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Price Data for Top 5 ETFs")
plt.legend()
plt.show()




