# Создайте кортеж из случайных 10 чисел. Найдите его максимальный минимальный элемент.
import random
a = [random.randint(1, 100) for i in range(10)]
b = tuple(a)
print(b)
print("max", max(a), "min", min(a))