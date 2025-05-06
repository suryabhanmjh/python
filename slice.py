# slice

# rules for slicing
# 1. Slicing is done on the first axis of the array
# 2 check step direction if step is negative, then reverse the order of the array
# 3. check if the start and end are in the range of the array, if not, then
# 4 check start 4 stop points direction . if not given it follows step direction
#  collecion [start:stop:step/direction]

s='i love python'
print(s[::]) # prints i love python

print(s[::-1]) # prints nohtyp evol i

print(s[2:10]) # prints love pyt

print(s[7:-10]) # prints ''
print(s[7:-2]) # prints thon
print(s[7:7]) # prints ''

v='I love python'
print(v[::-1][1:7][::-1][2:3])
