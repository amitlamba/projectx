import yfinance as yf
import pandas as pd
def get_historical_data(stock_symbol, years=20):
    # Get the ticker object for the stock symbol
    stock = yf.Ticker(stock_symbol)

    # Get historical data for the stock
    historical_data = stock.history(period=f"{years}y")

    return historical_data

def addHistoricalDataToExcelFile(stock_symbol,years):
    historical_data = get_historical_data(stock_symbol, years)

    
    if not historical_data.empty:
       df = pd.DataFrame(historical_data)
       df.insert(0, 'Date', df.index.strftime("%Y-%m-%d"))
       df.to_excel("HD_"+symbol+"_using_yfinanceLib.xlsx", index=False)

if __name__ == "__main__":
    
    stock_symbols = ["RELIANCE.NS","TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "HINDUNILVR.NS"]
    years = 20  # Replace with the desired number of years

    for symbol in stock_symbols:
        addHistoricalDataToExcelFile(symbol,years)

    
    
