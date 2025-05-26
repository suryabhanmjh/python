# write one call multiple 
# to acive code reusebility
# avoide sequential code or # repetitive code
# syntex

# def function_name(parameters):
    #  operations

# def add(a, b):
#     """This function adds two numbers."""
#     return a + b

# def subtract(a, b):
#     """This function subtracts two numbers."""
#     return a - b

# def multiply(a, b):
#     """This function multiplies two numbers."""
#     return a * b

# def divide(a, b):
#     """This function divides two numbers."""
#     if b != 0:
#         return a / b
#     else:
#         return "Division by zero error"

    
    #  calling the functions
    #  function_name(arguments)

# required
#       def
#       function_name
#      ()
#      :

# operations
#       parameters
#       arguments
#      return
# 


# def first():
#     pass
# first()
# print(first())

# def first():
#     return "Hello, World!"
# first()
# print(first())

# Even numbers

# def even_num(n):
#     for i in range(1, n + 1):
#         if i < n:
#             print(2*i, end=',')
#         else:
#             print(2*i, end=' ')   

# print("Hello") 
# even_num(int(input("Enter a number: ")))
# print("\nGoodbye")
# even_num(int(input("Enter a number: ")))

# Odd numbers
# def odd_num(n):
#     for i in range(1, n + 1):
#         if i < n:
#             print(2*i - 1, end=',')
#         else:
#             print(2*i - 1, end=' ')
# print("Hello")
# odd_num(int(input("Enter a number: ")))            

# factorial
# def factorial(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     print(f'Factorial: {n} is {factorial}')
# print("Hello")
# factorial(int(input("Enter a number: ")))
# print("\nGoodbye")

# or

def factorial(n):
    factorial = 1
    for i in range(5, 0, -1):
        factorial *= i
        if i > 1:
            print(f'{i} * ', end='')
        else:
            print(f'{i} = ', end='')   
    print(factorial)
print("Hello")
factorial(int(input("Enter a number: ")))
print("\nGoodbye")