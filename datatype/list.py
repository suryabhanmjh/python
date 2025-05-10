l=[10,20,30, 'python', 40, 50]
print(l) # prints [10, 20, 30, 'python', 40, 50]
print(type(l)) # prints <class 'list'>

l1=[10,20,30, 40, 50]
print(max(l1)) # prints [10, 20, 30, 40, 50]
print(min(l1)) # prints [10, 20, 30, 40, 50]
print(sum(l1)) # prints 150
print(len(l1)) # prints 5


l2=['python', 'java', 'c', 'c++']
print(max(l2)) # prints python
print(min(l2)) # prints c
#print(sum(l2)) # prints TypeError: sum() can't sum strings
print(len(l2)) # prints 4


#methods
#1 copy() # returns a shallow copy of the list
#2 count() # returns the number of occurrences of a value in the list
#3 extend() # extends the list by appending elements from the iterable
#4 insert() # inserts an element at a given position
#5 pop() # removes and returns an element at a given position
#6 remove() # removes the first occurrence of a value from the list
#7 reverse() # reverses the elements of the list in place
#8  sort() # sorts the elements of the list in place
#9 index() # returns the index of the first occurrence of a value in the list
#10 clear() # removes all elements from the list
#11 append() # adds an element to the end of the list


# append() - adds an element to the end of the list
m=[10,20,20,20,30,40,'python']
m.append('java') # adds 'java' to the end of the list
print(m) # prints [10, 20, 30, 40, 'python', 'java']
m.append([50,60]) # adds 50 to the end of the list
print(m) # prints [10, 20, 30, 40, 'python', 'java', 50]


# extend() - extends the list by appending elements from the iterable
m.extend(['php','c++']) # adds 50 to the end of the list
print(m) # prints [10, 20, 30, 40, 'python', 'java', 50, 'php', 'c++']
m.extend('java') # adds 50 to the end of the list
print(m)

#insert() - inserts an element at a given position
m.insert(2, 'java') # inserts 'java' at index 2
print(m) # prints [10, 20, 'java', 30, 40, 'python', 'java', 50, 'php', 'c++']

#pop
m.pop()
print(m) # prints [10, 20, 'java', 30, 40, 'python', 'java', 50, 'php']

m.remove('java') # removes the first occurrence of 'java' from the list
print(m) # prints [10, 20, 30, 40, 'python', 'java', 50, 'php']

print(m.index('java')) # prints 5
print(m.count(20)) # prints 1
