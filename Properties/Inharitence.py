# parent-child relationship
# Inheritance allows a class to inherit attributes and methods from another class.



# class Parent:
#     Bank_acc=10000
#     def home(self):
#         print("Home from parent class")
#     def car(self):
#         print("Car from parent class")
# class Child(Parent):
#     pass
# obj=Child()
# print(obj.Bank_acc)
# print(obj.home())
# print(obj.car())


# type of inheritance
# 1. Single Inheritance - one parent class, one child class
# 2. Multiple Inheritance - multiple parent classes, one child class
# 3. Multilevel Inheritance - one parent class, one child class, and so on
# 4. Hierarchical Inheritance - multiple child classes from one parent class
# 5. Hybrid Inheritance - combination of multiple inheritance and multilevel inheritance


# multilevel inheritance
# class GP:
#     def home1(self):
#         print("Home from Grand Parent class")

#     def car1(self):
#         print("Car from Grand Parent class")    

# class Parent(GP):
#     def home2(self):
#         print("Home from Parent class")

#     def car2(self):
#         print("Car from Parent class")

# class Child(Parent):
#    pass
# obj=Child()
# obj.home1()  # Accessing method from Grand Parent class
# obj.car1()  # Accessing method from Grand Parent class
# obj.home2()  # Accessing method from Parent class
# obj.car2()  # Accessing method from Parent class


# multiple inheritance
# class Parent1:
#     def home1(self):
#         print("Home from  Parent1 class")

#     def car1(self):
#         print("Car from Parent1 class")

# class Parent2:
#     def home2(self):
#         print("Home from Parent2 class")

#     def car2(self):
#         print("Car from Parent2 class")

# class Child(Parent1, Parent2):
#     pass
# obj=Child()
# obj.home1()  # Accessing method from Parent1 class
# obj.car1()  # Accessing method from Parent1 class
# obj.home2()  # Accessing method from Parent2 class
# obj.car2()  # Accessing method from Parent2 class



# MRO method resolution order
# class Parent1:
#     def home(self):
#         print("Home from  Parent1 class")

#     def car1(self):
#         print("Car from Parent1 class")

# class Parent2:
#     def home(self):
#         print("Home from Parent2 class")

#     def car2(self):
#         print("Car from Parent2 class")

# class Child(Parent2, Parent1):
#     pass
# obj=Child()
# obj.home()  # Accessing method from Parent1 class



# hierarchical inheritance

# class Parent:
#     def home(self):
#         print("Home from Parent class")
#     def car(self):
#         print("Car from Parent class")
# class son(Parent):
#     pass 
# class daughter(Parent):
#     pass
# obj=son()
# obj.home()   
# obj.car()

# obj2=daughter()
# obj2.home()   
# obj2.car()       


# hybrid inheritance
# class Parent:
#     def home(self):
#         print("Home from Parent class")
#     def car(self):
#         print("Car from Parent class")
# class son(Parent):
#     pass 
# class daughter(Parent):
#     pass
# class child(son, daughter):
#     pass
# obj=child()
# obj.home()
# obj.car()


# Q mro in interview

# .overriding  python support method overriding, which allows a child class to provide a specific implementation of a method that is already defined in its parent class. This is useful for customizing the behavior of inherited methods.
# class Parent:
#     def home(self):
#         print("Home from Parent class")
#     def car(self):
#         print("Car from Parent class")
# class Child(Parent):
#     def home(self):
#         print("Home from Child class")
# obj=Child()
# obj.home()
# # obj.car()



# super() function in python
class Parent:
    def home(self):
        print("Home from Parent class")
    def car(self):
        print("Car from Parent class")
class Child(Parent):
    def home(self):
        print("Home from Child class")
        super().home()  # Calling the parent class method
obj=Child()
obj.home()
# obj.car()