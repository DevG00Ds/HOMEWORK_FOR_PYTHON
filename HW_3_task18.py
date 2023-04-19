# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
#
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

number = abs(int(input(" Введите кол-во элементов в массиве : ")))
lst = [randint(1, 9) for i in range(number)]
lst_A = list(map(int, lst))
print(lst_A)
num = int(input(" Введите число которое будем сравнивать : "))
min = abs(num - lst_A[0])
count = 0
for i in range(0, number):
    count = abs(num - lst_A[i])
    if count < min:
        min = count
        count = i
print(f" Число {lst[count]} близко находится к числу {num}")
