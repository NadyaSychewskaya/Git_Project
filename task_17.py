# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


while True:

    try:
        a = float(input('Введите 1-ое число'))
        b = float(input('Введите 2-ое число'))
        action = input('Введите операцию: + - * /')

        if action == '/':
            def divide():
                return a / b
            print(divide())

        elif action == '*':
            def multiply():
                return a * b
            print(multiply())

        elif action == '+':
            def plus():
                return a + b
            print(plus())

        elif action == '-':
            def minus():
                return a - b
            print(minus())

    except ValueError:
        print("Это не число!")
    except ZeroDivisionError:
        print("Делить на 0 нельзя!")
        print("Всего хорошего!")
        break

