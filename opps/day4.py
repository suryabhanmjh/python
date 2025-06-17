#local variable
# class student:
#   def new(self):
#     x=10
#     print(x)
#   def new1(self):
#     print(x)
# obj1=student()
# obj1.new()



class student:
  def first(self):
    print("from first method")
    
  @staticmethod
  def wel_great():
    print("welcome this webspage")
    
  @staticmethod
  def thankx_great():
    print("thankx for visit")
obj=student()
obj.wel_great()
    