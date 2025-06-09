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

# f=open('n3.txt', 'wb') 
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)


# 1) open()
# 2) write() / read()
# ii) write() -> write a string to the file
# ii) read() -> read a string from the file
# write -- i) write() -> single line
#              ii) writelines() -> multiple lines

# i)
# f=open('n4.txt', 'a+')
# f.write('Hello, this is a test file.\n')
# f.close()

# ii) error
# f=open('n4.txt', 'a+')
# # f.writelines(['Hello, this is a test file.\n', 'This is the second line.\n'])
# f.writelines('python\n', 'java\n', 'c++\n')
# f.close()

# f=open('n5.txt', 'a+')
# # Writing a single line to the file
# f.writelines(['Hello, this is a test file.', 'This is the second line.'])
# f.close()

# f=open('n6.txt', 'a+')
# data=['python\n', 'java\n', 'c++\n']
# f.writelines(data)
# f.close()


# f=open('n7.txt', 'a+')
# data='''
# n=7
# i=1
# while i<=n:
#     print(i)
#     i=i+1
# '''
# f.writelines(data)
# f.close()

# f=open('n7.txt', 'a+')
# data='''
# n=7
# i=1
# while i<=n:
#     print(i)
#     i=i+1
# '''
# f.write(data)
# f.close()