import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup
import re
from validator_collection import checkers

def start(keyword):
    res = requests.get('https://in.search.yahoo.com/search?p='+keyword)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    #print(soup)
    links = soup.select('div > span')
    
    #tab_counts = min(10, len(links))
    #print(tab_counts)
    i=0
    #j=0
    k=0
    while i<11 and k<len(links):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', str(links[k]))
        k+=1
        #print(cleantext)
        #print("  ")
        s=cleantext[:4]
        
        if(s!='http'):
            cleantext='https://'+cleantext
        
        if(not checkers.is_url(cleantext)):
            continue
        #print(links[i])
        #print(cleantext)
        #webbrowser.open(str(cleantext))
        i+=1
        
        link =cleantext
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        # writing content of each page to a text file
        name = "paragraph" + str(i) + ".txt"
        with open("C:\\Users\\DELL\\Desktop\\Project\\Yahoo\\paragraph\\" + name, 'w') as filehandle:
            for x in soup.find_all('header'):
                filehandle.write(x.get_text() + "\n")
            for x in soup.find_all('p'):
                filehandle.write(x.get_text() + "\n")

start("swine flu vaccine")
