"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

import random

a = [random.choice([i for i in range(0, 10)]) for j in range(5)]
print(a)

min_index = a.index(int(min(a)))
print(min_index)
min1 = a.pop(min_index)
min2 = a.pop(min_index)
print(min1, min2)

# Периодически ломается, не пойму что не правильно. Pop index out of range. Так понимаю надо добавить какую-то проверку?