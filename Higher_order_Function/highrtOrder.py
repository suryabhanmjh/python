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
l=[1,2,3,4,5]
def sqr(x):
    return x**2
x=map(sqr,l) 
print(x) 
print(list(x))  