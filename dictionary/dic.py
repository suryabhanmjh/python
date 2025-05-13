# dictionary.py
# collection of key-value pairs
# keys are unique
# values can be duplicate
# representation through {} with comma separated key-value pairs
# indexing not supported
# slicing not supported
# mutable in nature

d={
    2:'python',
    1:34,
    3:'B.E',
    
}

print(len(d)) # prints 7
print(max(d)) # prints 34
print(min(d)) # prints 'B.E'
print(sum(d)) # prints TypeError: sum() of dictionary is not supported
print(type(d)) # prints <class 'dict'>
print(id)

e={ 2:'python', 2:37, '3':'B.E'} # prints {2: 37, '3': 'B.E'} over loading
print(e) # prints {2: 37, '3': 'B.E'}
print(sum(e)) # prints TypeError: sum() of dictionary is not supported
print(max(e)) # prints 37
print(min(e)) # prints 'B.E'   
print(len(e)) # prints 2
print(type(e)) # prints <class 'dict'>  