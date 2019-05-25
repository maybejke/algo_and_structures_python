# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random


def max_number(a):
    m = a[0]
    for i in a:
        # f = True
        if i > m:
            m = i
    return m


def min_number(a):
    m = a[0]
    for i in a:
        # f = True
        if i < m:
            m = i
    return m

a = []
N = int(random() * 10)
for i in range(N):
    a.append(int(random() * 100))
print(a)
min_index = a.index(min_number(a))
max_index = a.index(max_number(a))

print(min_index, max_index)

a[min_index], a[max_index] = a[max_index], a[min_index]

print(a)
