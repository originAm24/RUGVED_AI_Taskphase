#Caesar's Cipher
ststr="abcdefghijklmnopqrstuvwxyz "
st="hello world$"
n=int(input("By how much do you want to shift?: "))
if n>26:
    n=n-26

for i in st:
    a=list(ststr).index(i)
    if (a+n>25):
        a=a-25
    print(ststr[a+n], end="")

    
