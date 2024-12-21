class Calculator:
    def __init__(self):
        pass

    def str_to_float(self, value: str):
        global result
        try:
            result = float(value)
        except ValueError:
            print("Помилка: неможливо конвертувати значення в число.")
            result = None
        finally:
            return result

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float):
        global result
        try:
            result = a / b
        except ZeroDivisionError:
            print("Помилка: ділення на нуль неможливе.")
            result = None
        finally:
            return result

    def calculate(self, num1: str, operator: str, num2: str):
        a = self.str_to_float(num1)
        b = self.str_to_float(num2)

        if a is None or b is None:
            print("Помилка в введених числах.")
            return None

        if operator == "+":
            return self.add(a, b)
        elif operator == "-":
            return self.subtract(a, b)
        elif operator == "*":
            return self.multiply(a, b)
        elif operator == "/":
            return self.divide(a, b)
        else:
            print("Невідомий оператор.")
            return None


calc = Calculator()

num1 = input("Введіть перше число: ")
operator = input("Введіть оператор (+, -, *, /): ")
num2 = input("Введіть друге число: ")

result = calc.calculate(num1, operator, num2)
if result is not None:
    print("Результат:", result)