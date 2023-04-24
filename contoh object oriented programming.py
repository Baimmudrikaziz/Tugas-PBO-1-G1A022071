class Square:
    def __init__(self, x):
        self.x = x
    def calculate(self):
        return self.x*self.x

s = Square(5)
result = s.calculate()
print(result) # Output: 25
