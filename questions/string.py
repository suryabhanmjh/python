s='python'
l=list(s)  # Convert string to list
l[0], l[-1] = l[-1], l[0]  # Swap first and last characters
print(l)
s = ''.join(l)  # Convert list back to string
print("Swapped string:", s)