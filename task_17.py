# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).



def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

while True:
    try:
        a = float(input('Введите 1-ое число'))
        b = float(input('Введите 2-ое число'))
        action = input('Введите операцию: + - * /')

        if action == '/':
            print(divide(a, b))
        elif action == '*':
            print(multiply(a, b))
        elif action == '+':
            print(plus(a, b))
        elif action == '-':
            print(minus(a, b))
        else:
            print("Такая операция не поддерживается!")

    except ValueError:
        print("Это не число!")
    except ZeroDivisionError:
        print("Делить на 0 нельзя!")
        print("Всего хорошего!")
        break

