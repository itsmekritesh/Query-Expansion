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
#sorting in reverse        
word_dict1=sorted(word_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) 
#print(sorted(word_dict.items(), key = lambda kv:(kv[1], kv[0])))       
file1=open("C:\\Users\\Kritesh\\Desktop\\Project\\paragraph tagged\\word_dict.txt","w")
for obj in range(len(word_dict1)):
    file1.write(str(word_dict1[obj][0])+str(word_dict1[obj][1])+"\n")
    
        