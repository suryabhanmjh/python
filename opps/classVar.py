# class variables/ static variables
class Student:
    school_name = "SHSS"  # class variable

    def __init__(self, name, grade, roll_no, age):
        self.n = name
        self.g = grade
        self.r = roll_no
        self.a = age
        Student.principal = "Mr. Sharma"  # class variable
    

    def show(self):
        print(f"Name: {self.n}, Age: {self.a}, Grade: {self.g}, Roll No: {self.r}, School: {Student.school_name}, {Student.city}, Principal: {Student.principal}")
# Student.school_name = "SSSS"  # Changing the class variable

print(Student.school_name)  # Accessing the class variable
obj= Student("Ramesh", "10th", 101, 15)
obj.show()
print(Student.principal)  # Accessing the class variable
obj2 = Student("Shyaam", "9th", 102, 14)
obj2.show()
Student.city = "Delhi"  # Adding a new class variable
print(Student.city)  # Accessing the new class variable
obj2.show()

# Accessing the class variable
# declaration        in-side class, # outside class, in-side method, outside method
# accessing         using class name, using