n=int(input("Enter the number to sum: "))
sum=0
for i in range(1,n+1,2):
    sum+=i
    if i<=n-2:
        print(i,end='+')
    else:
        print(i,end='=')    
print("The sum is:",sum)