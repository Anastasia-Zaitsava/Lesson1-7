# казино

import random
number = random.randint(1, 10)
colar = random.randint(1, 2)
print("Загаданные - число:", number, "цвет:", colar)

i = 0
while i < 5:
    i += 1
    a = int(input('Ваше число: '))
    b = int(input('Выберите цвет: 1-красный, 2-черный: '))
    if a > number:
        print("Число меньше загаданного")
        if b == colar:
            print("Вы угадали цвет")
        else:
            print("Вы не угадали цвет")
    elif a < number:
        print("Число больше загаданного")
        if b == colar:
            print("Вы угадали цвет")
        else:
            print("Вы не угадали цвет")
    elif a == number and b != colar:
        print("Вы угадали число, но не угадали цвет")
    elif a == number and b == colar:
        print("Поздравляю вы выйграли")

        break
