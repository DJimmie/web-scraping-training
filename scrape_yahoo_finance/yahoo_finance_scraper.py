"""Scraping Yahoo Finance for stocks and financial data."""
# %%
import re
import json
from io import StringIO
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

symbol='APHA'

# %%
url_stats=f'https://finance.yahoo.com/quote/{symbol}/key-statistics?p={symbol}'
url_profile=f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
url_financials=f'https://finance.yahoo.com/quote/{symbol}/financials?p={symbol}'


# %%
def open_site(url):
    # global html,soup
    page = urlopen(url)
    soup = BeautifulSoup(page, 'lxml')

    return page,soup

# %%

def using_request(url):
    response=requests.get(url_financials)
    soup=BeautifulSoup(response.text,'html.parser')
    print(soup)
    pattern=re.compile(r'\s--\Data\s--\s')
    script_data=soup.find('script',text=pattern).contents[0]
    print(script_data)

# %%

if __name__ == '__main__':
    
    page,soup=open_site(url_financials)

    
   
    

# %%
