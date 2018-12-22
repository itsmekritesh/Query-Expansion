import nltk

file = open("C:\\Users\\DELL\\Desktop\\Project\\paragraph tagged\\paragraph1.txt",'r')
words=[]
query_tagged = []
while (True):
    query=file.readline()
    if query=="":
        break
    text = nltk.word_tokenize(query)   
    list_tagged =nltk.pos_tag(text)
    print(list_tagged)
    str=""
    for obj in list_tagged:
        str = str + obj[0] + "_" + obj[1] + " "
    
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
            
with open('C:\\Users\\DELL\\Desktop\\Project\\New data\\test_extended.txt', 'w') as filehandle:
    for i in words:
        filehandle.write('%s\n' % i)

with open('C:\\Users\\DELL\\Desktop\\Project\\New data\\test_tagged.txt', 'w') as filehandle:
    for i in query_tagged:
        filehandle.write('%s\n' % i)