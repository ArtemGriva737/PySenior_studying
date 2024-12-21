import logging

logging.basicConfig(level=logging.INFO,
                    filename='logs.txt', filemode='a',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    encoding='utf-8')

print('Homework 8: Logging')


class Calculation:
    def __call__(self, a, b, operation):
        try:
            a = self.convert(a)
            b = self.convert(b)

            if operation == '+':
                return a + b
            elif operation == '-':
                return a - b
            elif operation == '*':
                return a * b
            elif operation == '/':
                if a == 0 or b == 0:
                    raise ZeroDivisionError("Спроба ділення на нуль")
                return a / b
            else:
                raise ValueError("Невідомий оператор.")

        except Exception as error:
            logging.error(f"Помилка при обчисленні: {error.__str__()}")
            return None

    def convert(self, value):
        try:
            if isinstance(value, (int, float)):
                return value
            elif isinstance(value, str) and '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError as error:
            logging.error(f"Помилка конвертації значення '{value}': {error.__str__()}")
            raise ValueError(f"Неможливо конвертувати значення '{value}' до числа.")


calculation = Calculation()

logging.info('start app')
print(calculation(a = input('Введіть перше число: '), b = input('Введіть друге число: '), operation = input('Введіть оператора: ')))
logging.info('end app')