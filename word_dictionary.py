file=open("C:\\Users\\Kritesh\\Desktop\\Project\\paragraph tagged\\test_extended.txt","r")
word_dict={}
while (True):
    key=file.readline()
    if not key:
        break
    if key in word_dict:
        word_dict[key]+=1
    else:
        word_dict[key]=1
print (word_dict)        
file1=open("C:\\Users\\Kritesh\\Desktop\\Project\\paragraph tagged\\word_dict.txt","w")
for obj in word_dict:
    file1.write(obj+str(word_dict[obj])+"\n")
    
        