
#   #static/Class varibale in python

# #instance variable=esa varibale jo object depeendent hota he
# class variable=esa variable jo change nahi hoga like school ka name principle ka name etc 
# class Student:
#   school='SHSS'  #declartion of the classs variabble
#   def __init__(self,name,gread,roll):
#     self.n=name
#     self.g=gread
#     self.r=roll
#   def show(self):
#     print(self.n)
#     print(self.g)
#     print(self.r)
#     print(Student.school)   #accessiing of class variable inside methods
# obj=Student('ramesh','m.tch',101)
# obj.show()
# obj1=Student('Rahul','Btech',102)
# obj1.show()

# class Student:
#   school='SHSS'  #declartion of the classs variabble
#   def __init__(self,name,gread):
#     self.n=name
#     self.g=gread
#     Student.principal='python'  #declare
#     print(Student.city)  #acce
#   def show(self):
#     print(self.n)
#     print(self.g)
#     print(self.r)
#     print(Student.school)   #accessiing of class variable inside methods
#     print(Student.city) #aceess
# Student.city='Bhopal'
# obj=Student('Aman','M.tech')



#  Classs Method
#@classmethod se isey show kiya jata he 
#first paramter is cls instead of self
#used to create/update any class variabvle

# class Student:
#   gread='ist'
#   def __init__ (self,name,roll):
#     self.n=name
#     self.r=roll
#   def show(self):
#     print(self.n)
#     print(self.r)
#     print(Student.gread)
#   @classmethod
#   def update(cls,x):
#     cls.gread=x
# obj=Student('Ramesh',101)
# obj.show()
# obj.update('2nd')
# obj.show()


