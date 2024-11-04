import simfin as sf
import pandas as pd

# Set your API-key for downloading data. This key gets the free data.
sf.set_api_key('6cfb94d9-38c9-47ad-8915-9a2d9521e138')

income = sf.load_income(variant='annual', market='us').reset_index()
balance = sf.load_balance(variant='annual', market='us').reset_index()
cashflow = sf.load_cashflow(variant='annual', market='us').reset_index()    

# Merge the income, balance, and cashflow statements
data = pd.merge(income, balance, on=['Ticker', 'Report Date', 'SimFinId'])
data = pd.merge(data, cashflow, on=['Ticker', 'Report Date', 'SimFinId'])   

# Calculate the return on assets (ROA)
data['ROA'] = data['Net Income'] / data['Total Assets']

# Calculate the return on equity (ROE)
data['ROE'] = data['Net Income'] / data['Shareholders Equity']

# Calculate the free cash flow (FCF)
data['FCF'] = data['Operating Cash Flow'] - data['Capex']

# Calculate the free cash flow to equity (FCFE)
data['FCFE'] = data['FCF'] - data['Net Debt Issuance']

# Calculate the price-to-earnings (P/E) ratio
data['P/E'] = data['Market Cap'] / data['Net Income']

# Calculate the price-to-book (P/B) ratio
data['P/B'] = data['Market Cap'] / data['Shareholders Equity']

# Calculate the price-to-sales (P/S) ratio
data['P/S'] = data['Market Cap'] / data['Revenue']

# Calculate the price-to-cashflow (P/CF) ratio



