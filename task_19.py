# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class Test:
    pass

def function_1(self):
        pass

def function_2(self):
    pass


info = input("Enter data: ")

if type(info) is str:
    info_lenght = len(info)  # во вотором методе искать
    # дописать счет гласных/согласных через функцию
    count_vowels = 0
    vowels_list = []
    count_consonants = 0
    consonants_list = []
    # vowels = "eyuioa"
    # consonants = "qwrtpsdfghjklzxcvbnm"

    for item in info:
        if item is in "eyuioa":
            count_vowels += 1
            vowels_list = vowels_list.append(item)
        elif item is in "qwrtpsdfghjklzxcvbnm":
            count_consonants += 1
            consonants_list = consonants_list.append(item)

    mult_vowels_consonants = count_vowels * count_consonants
    if mult_vowels_consonants <= info_lenght:
        print(vowels_list)
    else:
        print(consonants_list)


elif type(info) is int:
    info_lenght = len(info) #ДУБЛИРОВАНО!
    even = 0
    for item in info:
        if info % 2 == 0:
            even += 1

    result = info_lengh * even  # тут не видно, т.к. в первой части, при оформлении метода должно стать видимым
    print(result)










