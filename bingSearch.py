import webbrowser
import requests
import bs4
import re

def start(keyword):
    res = requests.get('https://bing.com/search?q='+keyword)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #print(soup)
    links = soup.select('cite')
    #print(links)
    
    tab_counts = min(10, len(links))
    #print(tab_counts)
    for i in range(tab_counts):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', str(links[i]))
        print(cleantext)
        print("  ")
        #print(links[i])
        #print(" ")
        webbrowser.open(str(cleantext))

start("swine flu vaccine")
