a=0
b=1
n=int(input("Enter n values"))
print(a, "", b, end=" ")
for i in range(0, n-2):
    temp=b
    b=a+b
    a=temp
    print(b, end=" ")
#0 1 1 2 3 5 8 
#a b

    