# 1) open()
#      syntex  ->  open('file)

# mode
# x -> Creat
# w -> write
# r -> read
# a -> append




# f=open('n2.txt', 'a') 
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)

# 

# updated mode
# x+ -> Creat
# w+ -> write
# r+ -> read
# a+ -> append

# f=open('n3.txt', 'a+') 
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)



# binary mode
# xb -> Creat
# wb -> write
# rb -> read
# ab -> append

f=open('n3.txt', 'wb') 
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)