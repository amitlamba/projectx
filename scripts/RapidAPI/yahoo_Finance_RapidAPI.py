import requests
from datetime import datetime
import pandas as pd
import time
import json
import os

def convert_Epoch_To_DateTime (epoch):
    from datetime import datetime
    
    datetime_obj=datetime.fromtimestamp(epoch)
    
    return datetime_obj

def get_HistoricalData_rapidAPI(symbol):

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"
    
    current_time_epoch = int(time.time())
    querystring = {
        "period1":"1041379200",
        "period2":current_time_epoch,
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

    
    data = {"prices": data["prices"]}
    
    
    df = pd.DataFrame(data["prices"])
    df['date'] = pd.to_datetime(df['date'], unit='s').dt.strftime('%Y-%m-%d')
   
    df = df[df["open"].notnull()] 
    
    
    df = df.reset_index(drop=True)  #drop empty rows
    df = df.dropna(axis=1, how='all') # drop empty columns

    cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parent_directory = os.path.dirname(cur_dir)
       
    output_directory = os.path.join(parent_directory, 'data')
    hist_folder = os.path.join(output_directory, "hist_data")
    rAPI = os.path.join(hist_folder, "RapidAPI")
    if not os.path.exists(rAPI):
                os.makedirs(rAPI)
       
    output_filename="HD_"+symbol+"_using_RapidAPI.xlsx"
    excel_file_path = os.path.join(rAPI, output_filename)
       
    df.to_excel(excel_file_path, index=False)
    

   

  


if __name__ == "__main__":
     stock_symbols = ["RELIANCE.NS","TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "HINDUNILVR.NS"]
     
     for symbol in stock_symbols:
         get_HistoricalData_rapidAPI(symbol)
         


    
