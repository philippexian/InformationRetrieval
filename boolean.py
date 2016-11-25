import re
import tokenisation
import operations

#create a dictionary to show if the query term occurs in the document
#for each term in the query token list (after treatment), the list of documents containing it

dict={}

for i in range(0,len(tokenisation.keys)):
    docindex=0
    countline=0
    indexlist=[]
    word=tokenisation.keys[i]
    cacm=open("cacm/cacm.all","r")
    for line in cacm.readlines():
        countline+=1
        line=line.strip()
        if line.startswith(".I"):
            docindex+=1
        linelist=re.split(' ',line)
        for W in linelist:
            if (word in W) or (word in W.lower()):#in case of match
                if not docindex in indexlist:
                    indexlist.append(docindex)

    dict[word]=indexlist
    cacm.close()

for word in dict.keys():
    print(word,':',dict[word])


#the number of query tokens that occur in each document
dict2={}
for i in range(1,docindex+1):
    dict2[i]=0
    for word in dict.keys():
        if i in dict[word]:
            dict2[i]+=1

#print(dict2)

maxvalue=operations.MaxValue(dict2)
print(maxvalue)
print(operations.keyWithMaxValue(dict2))

docList=[]
threshold=maxvalue/1.5#when the value is smaller than a certain value, stop it
#or we can choose the top 20 documents or top 50, just redefine a threshold

while (operations.MaxValue(dict2)>=threshold):
    keyMV=operations.keyWithMaxValue(dict2)
    MV=dict2[keyMV]
    docList.append(keyMV)
    del dict2[keyMV]

print(len(docList), 'results:')
print(docList)





