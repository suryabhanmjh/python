

# for i in range(5):
#     for j in range(1, 6):
#         print(j, end=' ')
#     print()

# n=int(input("Enter a number: "))
# i=1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(j, end=' ')
#     print()  # Move to the next line after printing each row
n=int(input("Enter a number: "))
for i in range(n):
        x='A'
        for j in range(0,n):
            print(chr(ord(x)+j), end=' ')
        print()  # Move to the next line after printing each row
           