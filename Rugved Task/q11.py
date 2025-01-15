st=input("Enter a string: ")
st=st+" "
l1=[",", ".", "?", ";", "!"]
l2=[".", "?", "!"]
ch=0
wor=0
sen=0
for i in st:
    if i.isalpha():
        ch+=1

for i in range(0, len(st)-1):
    if(((st[i].isalpha) or (st[i] in l1)) and st[i+1]==" "):
        wor+=1


for i in st:
    if i in l2:
        sen+=1
print(ch)
print(wor)
print(sen)
index=0.0588*(100*ch/wor)-0.296*(100*sen/wor)-15.8
print(index)

