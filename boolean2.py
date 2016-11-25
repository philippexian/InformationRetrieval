import tokenisationBool
import re
import operations

dict={}

for i in range(0,len(tokenisationBool.list)):
    docindex=0
    countline=0
    indexlist=[]
    word=tokenisationBool.list[i]
    if not (word=='AND' or word=='OR' or word=='NOT'):
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

def operationsInBracket(list):
    return list

#fail to treat the case where there are brackets
resultList=[]
cursor=0

#use a cursor to jump to the next logic sign "AND", "OR" and "NOT"
while(cursor<len(tokenisationBool.list)):
    resultList1=resultList#left=result of last step
    resultList2=[]
    if tokenisationBool.list[cursor]=='AND':
        if tokenisationBool.list[cursor+1]=='NOT':
            resultList2=operations.complementary(dict[tokenisationBool.list[cursor+2]],docindex)
            cursor+=3
        else:
            resultList2=dict[tokenisationBool.list[cursor+1]]
            cursor+=2
        resultList=operations.intersect(resultList1, resultList2)
    elif tokenisationBool.list[cursor]=='OR':
        if tokenisationBool.list[cursor+1]=='NOT':
            resultList2=operations.complementary(dict[tokenisationBool.list[cursor+2]],docindex)
            cursor+=3
        else:
            resultList2=dict[tokenisationBool.list[cursor+1]]
            cursor+=2
        resultList=operations.union(resultList1, resultList2)
    elif tokenisationBool.list[cursor]=='NOT':
        resultList=operations.complementary(dict[tokenisationBool.list[cursor+1]], docindex)
        cursor+=2
    else:
        resultList=dict[tokenisationBool.list[cursor]]
        cursor+=1

print(cursor)
print(resultList)


