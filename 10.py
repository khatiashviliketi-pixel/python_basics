
class BasicCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b

obj = BasicCalculator(10, 5,)
print(obj.addition())
print(obj.subtraction())
print(obj.multiplication())
print(obj.division())

print("*********************************************************")
# obj არის სახელი. რასაც მინდა იმას დავარქმევ obj-ის ნაცვლად
# CHATGPT

class BasicCalculator:
    def __init__(self, first_number, second_number):
        self.num1 = first_number
        self.num2 = second_number

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


calculator = BasicCalculator(10, 5)

print(calculator.addition())
print(calculator.subtraction())
print(calculator.multiplication())
print(calculator.division())