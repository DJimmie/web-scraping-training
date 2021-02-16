
# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime as dt
import time
import re

# %%
symbol='APHA'

# url=f'https://finance.yahoo.com/quote/{symbol}/profile?p={symbol}'
url = "http://olympus.realpython.org/profiles/aphrodite"

# %%
def access_site(url):
    
    t1=soup.find_all('title')
    for t in t1:
        print(f'Title:{t.get_text()}\n')
    
    try:
        t2=soup.h1.get_text()
        print(f'h1 Text: {t2}\n')
    except AttributeError as e:
        print(f'Received the following error message while trying to get the h1 tag:\n{e}\n')

# %%
def regex_method(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")

    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title) # Remove HTML tags

    print(title)

# %%
def soup_method(url):
    global soup
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
# %%
# global html,soup
# html = urlopen(url)
# soup = BeautifulSoup(html, 'html.parser')

# %%
page = urlopen(url)

page
# %%
html_bytes = page.read()
# %%
# print(html_bytes)
html = html_bytes.decode("utf-8")
print(html)
# %%
title_index = html.find("<title>")
title_index
# %%
start_index = title_index + len("<title>")
start_index
# %%
end_index = html.find("</title>")
end_index

# %%
title = html[start_index:end_index]
title
# %%
regex_method(url)
# %%
soup_method(url)
# %%
print(soup.get_text())