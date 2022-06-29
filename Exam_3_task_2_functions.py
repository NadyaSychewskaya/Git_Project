# 2. Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrom(word):
    if str(word) == str(word)[::-1]:
        print("Palindrom")

palindrom(word=input("Enter a word: "))

