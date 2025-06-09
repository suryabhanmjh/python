# cursor 
# 1 tell() -> get the current position of the cursor
# 2 seek() -> move the cursor to a specific position in the file 
#         0 from the beginning of the file
#         1 from the current position of the file
#         2 from the end of the file

f=open('n7.txt', 'r+')
print(f.tell())  # Get the current position of the cursor
f.read(5)
# print(f.tell())  # Get the current position of the cursor after reading 5 characters
f.seek(0)  # Move the cursor back to the beginning of the file
print(f.tell())  # Get the current position of the cursor after seeking to the beginning