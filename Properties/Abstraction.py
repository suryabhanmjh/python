# Abstraction     abstract class, abstract methods, create methods


# concrete class, concrete methods, override methods
# from abc import ABC, abstractmethod
# class Senior(ABC):
#     def add(self, x, y):
#         return x + y
#     def sub(self, x, y):
#         return x - y
#     @abstractmethod
#     def mult(self, x, y):
#         pass
# class Junior(Senior):
#     def mult(self, x, y):
#         return x * y


from abc import ABC, abstractmethod
class webdb(ABC):
    def home(self):
        print("Home Page")
    def dashboard(self):
        print("Dashboard Page")
    @abstractmethod
    def login(self):
        pass
class webapp(webdb):
    def login(self, username, password):
        print(f"Web App Login Page - Username: {username}, Password: {password}")
