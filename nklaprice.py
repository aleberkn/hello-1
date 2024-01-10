import yfinance as yf

# Get the data for the stock NKLA
stock_data = yf.Ticker("NKLA")

# Get the current stock price
current_price = stock_data.info["currentPrice"]

# Print the current stock price
print(f"The current stock price of NKLA is ${current_price:.2f}")
