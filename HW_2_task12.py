# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.


number1 = int(input(" Введите 1 число : "))
number2 = int(input(" Введите 2 число : "))

for i in range(number1):
    for j in range(number2):
        if number1 == i + j and number2 == i * j:
            print(i, j)
            break
    else:
        continue

    break