# frozen  set
# collection of unordered unique elements
# representation through frozenset() with comma (,) separated values
# indexing not supported
# slicing not supported
# immutable in nature

# example
l1=[1, 2, 3, 4, 5]
l2=[10,20,30,40,50]
fs1 = frozenset(l1)
fs2 = frozenset(l2)
print(fs1) # prints frozenset({1, 2, 3, 4, 5})
print(type(fs1)) # prints <class 'frozenset'>
print(fs2) # prints frozenset({10, 20, 30, 40, 50})
print(type(fs2)) # prints <class 'frozenset'>

# methods for frozenset
print(fs1.union(fs2)) # prints frozenset({1, 2, 3, 4, 5, 10, 20, 30, 40, 50})
print(fs1.intersection(fs2)) # prints frozenset()
print(fs2.difference(fs1)) # prints frozenset({10, 20, 30, 40, 50})
print(fs1.difference(fs2)) # prints frozenset({1, 2, 3, 4, 5})
print(fs1.symmetric_difference(fs2)) # prints frozenset({1, 2, 3, 4, 5, 10, 20, 30, 40, 50})