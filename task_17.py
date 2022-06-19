# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).



def divide():
    return a / b

def multiply():
    return a * b

def plus():
    return a + b

def minus():
    return a - b

while True:
    try:
        a = float(input('Введите 1-ое число'))
        b = float(input('Введите 2-ое число'))
        action = input('Введите операцию: + - * /')

        if action == '/':
            print(divide())
        elif action == '*':
            print(multiply())
        elif action == '+':
            print(plus())
        elif action == '-':
            print(minus())

    except ValueError:
        print("Это не число!")
    except ZeroDivisionError:
        print("Делить на 0 нельзя!")
        print("Всего хорошего!")
        break

