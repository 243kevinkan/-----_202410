# count=1
# for ticker, sharpe_ratio in sorted_sharpe_ratios[:3]:
#     monthly_investment_amount = round(npf.pmt(annualized_returns[ticker]/12, years_left*12, 0, -total_amount_needed),0) # use npf.pmt
#     print("<",count,">")
#     count += 1
#     print(f"The required monthly investment amount for {ticker} to achieve the total amount of ${total_amount_needed:,.0f} is ${monthly_investment_amount:,.0f}")

# chosen_ticker = input("Choose one from the top 3 tickers: ")
# #if the user does not input the tickers, ask the user to choose again
# while chosen_ticker not in top_3_tickers:
#     chosen_ticker = input("Invalid input. Please choose one from the top 3 tickers: ")

# monthly_contribution = eval(input("Enter the monthly contribution you want to invest in: "))
# # Calculate the future value of the investment
# future_value = monthly_contribution * ((1 + annualized_returns[chosen_ticker]/12) ** (years_left*12) - 1) / (annualized_returns[chosen_ticker]/12)
# print(chosen_ticker,":", f"The future value of the investment in retirement is: ${future_value:,.0f}")

# # Ask the user if they want to invest other tickers
# other_tickers = input("Do you want to invest in other tickers? (yes/no): ")
# # Loop until the user does not input year or no
# while other_tickers != "yes" and other_tickers != "no":
#     other_tickers = input("Invalid input. Please enter yes or no: ")

# total_future_value = future_value
# # Loop until the user does not want to invest in other tickers
# while other_tickers == "yes":
#     chosen_ticker = input("Choose one from the top 3 tickers: ")
#     while chosen_ticker not in top_3_tickers:
#         chosen_ticker = input("Invalid input. Please choose one from the top 3 tickers: ")
#     monthly_contribution = eval(input("Enter the monthly contribution you want to invest in: "))
#     future_value = monthly_contribution * ((1 + annualized_returns[chosen_ticker]/12) ** (years_left*12) - 1) / (annualized_returns[chosen_ticker]/12)
#     print(chosen_ticker,":", f"The future value of the investment in retirement is: ${future_value:,.0f}")
#     total_future_value += future_value
#     other_tickers = input("Do you want to invest in other tickers? (yes/no): ")
#     print("The total future value of the investment in retirement is: ", f"${total_future_value:,.0f}")

# Difference = total_future_value - total_amount_needed
# print("The total future value of the investment in retirement is: ", f"${total_future_value:,.0f}")
# print("The difference between the total future value and the total amount of money needed for retirement is: ", f"${Difference:,.0f}")
# #If the difference is positive, print "You will have more than enough money for retirement."
# if Difference > 0:
#     print("You will have more than enough money for retirement.")
# #If the difference is negative, print "You will not have enough money for retirement."
# else:
#     print("You will not have enough money for retirement.")