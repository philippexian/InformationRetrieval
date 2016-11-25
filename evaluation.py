import operations
import tokenisation


realList=operations.automaticGetResult(tokenisation.queryindex)
print(realList)

str = input("which model to choose?")
if str=="boolean":
    import boolean
    resultList=boolean.docList
    intersectList=operations.intersect(realList,resultList)
    print(intersectList)
if str=="boolean2":
    import boolean2
    resultList=boolean2.resultList
    intersectList=operations.intersect(realList,resultList)
    print(intersectList)
if str=="vectorial":
    import vectorial
    resultList=vectorial.docList
    intersectList=operations.intersect(realList,resultList)
    print(intersectList)
if str=="probabilistic":
    import Probabilistic
    resultList=Probabilistic.docList
    intersectList=operations.intersect(realList,resultList)
    print(intersectList)
else:
    print("the retrieval model is not found")

#or we can use 2 or 3 models in combination to increase the recall rate
#but the precision will increase? decrease? not sure

recall=len(intersectList)/len(realList)
precision=len(intersectList)/len(resultList)

print(recall)
print(precision)
#the two last parameters are respectively the recall and precision

