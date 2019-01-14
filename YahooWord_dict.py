from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
#nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

file=open("C:\\Users\\kritesh\\Desktop\\Project\\Yahoo\\paragraph tagged\\test_extended.txt","r")
word_dict={}
while (True):
    key=file.readline()
    if not key:
        break
    word=word_tokenize(key)
    if word[0] in stop_words:
        continue
    if key in word_dict:
        word_dict[key]+=1
    else:
        word_dict[key]=1
        
#sorting in reverse        
word_dict1=sorted(word_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) 

#print (word_dict)        
file1=open("C:\\Users\\kritesh\\Desktop\\Project\\Yahoo\\paragraph tagged\\word_dict.txt","w")
for obj in word_dict1:
    file1.write(obj[0]+str(obj[1])+"\n")
    
        
