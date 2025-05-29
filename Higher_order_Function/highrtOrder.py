# map()
# filter()
# reduce()
# lambda
# decoder()
# genrator()

# 1 map()

# syntex  map(fun-name, iteration1, iteration2. ......)
#         map(fun-name, collection1, collection2. ......)

# ex 
# l=[1,2,3,4,5]
# def sqr(x):
#     return x**2
# x=map(sqr,l) 
# print(x) 
# print(list(x))  

# ṃultiple list
l1=[2,4,6,8]
l2=[1,2,3,6]
l3=[5,6,7,8]
def add(x,y,z):
    return (x+y+z)
p=map(add,l1,l2,l3)
print(list(p))