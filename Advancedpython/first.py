#>..................................................................Generator...........................................
#generator ke andar yeild keyword ka use krty he 

#return funvtion termiate kr deta he 
#yeild next task perform krne ke liye use kr  sktye he 

#benefits of memory utilization

def even_no(n):
    i=2
    while i<=n:
        yield i
        i=i+2
n=int(input("enter the num"))
x=even_no(n)
print(next(x))



