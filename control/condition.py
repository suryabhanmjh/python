# if condition
x=10
if x < 5:
    print("x is less than 5")

print("x is greater than or equal to 5")

#or
#y=input("Enter a number: ")
y=False  #or if false
if y:
    print("y is not zero")
print("y is zero")

# if else
#even or odd
z=int(input("Enter a number: "))
if z%2==0:
    print(f'given no {z} is even')
else:
    print(f'given no {z} is odd')

# nested if
a=10
b=20
c=30
if (a>b and a>c):
    print(f'{a} is greater than {b} and {c}')   
elif (b>a and b>c):
    print(f'{b} is greater than {a} and {c}')
else:
    print(f'{c} is greater than {a} and {b}')

# line of block repeated sequentially
# to avoide sequentially repeated of code block of code we use iteration/looping statements
# for loop
# while loop


#up to n natural no.
e=int(input("Enter a number: "))
# natural no. is 1 to n
for i in range(1,e+1):
    print(i)
