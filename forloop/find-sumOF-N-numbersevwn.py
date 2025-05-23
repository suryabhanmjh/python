n=int(input("Enter the number to sum: "))
sum=0
for i in range(1,n+1,1):
    sum+=2*i
    if i<=n-2:
        print(2*i,end='+')
    else:
        print(2*i,end='=')    
print("The sum is:",sum)



# or

n=int(input("Enter the number to sum: "))
sum=0
for i in range(2,(2*n+1),2):
    sum+=i
    if i<2*n:
        print(i,end='+')
    else:
        print(i,end='=')    
print("The sum is:",sum)
