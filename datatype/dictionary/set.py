# set () 
# unordered collection of unique elements
# representation through {} with comma (,) separated values 
# indexing not supported
# slicing not supported
# mutable in nature
#example
set1={1,2,3,4,'a','b','c'}
print(set1) # prints {1, 2, 3, 4, 'a', 'b', 'c'}
print(id(set1)) # prints the memory address of the set



# methods for set
print(len(set1)) # prints 7 replace duplicate with unique
# print(max(set1)) # prints 4
# print(min(set1)) # prints 1
print(type(set1)) # prints <class 'set'>
# print(sum(set1)) # prints TypeError: sum() of set is not supported


# In-built methods
s={1,2,3,4,'a','b','c'}
s.add(5) # adds 5 to the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5}

s.update([6,7,8]) # adds 6, 7, 8 to the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8}

s.update((9,10,'vicky'), 'python') # adds 9, 10, 'vicky' to the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10, 'vicky', 'python'}

s.pop() # removes the last inserted element from the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10, 'vicky'}

s.remove('vicky') # removes 'vicky' from the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10}
s.discard('vicky') # removes 'vicky' from the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10}

# s.clear() # clears the set
# print(s) # prints set()

s1=s.copy() # creates a shallow copy of the set
print(s,s1)
print(id(s), id(s1)) # prints the memory address of the set and its copy

s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2)) # prints {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.intersection(s2)) # prints {4, 5}
print(s1.difference(s2)) # prints {1, 2, 3} in the set
print(s1.symmetric_difference(s2)) # prints {1, 2, 3, 6, 7, 8}
# s1.intersection_update(s2)
# print(s1) # prints {4, 5}
# print(s2) # prints {4, 5, 6, 7, 8}
s1.difference_update(s2)
print(s1) # prints {1, 2, 3}
print(s2) # prints {4, 5, 6, 7, 8}

s1.symmetric_difference_update(s2)
print(s1) # prints {1, 2, 3, 6, 7, 8}   
print(s2) # prints {4, 5, 6, 7, 8}

print(s1.disjoint(s2)) # prints False