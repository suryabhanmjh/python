# swap the numbers input= 12345 output= 52341
l=[1, 2, 3, 4, 5]
l[0], l[-1] = l[-1], l[0]
print("Swapped list:", l)