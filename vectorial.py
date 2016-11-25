import tokenisation
import re
import operations

#create a dictionary to mark the occurrence of each keyword
dict = {}

#try to apply the innverted index model

titleweight=3
authorweight=2
textweight=1
keywordweight=3

championList=[]
for i in range(0,len(tokenisation.keys)):
    docindex=0
    countline=0
    indextable={}
    tag=""
    word=tokenisation.keys[i]
    cacm=open("cacm/cacm.all","r")
    for line in cacm.readlines():
        countline+=1
        line=line.strip()
        if line.startswith(".I"):
            tag="id"
            docindex+=1
        if line.startswith(".T"):
            tag="title"
        if line.startswith(".A"):
            tag="author"
        if line.startswith(".K"):
            tag="keyword"
        if line.startswith(".W"):
            tag="text"
        if line.startswith(".C"):
            tag=""

        linelist=re.split(' ',line)
        for W in linelist:
            if (word in W) or (word in W.lower()):#in case of match
                if tag=="title":
                    if not docindex in indextable.keys():
                        indextable[docindex]=titleweight
                    else:
                        indextable[docindex]+=titleweight
                if tag=="author":
                    if (tokenisation.focusAuthor):
                        if not docindex in indextable.keys():
                            indextable[docindex]=authorweight*10
                        else:
                            indextable[docindex]+=authorweight*10
                    else:
                        if not docindex in indextable.keys():
                            indextable[docindex]=authorweight
                        else:
                            indextable[docindex]+=authorweight

                if tag=="keyword":
                    if not docindex in indextable.keys():
                        indextable[docindex]=keywordweight
                    else:
                        indextable[docindex]+=keywordweight
                else:
                    if not docindex in indextable.keys():
                        indextable[docindex]=textweight
                    else:
                        indextable[docindex]+=textweight


    dict[word]=indextable
    for index in indextable.keys():
        if indextable[index]>=2:
            if not index in championList:
                championList.append(index)
    cacm.close()


#a little time-consuming (this loop)

print(docindex)
print(championList)

for i in range(0,len(tokenisation.keys)):
    word=tokenisation.keys[i]
    print (word,':',dict[word])


#construct a vectorial model
#construct a vector for each document
#the weight for each term is its occurrence in the doc

dict2={}

for index in range(1,docindex+1):
    vector=[]
    for i in range(0,len(tokenisation.keys)):
        word=tokenisation.keys[i]
        if index in dict[word].keys():
            vector.append(dict[word][index])
        else:
            vector.append(0)
    dict2[index]=vector


#calculate the similarity
queryVector=[]
for value in tokenisation.queryDict.values():
    queryVector.append(value)

print('queryVector: ',queryVector)

dict3={}
for index in dict2.keys():
    vector=dict2[index]
    flag=False
    for i in vector:
        if i>0:
            flag=True
    #verify if the vector is a null vector
    if flag:
        similarity=operations.calculatePseudoAngle(queryVector,vector,queryVector)
        dict3[index]=similarity
    else:
        similarity=0

for index in dict3.keys():
    print(index,':',dict3[index])

#print(dict3[756],dict3[1307],dict3[1502],dict3[2035],dict3[2299],dict3[2399],dict3[2501],dict3[2820])
for index in operations.automaticGetResult(tokenisation.queryindex):
    if index in dict3.keys():
        print(dict3[index])

#try to sort the result list
maxvalue=operations.MaxValue(dict3)
print(maxvalue)
print(operations.keyWithMaxValue(dict3))

docList=[]
threshold=maxvalue/3.8#when the similarity is smaller than a certain value, stop it
#or we can choose the top 20 documents or top 50, just redefine a threshold


while (operations.MaxValue(dict3)>=threshold):
    keyMV=operations.keyWithMaxValue(dict3)
    MV=dict3[keyMV]
    docList.append(keyMV)
    del dict3[keyMV]

print(len(docList),'results:')
print(docList)



