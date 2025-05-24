l=(1, 2, 3, 4, 5)
l = list(l)  # Convert tuple to list
l[0], l[-1] = l[-1], l[0]
l = tuple(l)  # Convert list back to tuple
print("Swapped tuple:", l)