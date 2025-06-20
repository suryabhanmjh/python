# function

# method overloading

class Addition:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
    def add(self, a, b, c, d):
        return a + b + c + d
    def add(self, *numbers):
        sum =0 
        for i in numbers:
            sum += i
        print(sum)
obj = Addition()
obj.add(1, 2)