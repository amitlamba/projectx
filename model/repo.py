import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url = "https://freefincal.com/rbi-repo-rate-history/"
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    table = soup.find("table")  # Assuming the data is contained within a <table> element
    
    if table:
        rows = table.find_all("tr")
        
        data = []
        for idx, row in enumerate(rows[1:], start=1):  # Skipping the header row
            if idx > 33:  # Skip rows after the 38th row
                break
            
            columns = row.find_all("td")
            
            if len(columns) == 2:
                date_str = columns[0].text.strip()
                repo_rate = columns[1].text.strip().replace('%', '')  # Remove percentage sign
                
                # Convert date to the desired format
                date_obj = datetime.strptime(date_str, "%d-%m-%Y")
                formatted_date = date_obj.strftime("%Y-%m-%d")
                
                data.append({"Date": formatted_date, "RBI Repo Rate": repo_rate})
        
        df = pd.DataFrame(data)
        df.to_excel("rbi_repo_rates.xlsx", index=False)  # Write to Excel file
        print("Data written to 'rbi_repo_rates.xlsx'")
    else:
        print("Table not found on the webpage.")
else:
    print("Error:", response.status_code)
