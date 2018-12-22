
filename = "C:\\Users\\DELL\\Desktop\\Project\\query.txt"
filehandle = open(filename, 'r') 
queries = [] 
while True:      
    line = filehandle.readline()    # read a single line
    if not line:
        break
    if "<title>" in line:           #if "<title>" in line:
        start = 7                   #removing starting <title>
        end = len(line)-9           #removing ending <\title>
        st = line[start:end]
        stm =""
        for i in st:
            if i=="'" or i==",":
                stm=stm+" "
            stm=stm+i
        #print(stm)
        queries.append(stm)
  
with open("C:\\Users\\DELL\\Desktop\\Project\\New data\\query_list.txt",'w') as filehandle:
    for q in queries:
        filehandle.write(q+"\n")

#import nltk      
from nltk.tag.stanford import StanfordPOSTagger
import nltk
import os

java_path = "C:\\Program Files\\Java\\jre1.8.0_181\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path
nltk.internals.config_java("C:/Program Files/Java/jre1.8.0_191/bin/java.exe")
myTagger = StanfordPOSTagger('C:\\Users\\DELL\\Desktop\\Project\\stanford-postagger-2018-10-16\\models\\english-bidirectional-distsim.tagger','C:\\Users\\DELL\\Desktop\\Project\\stanford-postagger-2018-10-16\\stanford-postagger.jar')

#myTagger.tag('What is the airspeed of an unladen swallow ?'.split())
words=[]
query_tagged = []
for query in queries:
    list_tagged = myTagger.tag(query.split())
    print(list_tagged)
    str=""
    for obj in list_tagged:
        str += str + obj[0] + "_" + obj[1] + " "
    
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
                    print(strt)
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
                print(strt)
                words.append(strt)
                strt = strt + " "
            
with open('C:\\Users\\DELL\\Desktop\\Project\\New data\\query_extended.txt', 'w') as filehandle:
    for i in words:
        filehandle.write('%s\n' % i)

with open('C:\\Users\\DELL\\Desktop\\Project\\New data\\query_tagged.txt', 'w') as filehandle:
    for i in query_tagged:
        filehandle.write('%s\n' % i)







