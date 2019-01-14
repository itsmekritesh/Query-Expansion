import webbrowser
import requests
import bs4
import re

def start(keyword):
    res = requests.get('https://in.search.yahoo.com/search?p='+keyword)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #print(soup)
    links = soup.select('div > span')
    #print(links)
    
    tab_counts = min(10, len(links))
    print(tab_counts)
    i=0
    #j=0
    k=0
    while i<11:
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', str(links[k]))
        k+=1
        #print(cleantext)
        print("  ")
        s=cleantext[:4]
        if(cleantext=="" or cleantext==" "):
            continue
        if(s!='http'):
            cleantext='https://'+cleantext
        #print(links[i])
        print(cleantext)
        #webbrowser.open(str(cleantext))
        i+=1

start("swine flu vaccine")
