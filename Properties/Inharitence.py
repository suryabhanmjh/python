# parent-child relationship
# Inheritance allows a class to inherit attributes and methods from another class.



class Parent:
    Bank_acc=10000
    def home(self):
        print("Home from parent class")
    def car(self):
        print("Car from parent class")
class Child(Parent):
    pass
obj=Child()
print(obj.Bank_acc)
print(obj.home())
print(obj.car())


# type of inheritance
# 1. Single Inheritance - one parent class, one child class
# 2. Multiple Inheritance - multiple parent classes, one child class
# 3. Multilevel Inheritance - one parent class, one child class, and so on
# 4. Hierarchical Inheritance - multiple child classes from one parent class
# 5. Hybrid Inheritance - combination of multiple inheritance and multilevel inheritance


