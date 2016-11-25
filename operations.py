import math

#intersection

def intersect(L1,L2):
    L=[]
    for i in L1:
        for j in L2:
            if i==j:
                L.append(i)
    selectsort(L)
    return L

def union(L1,L2):
    L=L1
    for i in L2:
        if not i in L:
            L.append(i)
    selectsort(L)
    return L

def complementary(L1, length):
    L=[]
    for i in range(1, length+1):
        if i not in L1:
            L.append(i)
    return L

def selectsort(L):
    if len(L)==1:
        return L
    else:
        for i in range(0,len(L)):
            for j in range(i+1,len(L)):
                if L[i]>L[j]:
                    temp=L[i]
                    L[i]=L[j]
                    L[j]=temp

        return L




import re

#remove the punctuations in the words
def deleteSigns(signcollection,list):
    for sign in signcollection:
        for idword in range(0,len(list)):
            if list[idword].endswith(sign):
                list[idword]=list[idword][:-1]
            if list[idword].startswith(sign):
                list[idword]=list[idword][1:]
    return list


vowel=['a','e','u','i','o']

#remove 's' at the end of a noun or a verb
def removePlurial(list):
    for idWord in range(0,len(list)):
        thisWord=list[idWord];
        if thisWord.endswith('s'):
            if thisWord.endswith('ss'):
                continue
            if thisWord.endswith('es'):
                if thisWord.endswith('ies'):
                    thisWord=thisWord[:-3]#remove last 3 letters
                else:
                    thisWord=thisWord[:-2]#for words ending with e, just remove the plurial s
            else:
                thisWord=thisWord[:-1]
        if thisWord.endswith('y'):
            if not thisWord[-2] in vowel:
                thisWord=thisWord[:-1]
        if thisWord.endswith('e'):
            if len(thisWord)>=5:#issue for example
                thisWord=thisWord[:-1]
        list[idWord]=thisWord
    return list

def deleteING(list):
    for idWord in range(0,len(list)):
        thisWord=list[idWord];
        if thisWord.endswith('ing'):
            thisWord=thisWord[:-3]
        list[idWord]=thisWord
    return list

def deleteED(list):
    for idWord in range(0,len(list)):
        thisWord=list[idWord];
        if thisWord.endswith('ed'):
            thisWord=thisWord[:-2]
        list[idWord]=thisWord
    return list

def deleteLY(list):
    for idWord in range(0,len(list)):
        thisWord=list[idWord];
        if thisWord.endswith('ly'):
            thisWord=thisWord[:-2]
        list[idWord]=thisWord
    return list


commonSuffix=['tion','ment','ness','sion']

def deleteCommonSuffix(list):
    for idWord in range(0,len(list)):
        thisWord=list[idWord];
        for suffix in commonSuffix:
            if thisWord.endswith(suffix):
                thisWord=thisWord[:-4]
        list[idWord]=thisWord
    return list

#print(deleteCommonSuffix(['description','implementation']))

def calculateDotProduct(L1,L2):
    if not len(L1)==len(L2):
        raise "not in same dimension"
    try:
        sumDotProduct=0
        for i in range(0,len(L1)):
            sumDotProduct+=L1[i]*L2[i]
        return sumDotProduct
    except "not in same dimension":
        print("Error: the two vectors are not in the same dimension")

def calculateModule(L):
    sumModule=0
    for i in range(0,len(L)):
        sumModule+=L[i]**2
    Module=math.sqrt(sumModule)
    return Module

def calculateAngle(L1,L2):
    return calculateDotProduct(L1,L2)/(calculateModule(L1)*calculateModule(L2))

def calculatePseudoAngle(L1,L2,L3):
    return calculateDotProduct(L1,L2)/calculateModule(L3)

def keyWithMaxValue(dict):
    keyMV=0
    MV=0
    for index in dict.keys():
        if dict[index]>MV:
            keyMV=index
            MV=dict[index]
    return keyMV

def MaxValue(dict):
    keyMV=0
    MV=0
    for index in dict.keys():
        if dict[index]>MV:
            keyMV=index
            MV=dict[index]
    return MV



def automaticGetQuery(i):
    queryset=open("cacm/query.text","r")
    flag1=False
    flag2=False
    query=""
    counter=0
    for line in queryset.readlines():
        line=line.strip()
        if line==".I "+str(i):
            flag1=True
        if line==".I "+str(i+1):
            flag1=False
        if line.startswith(".W"):
            flag2=True
        if line.startswith(".A") or line.startswith(".N"):
            flag2=False
        if (flag1 and flag2):
            query+=(line+" ")
            counter+=1
    query=query[3:]
    query=query[:-1]
    queryset.close()
    return query

#print(automaticGetQuery(5))


def automaticGetResult(i):
    resultset=open("cacm/qrels.text","r")
    resultlist=[]
    flag=False
    for line in resultset.readlines():
        line=line.strip()
        if i<10:
            if line.startswith(str(0)+str(i)):
                flag=True
            else:
                flag=False
        else:
            if line.startswith(str(i)):
                flag=True
            else:
                flag=False
        if flag:
            linelist=re.split(' ',line)
            resultlist.append(int(linelist[1]))
    return resultlist

#print(automaticGetResult(1))


