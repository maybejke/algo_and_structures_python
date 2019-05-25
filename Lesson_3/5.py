#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint
a = []
max_otr = 0
for i in range(10):
    a.append(randint(-10, 10))
print(a)

for i in a:
    if i < 0:
        max_otr = max([i])

print(max_otr)
print(f"Максимальный отрицательный эдемент {max_otr}, под номером {a.index(max_otr)}")

