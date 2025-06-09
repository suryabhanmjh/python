# read()
# 1) read() -> all data  read in character form
# 2) read(n) -> read n characters from the file
# 3) readline() -> read the file line by line
# 4) readlines() -> read all lines into a list

# f=open('n7.txt', 'r+')
# # data=f.read()  # Read all data from the file
# # data=f.read(10)
# # data=f.readline()  # Read the first line from the file
# # data=f.readlines()  # Read all lines into a list
# print(data)

# f=open('n7.txt', 'r+')
# data1=f.read(5)  # Read 5 characters from the file
# data2=f.read(10)  # Read the next 10 characters from the file
# print(data1)
# print(data2)


# f=open('n7.txt', 'r+')
# f.write('Hello, this is a test file.\n')
# f.close()

f=open('n7.txt', 'r+')
f.readline()  # Read the first line from the file
f.write('Hello, this is a test file.\n')
f.close()