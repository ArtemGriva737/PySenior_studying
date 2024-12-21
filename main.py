print('Lesson 7. Iterators, Decorators')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('before:\n', numbers, '\n')


def convert(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        print(f"Результат '{value}' не вдалося конвертувати до числа!")
        return None


def up_square(n):
    if n % 2 != 0:
        result = n ** 2
    else:
        result = n
    return convert(result)


def widn(n):
    if n % 2 != 0:
        result = n - 5
    else:
        result = n
    return convert(result)


def mnog(n):
    if n % 2 != 0:
        result = n * 2
    else:
        result = n
    return convert(result)


def perevirka(n, dilnik):
    try:
        return n / dilnik
    except ZeroDivisionError:
        print("На нуль ділити не можна!")
        return None


def dil(n):
    if n % 2 != 0:
        return perevirka(n, 2)
    else:
        result = n
    return convert(result)


numbers_square = [up_square(n) for n in numbers if n >= 5]
numbers_widn = [widn(n) for n in numbers if n >= 5]
numbers_mnog = [mnog(n) for n in numbers if n >= 5]
numbers_dil = [dil(n) for n in numbers if n >= 5]
print(
    f'after:\n Up square - {numbers_square}\n Subtraction - {numbers_widn}\n Multiplication - {numbers_mnog}\n Division - {numbers_dil}')
