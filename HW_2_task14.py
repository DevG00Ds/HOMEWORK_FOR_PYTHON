# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k),
# не превосходящие числа N.


number = int(input(" Введите число : "))

number2k = 0

while 2 ** number2k <= number:
    print(2 ** number2k)
    number2k += 1
