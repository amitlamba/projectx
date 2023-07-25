import requests
from bs4 import BeautifulSoup
import pandas as pd

# def addToDict(companyName):
def addDataToExcel(companyName,companyShortForm): #for Reliance 
    result_dict={}

    for i in range(1, 5):

        url = "https://www.moneycontrol.com/financials/"+companyName+"/ratiosVI/"+companyShortForm+"/"+ str(i)+"#"+companyShortForm  # Replace with the URL of the website you want to scrape
        # print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        table = soup.find('table', class_='mctable1')

        # Extract table headers (th elements)
        if table is not None:
            headers = [th.text for th in table.find_all('th')]

            # Extract table rows (tr elements)
            rows = []
            for row in table.find_all('tr'):
                row_data = [td.text for td in row.find_all('td')]
                rows.append(row_data)

            
           
            for row in rows:
                
                isFinancialRatios = row[0].find("Key Financial Ratios of Reliance Industries (in Rs. Cr.)")
                if isFinancialRatios != -1:
                
                    if 'Year' in result_dict:
                        insertAt=len(result_dict['Year'])
                        ID = 'Year'
                        
                        i = 1
                        
                        # Run the while loop until the value is not equal to '\xa0'
                        while row[i] != '\xa0':
                            
                            result_dict[ID][insertAt]=row[i]
                            insertAt+=1;
                            i+=1
                        
                        data = pd.DataFrame(result_dict)
                    else :
                        ID = 'Year'
                        result_dict[ID] = {i: value for i, value in enumerate(row[1:], start=0) if value != '\xa0'}
                        data = pd.DataFrame(result_dict)
                
                isBasicEPS = row[0].find("Basic EPS (Rs.)")
                
                if isBasicEPS != -1:
                    
                    if 'Basic EPS (Rs.)' in result_dict:
                        insertAt=len(result_dict['Basic EPS (Rs.)'])
                        ID = row[0]
                        
                        i = 1
                        
                        # Run the while loop until the value is not equal to '\xa0'
                        while row[i] != '\xa0':
                            result_dict[ID][insertAt]=row[i]
                            insertAt+=1;
                            i+=1
                        
                        data = pd.DataFrame(result_dict)
                    else :
                        ID = row[0]
                        result_dict[ID] = {i: value for i, value in enumerate(row[1:], start=0) if value != '\xa0'}
                        data = pd.DataFrame(result_dict)
                    
                
                
                isTotalDebt_Equity = row[0].find("Total Debt/Equity (X)")
                if isTotalDebt_Equity != -1:
                
                    if 'Total Debt/Equity (X)' in result_dict:
                        insertAt=len(result_dict['Total Debt/Equity (X)'])
                        ID = row[0]
                        
                        i = 1
                        
                        # Run the while loop until the value is not equal to '\xa0'
                        while row[i] != '\xa0':
                            
                            result_dict[ID][insertAt]=row[i]
                            insertAt+=1;
                            i+=1
                        
                        data = pd.DataFrame(result_dict)
                    else :
                        ID = row[0]
                        result_dict[ID] = {i: value for i, value in enumerate(row[1:], start=0) if value != '\xa0'}
                        data = pd.DataFrame(result_dict)
                
                isPriceToBook = row[0].find("Price/BV (X)")
                if isPriceToBook != -1:
                    if 'Price/BV (X)' in result_dict:
                        insertAt=len(result_dict['Price/BV (X)'])
                        ID = row[0]
                        
                        i = 1
                        # Run the while loop until the value is not equal to '\xa0'
                        while row[i] != '\xa0':
                            
                            result_dict[ID][insertAt]=row[i]
                            insertAt+=1;
                            i+=1
                        data = pd.DataFrame(result_dict)
                    else :
                        ID = row[0]
                        result_dict[ID] = {i: value for i, value in enumerate(row[1:], start=0) if value != '\xa0'}
                        data = pd.DataFrame(result_dict) 
                    
                    
    data.to_excel(companyName+".xlsx")       # storing into the excel file         

company_Names=[ 

    ("relianceindustries","RI") 
    # ("tataconsultancyservices" ,"TCS"),
    # ("hdfcbank","HDF01"),
    # ("icicibank","ICI02"),
    # ("hindustanunilever","HU")

]
 
if __name__ == "__main__":

    for company in company_Names :
      addDataToExcel(company[0],company[1]);

   
