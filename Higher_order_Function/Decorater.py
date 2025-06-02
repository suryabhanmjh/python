# def decor(x):
#     def inner_function():
#         p=x
#         return p
#     return inner_function
# x=decor(10)    
# z=x()
# print(z)


# def decor(x):
#     def inner_function(r,s):
#         r=r+5
#         s=s+5
#         p=x(r,s)
#         return p
#     return inner_function
# def add(x,y):
#     return x+y
# x=decor(add)
# z=x(10,5)
# print(z)

# oe
def decor(x):
    def inner_function(r,s):
        r=r+5
        s=s+5
        p=x(r,s)
        return p
    return inner_function
@decor
def add(x,y):
    return x+y
z=add(5,10)
print(z)