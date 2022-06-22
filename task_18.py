# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.

a = ('red', 'white', 'yellow', 'orange') #20
# a = [1, 2, 3, 'one', 'two', 'three' ]    #11, 3
# a = 12345                                #3
# a = "What a wonderful world!"            #19

def function(a):

    numbers = 0
    odd = 0
    letters = 0
    all_words_lenght = 0

    for i in str(a):
        if i.isdigit():
            if int(i) % 2 != 0:
                odd += 1
            for j in i:
                if j.isdigit():
                    numbers += 1
        if i.isalpha():
            letters += 1
            for j in i:
                if j.isalpha():
                    all_words_lenght += 1

    if type(a) is tuple:
        print("All words lenght: ", all_words_lenght)
    elif type(a) is list:
        print("Letters: ", letters, "Numbers: ", numbers)
    elif type(a) is int:
        print("Odd: ", odd)
    elif type(a) is str:
        print("Letters: ", letters)

function(a)





