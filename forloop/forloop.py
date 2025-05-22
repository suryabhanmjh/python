# finite iteration

# l=[1,2,3,4,5]
# l1=[]
# for i in l:
#     l1.append(i**2)
#     print(l1)
# print(l1)    

# string

# s="hello"
# for i in s:
#     print(i)



# x=a='a'
# print(ord('a'))
# print(ord('a')+4)
# print(chr(ord('a')+4))

# print abcde to efghi 
# s='abcde'
# for i in s:
#     print(chr(ord(i)+4),end='')

# print like this ['e', 'f', 'g', 'h', 'i']

s='abcde'
s1=''
for i in s:
    s1=''.join((s1,chr(ord(i)+4)))
print(s1)    