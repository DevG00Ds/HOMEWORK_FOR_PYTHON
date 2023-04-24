# Задача 26:  Напишите программу, которая на вход принимает два
# числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8



def mathpow(number_A, number_B):
    if (number_B == 1):
        return number_A
    if (number_B != 1):
        return (number_A * mathpow(number_A, number_B - 1))


number_A = int(input("Введите число : "))
number_B = int(input(" Введите его степень : "))

print(' Результат : ', mathpow(number_A, number_B))
