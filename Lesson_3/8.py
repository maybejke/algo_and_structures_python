"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import randint

M = 5
N = 4
a =[]
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(0, 10))
        print("%3d" % b[j], end='',)
    a.append(b)
    print(' ', sum(b), '  |')
for i in range(M):
    print(' --', end='')
print()
