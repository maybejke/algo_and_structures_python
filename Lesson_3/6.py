"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


import random

a = [random.choice([i for i in range(0, 10)]) for j in range(5)]
print(a)

min_index = a.index(min(a))
max_index = a.index(max(a))
print(f'Минимальный индекс {min_index}, минимальное значение {min(a)},\n'
      f' Максимальный индекс {max_index}, Максимальное значение {max(a)}')

if min_index > max_index:
    print(sum(a[max_index + 1:min_index]))
else:
    print(f'Сумма: {sum(a[min_index:max_index])}.')



