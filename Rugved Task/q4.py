lst=[3, 4, 5, 7, 1, 5, 6, 9]
for i in range(0, len(lst)):
    min=lst[i]
    minindex=-1
    for j in range(i, len(lst)):
        if lst[j]<min:
            min=lst[j]
            minindex=j

    temp=lst[i]
    lst[i]=min
    lst[minindex]=temp


print(lst)
    
        
