while True:
    print("1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Off")
    n = int(input("Enter the operation num: "))

    if n == 5:
        print("Calculator turned off.")
        break  

    if n in (1, 2, 3, 4):
        num1 = eval(input("Enter first number: "))
        num2 = eval(input("Enter second number: "))

        if n == 1:
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif n == 2:
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif n == 3:
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif n == 4:
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Cannot divide by 0.")
    else:
        print("Invalid input. Please select from 1 to 5.")

