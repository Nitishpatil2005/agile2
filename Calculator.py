import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot compute the square root of a negative number")
        return math.sqrt(a)
