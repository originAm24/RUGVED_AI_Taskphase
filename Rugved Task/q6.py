st=input("Enter a string: ")
st1=input("Enter another string: ")
st3=""
st4=""
lst=[]
lst1=[]
check=True
for i in st:
    if i!=" ":
        lst.append(i)
for i in st1:
    if i!=" ":
        lst1.append(i)
if len(lst)!=len(lst1):
    check=False


for i in lst:
    if i not in lst1:
        check=False



print(check)
