"""Calculator module"""

class Calculator:
    """
    Module of calculator class
    """
    def __init__(self, op1: float, op2: float):
        """Initialize the calculator class"""
        self.op1 = op1
        self.op2 = op2

    def add(self):
        """Add two numbers"""
        return self.op1 + self.op2

    def subtract(self):
        """Subtract two numbers"""
        return self.op1 - self.op2

    def multiply(self):
        """Multiply two numbers"""
        return self.op1 * self.op2

    def divide(self):
        """Divide two numbers"""
        if self.op2 == 0:
            raise ValueError("Can't divide by 0")
        return self.op1 / self.op2
