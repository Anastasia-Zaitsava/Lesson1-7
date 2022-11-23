# Записать в массив все числа в диапазоне от 1 до 500 кратные 5.
mas = []
for i in range(1, 500):
    if i % 5 == 0:
        mas.append(i)
print(mas)