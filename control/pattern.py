# pattern matching 
# 1

# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print('*'*i)     or '*'*i+' '*(n-i)
#     i+=1



# 2
 
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1

# 3
 
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1


# 4
# n= int(input("Enter a number: "))
# i=0
# while i<n:
#     print('*'*(n-i)+' '*i)
#     i+=1

# 5
# n= int(input("Enter a number: "))
# i=0
# while i<n:
#     print(' '*i+'*'*(n-i))
#     i+=1

# 6
# n= int(input("Enter a number: "))
# i=0
# while i<n:
#     print(' '*i+'* '*(n-i))
#     i+=1


#7
# n= int(input("Enter a number: "))
# i=0
# while i<n:
#     print(' '*i+'* '*(n-i))
#     i+=1
# i=i-2
# while i>=0:
#     print(' '*i+'* '*(n-i))
#     i-=1

#8
# n=int(input("Enter a number: "))
# i=0
# while i<n:
#     print('* '*(n-i))
#     i+=1
# i=i-2
# while i>=0:
#      print('* '*(n-i))
#      i-=1    

# 9
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1
# i=i-2
# while i>0:
#     print(' '*(n-i)+'* '*i)
#     i-=1    



# Armstrong number
#find length of number 1st method

# n=int(input("Enter a number: "))
# x=str(n)
# print(len(x))

#find length of number 2nd method
# n=int(input("Enter a number: "))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(f'total digits is {count} in given number {n}')

# add the last digit of number
# n=int(input("Enter a number: "))
# x=n
# sum=0
# while n>0:
#     last_digit=n%10
#     sum+=last_digit
#     n=n//10
# print(f'sum of digits is {sum} in given number {x}')

# check the number is armstrong or not
# n=int(input("Enter a number: "))
# digit=0
# sum=0
# x=y=n
# while n>0:
#     digit+=1
#     n=n//10
# while x>0:
#     last_digit=x%10
#     sum+=last_digit**digit
#     x=x//10
# if sum==y:
#     print(f'{y} is an Armstrong number')
# else:
#     print(f'{y} is not an Armstrong number')


# check tne number is palindrome or not
# n=input("Enter a number: ")
# if n==n[::-1]:
#     print(f'{n} is a palindrome number')
# else:
#     print(f'{n} is not a palindrome number')    

# second method
# n=int(input("Enter a number: ")) 
# rev=0
# x=n
# while n>0:
#     last_digit=n%10
#     rev=rev*10+last_digit
#     n=n//10
# if rev==x:
#     print(f'{x} is a palindrome number')
# else:
#     print(f'{x} is not a palindrome number')


# conventional method to check palindrome in srting not use slicing

s=input("Enter a string: ")
palindrome=True
l=int(len(s)/2)
i,j=0,-1

while l>0:
    if s[i]==s[j]:
        pass
    else:
        palindrome=False
        break
    i+=1
    j-=1
    l-=1
if palindrome:
    print(f'{s} is a palindrome string')
else:
    print(f'{s} is not a palindrome string')