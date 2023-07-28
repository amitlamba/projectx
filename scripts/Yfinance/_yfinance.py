import yfinance as yf
import pandas as pd
import os
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

       cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
       parent_directory = os.path.dirname(cur_dir)
       
       output_directory = os.path.join(parent_directory, 'data')
       hist_folder = os.path.join(output_directory, "hist_data")
       yfin = os.path.join(hist_folder, "yfinance")
       if not os.path.exists(yfin):
                os.makedirs(yfin)
       
       output_filename="HD_"+symbol+"_using_yfinanceLib.xlsx"
       excel_file_path = os.path.join(yfin, output_filename)
       
       df.to_excel(excel_file_path, index=False)

if __name__ == "__main__":
    
    stock_symbols = ["RELIANCE.NS","TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "HINDUNILVR.NS"]
    years = 20  # Replace with the desired number of years

    for symbol in stock_symbols:
        addHistoricalDataToExcelFile(symbol,years)

    
    
