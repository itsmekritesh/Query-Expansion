import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup

def start(keyword):

    res = requests.get('https://google.com/search?q='+keyword)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    links = soup.select('.r a')
    tab_counts = min(11, len(links))
    
    for i in range(tab_counts):     #opening top 10 links
        #webbrowser.open('https://google.com' + links[i].get('href'))
        if i==0:
            continue
        link = 'https://google.com' + links[i].get('href')
        page = requests.get(link)
        soup = BeautifulSoup(page.content,'html.parser')
        
        #writing content of each page to a text file
        name="paragraph"+str(i)+".txt"
        with open("C:\\Users\\DELL\\Desktop\\Project\\paragraph\\"+name, 'w') as filehandle:
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


 
import nltk
#nltk.download('averaged_perceptron_tagger')
def tagger():  
    for i in range(1,11):
        name="paragraph"+str(i)+".txt"
        file = open("C:\\Users\\DELL\\Desktop\\Project\\paragraph\\"+name,'r')
        words=[]
        query_tagged = []
        while (True):
            query=file.readline()
            if query=="":
                break
            text = nltk.word_tokenize(query)   
            list_tagged =nltk.pos_tag(text)
            #print(list_tagged)
            r=""
            for obj in list_tagged:
                r = r + obj[0] + "_" + obj[1] + " "
                
            query_tagged.append(str)
            
            i=0
            while i<len(list_tagged):
                cur = list_tagged[i][1][0]
                wr = []
                while i<len(list_tagged) and list_tagged[i][1]=="CD":
                    wr.append(list_tagged[i][0])
                    i=i+1
                if i>=len(list_tagged) or list_tagged[i][1][0] not in ('N','J','V'):
                    for j in range(len(wr)):
                        strt = ""
                        for k in range(j,len(wr)):
                            strt = strt + wr[k]
                            #print(strt)
                            words.append(strt)
                            strt = strt + " "
                        i=i+1
                        continue
                else:
                    cur = list_tagged[i][1][0]
                if cur not in ('N','J','V'):
                    i=i+1
                    continue
                while i<len(list_tagged) and (cur == list_tagged[i][1][0] or list_tagged[i][1]=="CD"):
                    wr.append(list_tagged[i][0])
                    i=i+1
                    #print(wr)
                for j in range(len(wr)):
                    strt = ""
                    for k in range(j,len(wr)):
                        strt = strt + wr[k]
                        #print(strt)
                        words.append(strt)
                        strt = strt + " "
                        
        with open('C:\\Users\\DELL\\Desktop\\Project\\New data\\test_extended.txt', 'a') as filehandle:
            for i in words:
                filehandle.write('%s\n' % i)

        with open('C:\\Users\\DELL\\Desktop\\Project\\New data\\test_tagged.txt', 'a') as filehandle:
            for i in query_tagged:
                filehandle.write('%s\n' % i)
       
tagger()

