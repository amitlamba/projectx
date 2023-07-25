import requests
from datetime import datetime
import pandas as pd
import time
import json

def convert_Epoch_To_DateTime (epoch):
    from datetime import datetime
    
    datetime_obj=datetime.fromtimestamp(epoch)
    
    return datetime_obj

def get_HistoricalData_rapidAPI(symbol):

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"
  
   
    querystring = {
        "period1":"1041379200",
        "period2":"1690190100",
        "symbol":symbol,
        "frequency":"1d",
        "filter":"history"}

    headers = {
        # API Key
        "X-RapidAPI-Key": "ce355ee7cbmsh449353194ab637fp1363b7jsn18e41cd77099",
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Response From API
    data = response.json()

 
    for x in data["prices"]:
        try :
            convertedTime=convert_Epoch_To_DateTime(x["date"])
            if(x["close"]==None) : continue
            print(convertedTime ,x["close"])
         
        except:
            continue;

  


if __name__ == "__main__":
    #  stock_symbols = ["RELIANCE.NS","TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "HINDUNILVR.NS"]
     stock_symbols = ["RELIANCE.NS"]
     for symbol in stock_symbols:
         get_HistoricalData_rapidAPI(symbol)
         


    
