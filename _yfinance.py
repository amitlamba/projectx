import yfinance as yf
import pandas as pd
def get_historical_data(stock_symbol, years=20):
    # Get the ticker object for the stock symbol
    stock = yf.Ticker(stock_symbol)

    # Get historical data for the stock
    historical_data = stock.history(period=f"{years}y")

    return historical_data


if __name__ == "__main__":
    stock_symbol = "RELIANCE.NS"  # Stock symbol
    years = 20  # Replace with the desired number of years

    
    historical_data = get_historical_data(stock_symbol, years)
    
    if not historical_data.empty:
       df = pd.DataFrame(historical_data)
       df.to_excel("historical_data_"+stock_symbol+'.xlsx', index=False)
    
