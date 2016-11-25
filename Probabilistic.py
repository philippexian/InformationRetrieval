import re
import tokenisation
import operations
import math

#we prefer a binary probabilistic model
#calculate the conditional probability using the cacm as a training set
#the criteria for ranking, RSVd=sum(log(pt/(1-pt))+log((1-ut)/ut))=sum(ct)
#ct=log((s/(S-s))/((dft-s)/((N-dft)-(S-s))))
#smoothing: ct=log(((s+0.5)/(S-s+0.5))/((dft-s+0.5)/((N-dft)-(S-s)+0.5)))

realList=operations.automaticGetResult(tokenisation.queryindex)
print(realList)

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

N=docindex
S=len(realList)
logOddRatio={}
for term in dict.keys():
    dft=len(dict[term])#amount of docs containing term t
    s=len(operations.intersect(dict[term],realList))#amount of docs where the term occurs and relevant
    ct=math.log(((s+0.5)/(S-s+0.5))/((dft-s+0.5)/((N-dft)-(S-s)+0.5)))
    logOddRatio[term]=ct

for term in logOddRatio:
    print(term,':',logOddRatio[term])

dict2={}
for i in range(1,docindex+1):
    #first create a list of terms in the query that the doc contains
    termList=[]
    for term in dict.keys():
        if i in dict[term]:
            termList.append(term)
    dict2[i]=termList


dict3={}
for i in dict2.keys():
    RSVd=0
    for term in dict2[i]:
        RSVd+=logOddRatio[term]
    dict3[i]=RSVd

for i in dict3.keys():
    print(i,':',dict3[i])

#try to sort the result list
maxvalue=operations.MaxValue(dict3)
print(maxvalue)
print(operations.keyWithMaxValue(dict3))

docList=[]
threshold=maxvalue/2.3#when the ranking value is smaller than a certain value, stop it
#or we can choose the top 20 documents or top 50, just redefine a threshold

while (operations.MaxValue(dict3)>=threshold):
    keyMV=operations.keyWithMaxValue(dict3)
    MV=dict3[keyMV]
    docList.append(keyMV)
    del dict3[keyMV]

print(len(docList), 'results:')
print(docList)

#a question is the training set is cacm and the testing set is cacm too