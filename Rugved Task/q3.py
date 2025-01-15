num=int(input("Enter a number"))
num1=num
lst=[]
while num1>0:
    dig=num1%10
    lst.append(dig)
    num1=num1//10
flag=True
if lst[len(lst)-1]!=lst[0]:
    flag=False
for i in range(0, len(lst)-1):
    if lst[i+1]<lst[i]:
        break
for j in range(i+1, len(lst)-1):
    if lst[j+1]>lst[j]:
        flag=False
print(flag)
