class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def add(self):
        print("Addition:", self.a + self.b)


    def subtract(self):
        print("Subtraction:", self.a - self.b)



class AdvancedCalculator(Calculator):
    def add(self):

        print("Advanced Addition (sum squared):", (self.a + self.b) ** 2)

    def multiply(self):
        print("Multiplication:", self.a * self.b)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


    def __str__(self):
        return f"Point({self.x}, {self.y})"


calc1 = Calculator(5, 3)
calc1.add()
calc1.subtract()

adv_calc = AdvancedCalculator(5, 3)
adv_calc.add()
adv_calc.multiply()
adv_calc.subtract()

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2      # Calls __add__
print("Point Addition Result:", p3)
