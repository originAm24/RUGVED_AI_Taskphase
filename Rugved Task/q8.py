st=input("Enter the string: ")
n=int(input("Enter number of characters: "))
st1=""
flag=True
if len(st)%n!=0:
    print("Invalid")
    exit(0)
lst=[]
for i in range(0, len(st), n):
    st1=""
    for j in range(i, n+i):
        st1=st1+st[j]
    lst.append(st1)
for i in lst:
    if i not in lst:
        flag=False
if flag==False:
    print("Invalid")
    exit(0)
else:
    for i in lst:
        print(i, end=" ")




