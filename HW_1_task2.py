# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


number = int(input('Введите число : '))

number1 = number % 10
number2 = number // 10 % 10
number3 = number // 100

print(number1 + number2 + number3)
