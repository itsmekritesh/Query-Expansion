import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup
import re

def search(keyword):
    
    res = requests.get('https://www.bing.com/search?q='+keyword)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    links = soup.select('cite')
    tab_counts = min(10, len(links))
    
    for i in range(tab_counts):     #opening top 10 links
        cleaner=re.compile('<.*?>')
        cleantxt=re.sub(cleaner, '',str(links[i]))
        #print(links[i])
        print(cleantxt)
        webbrowser.open(cleantxt)

search(keyword)    
