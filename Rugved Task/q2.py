st=input("Enter a string: ")
lst=[]
myDict={}
str1=""
for i in st:
    lst.append(i)
lst.sort()
for i in lst:
    str1=str1+i
for i in lst:
    if i not in myDict.keys():
        myDict[i]=1
    else:
        myDict[i]=myDict[i]+1
    
print(str1)
print(myDict)

    