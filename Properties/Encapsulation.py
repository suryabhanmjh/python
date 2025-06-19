# in opps method & variables are wraped in single unit
# Access Modifiers
# Public - can be accessed from anywhere     x/display()
# Private - can be accessed only within the class  __x/__display()
# Protected - can be accessed within the class and its subclasses  _x/_display()

# public variable/ public method
# class Parent:
#     x=2
#     def display(self):
#         print("from parent class")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj.x)  # Accessing public variable
# print(obj.display())

# protected 
# class Parent:
#     _x=2
#     def _display(self):
#         print("from parent class")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj._x)  # Accessing protected variable
# print(obj._display())

# private
# class Parent:
#     __x=2
#     def __display(self):
#         print("from parent class")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj.__x)  # Accessing private variable
# print(obj.__display())


class Parent:
    __x=10
    def __display(self):
        print("from parent class")
class Child(Parent):
    pass
obj=Child()
# print(obj.__x)  # Accessing private variable
# print(obj.__display())
print(dir(Parent))
print(Parent._Parent__x)
print(obj._Parent__x)