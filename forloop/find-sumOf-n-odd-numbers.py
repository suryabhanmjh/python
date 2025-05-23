n=int(input("Enter the number to sum: "))
sum=0
for i in range(1,n+1):
    sum+=2*i-1
    if i<=n:
        print(2*i-1,end='+')
    else:
        print(2*i-1,end='=')    
print("The sum is:",sum)



# or

n=int(input("Enter the number to sum: "))
sum=0
for i in range(1,(2*n-1+1),2):
    sum+=i
    if i<2*n-1:
        print(i,end='+')
    else:
        print(i,end='=')    
print("The sum is:",sum)
