# range - create collection of similar patterns sequence elements
# Syntex range(start, stop, step/direction)

n=int(input("Enter the number of elements: "))
x = range(1, n+1) # 0 to n-1
print(x) # prints range(1, n+1)
print(list(x)) # prints [1, 2, 3, 4, 5]

x=range(-1, -10)
print(list(x)) # prints [-1, -2, -3, -4, -5, -6, -7, -8, -9]4

x=range(-1, -10, -1) # prints [1, 3, 5, 7, 9]
print(list(x)) # prints [-1, -2, -3, -4, -5, -6, -7, -8, -9]

#Even numbers
x=range(2, 11, 2) # prints [0, 2, 4, 6, 8]
print(list(x)) # prints [2, 4, 6, 8, 10]10

#Odd numbers
x=range(1, 10, 2) # prints [1, 3, 5, 7, 9]
print(list(x)) # prints [1, 3, 5, 7, 9]

x=range(-4, 5, 2) # prints [1, 4, 7]
print(list(x)) # prints [-4, -2, 0, 2, 4, 6, 8]

x=range(-4, 0, 1) # prints [1, 4, 7
print(tuple(x)) # prints [-4, -3, -2, -1]

# to print colection -5 only
x=range(-5, -6, -1) # prints [1, 4, 7]
print(list(x)) # prints []

