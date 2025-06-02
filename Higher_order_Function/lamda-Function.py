# 1 lambda function

# l1=[2,4,6,8]
# l2=[1,2,3,6]
# l3=[5,6,7,8]
# x=map(lambda x,y,z: x+y+z, l1, l2, l3)
# print(list(x))




# Square of elements

# l1=[2,4,6,8]
# x=map(lambda x:x**2,l1)
# print(list(x))




# even no. frome list

# l1=[1,2,3,4,5,6,7,8,9,10]
# x=10
# p=lambda x:["even" if x%2==0 else"odd"]
# print(p(x))



# or
# l1=[1,2,3,4,5,6,7,8,9,10]
# p=filter (lambda x: x%2==0, l1)
# print(list(p))



# odd no. even no

# l1=[1,2,3,4,5,6,7,8,9,10]
# p=map (lambda x:["even" if x%2==0 else"odd"],l1)
# print(list(p))


# max digit
# from functools import reduce 
# l=[1,2,3,4,5,6,7,8,9,4]
# x= reduce (lambda p,q: p if p>q else q ,l)
# print(x)
