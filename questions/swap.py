n=12345
n = str(n)  # Convert the number to a string for easy manipulation
n = list(n)
n[0], n[-1] = n[-1], n[0]
n = ''.join(n)
print("Swapped number:", n)

