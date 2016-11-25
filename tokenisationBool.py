import re
import operations

query=input("enter a query\n")

print ("your query is: ",query)

list=re.split(' ', query)
print (list)

#how to handle hyphens? sometimes split words with hyphens for example ten-year-old, sometimes not, for example co-education
list1=[]
for word in list:
    l=re.split('-',word)
    for w in l:
        list1.append(w)
list=list1

list=operations.deleteLY(list)

list=operations.deleteING(list)

list=operations.deleteED(list)

list=operations.removePlurial(list)

list=operations.deleteCommonSuffix(list)

list=operations.removePlurial(list)

#normalize by changing into lowercases
for i in range(0,len(list)):
    if not (list[i]=='AND' or list[i]=='OR' or list[i]=='NOT'):
        if not ((list[i].isupper()) and (len(list[i])>=3)): #if all of the letters of the term are in upper case and the length >=3, change it into lower case
            list[i]=list[i].lower()


print(list)

