# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками.


def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]

while True:
    card = str(int(input("Enter your credit card number:")))

    if len(card) != 16:
        print("You may enter 16 digits")
    else:
        print(card_hide(card))
        break


