import re
import operations


commonwords=[]
cacm=open("cacm/common_words","r")
for line in cacm.readlines():
    line=re.split('\n',line)
    commonwords+=(line)
for word in commonwords:
    if word=='':
        commonwords.remove(word)

print (commonwords)

cacm.close()

#take a series of words as the query
#query=input("enter a query\n")
queryindex=5
query=operations.automaticGetQuery(queryindex)
print ("your query is: ",query)

#and consider the keywords and authors


#split it into a list of single words

list=re.split(' ', query)
print (list)

#how to handle hyphens? sometimes split words with hyphens for example ten-year-old, sometimes not, for example co-education
list1=[]
for word in list:
    l=re.split('-',word)
    for w in l:
        list1.append(w)
list=list1



#remove the common words

#why can't we remove all common words in one cycle?
#because when removing a world, the next word's index-1, you skip it by index++

#some sentences are formed totally by common words but they do have meanings
#to be or not to be, let it be

def check_commonword(list, commonwords):
    flag=False
    for word in list:
        if word in commonwords:
            flag=True
    return flag


punctuation=[',','.','?','!','-','(',')','/','<','>','[',']','{','}',' ',';']
for word in list:
    if word in punctuation:
        list.remove(word)


list=operations.deleteSigns(punctuation,list)
if '' in list:
    list.remove('')

print(list)


#think of normalizing the tokens
#delete some suffixes

list=operations.deleteLY(list)

list=operations.deleteING(list)

list=operations.deleteED(list)

list=operations.removePlurial(list)

list=operations.deleteCommonSuffix(list)

list=operations.removePlurial(list)


#normalize by changing into lowercases
for i in range(0,len(list)):
    if not ((list[i].isupper()) and (len(list[i])>=3)):
        list[i]=list[i].lower()

print(list)

while(check_commonword(list, commonwords)==True):
    for word in list:
        if word in commonwords :
            list.remove(word)

spwordlist1=['write','writing','written','draft','script']
focusAuthor=False
markIndex=0
for i in range(0,len(list)):
    for W in spwordlist1:
        if list[i] in W:
            focusAuthor=True
            markIndex=i


print(list)


#some suffixes like tion, ness, ment, i don't know if i should remove them

#when removing a redundant word, we should add to its occurrence
#we assume that the word's weight is its occurrence in the query

queryDict={}

for i in range(0,len(list)):
    if list[i].isupper():
        if not list[i] in queryDict.keys():
            queryDict[list[i]]=5
        else:
            queryDict[list[i]]+=5
    else:
        if not list[i] in queryDict.keys():
            queryDict[list[i]]=1
        else:
            queryDict[list[i]]+=1

if focusAuthor:
    for j in range(markIndex+1,len(list)):
        queryDict[list[j]]+=10


print(queryDict)


keys=[]
for word in queryDict.keys():
    keys.append(word)

print(keys)