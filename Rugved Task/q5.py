def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    
    return n*fact(n-1)
num=int(input("enter a number"))
print(fact(5))
