import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup

def start(keyword):

    res = requests.get('https://google.com/search?q='+keyword)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    links = soup.select('.r a')
    tab_counts = min(10, len(links))
    
    for i in range(tab_counts):     #opening top 10 links
        #webbrowser.open('https://google.com' + links[i].get('href'))
        link = 'https://google.com' + links[i].get('href')
        page = requests.get(link)
        soup = BeautifulSoup(page.content,'html.parser')
        
        #writing content of each page to a text file
        with open("C:\\Users\\DELL\\Desktop\\Project\\New data\\paragraph.txt", 'a') as filehandle:
            for x in soup.find_all('header'):
                filehandle.write(x.get_text()+"\n")
            for x in soup.find_all('p'):
                filehandle.write(x.get_text()+"\n")

start('swine flu vaccine')
    

'''with open("C:\\Users\\DELL\\Desktop\\Project\\New data\\query_list.txt",'r') as filehandle:
    while True:
        key=filehandle.readline()
        if key=="":
            break
        #print(key)
        start(key)'''
    
 
from nltk.tag.stanford import StanfordPOSTagger
import nltk
import os

java_path = "C:\\Program Files\\Java\\jre1.8.0_181\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path
nltk.internals.config_java("C:/Program Files/Java/jre1.8.0_191/bin/java.exe")
myTagger = StanfordPOSTagger('C:\\Users\\DELL\\Desktop\\Project\\stanford-postagger-2018-10-16\\models\\english-bidirectional-distsim.tagger','C:\\Users\\DELL\\Desktop\\Project\\stanford-postagger-2018-10-16\\stanford-postagger.jar')
#myTagger.tag('What is the airspeed of an unladen swallow ?'.split())
 
def tagger():  
    
    with open("C:\\Users\\DELL\\Desktop\\Project\\New data\\paragraph.txt", 'r') as file:
        while(True):
            str=file.readline()
            if str=="":
                break
            list_tagged = myTagger.tag(str.split())
            #print(list_tagged)
            s=""
            for obj in list_tagged:
                s += obj[0] + "_" + obj[1] + " "
            with open("C:\\Users\\DELL\\Desktop\\Project\\New data\\paragraph_tagged.txt", 'a') as filehandle:
                filehandle.write(s+"\n")
        
tagger()

