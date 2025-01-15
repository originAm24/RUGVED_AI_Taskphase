#Luhn's Algorithm
a=4539704354786391
sum=0
for i in range(1, 17):
    d=a%10
    if i%2==0:
        d=2*d
    if d>=10:
        sum=sum+(d//10)+(d%10)
    else:
        sum=sum+d
    a=a//10

if sum%10==0:
    print("valid")
else:
    print("invalid")        
    
