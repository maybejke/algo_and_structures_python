"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


import timeit
import cProfile

"""
Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""



N = 100000

a = 5
sum_el = 0


def equal2():
    n = 5
    sum_el = 0
    for i in range(n):
        sum_el += i
        if i == n:
            if sum_el == n * (n + 1) / 2:
                print('Teory is true')
            else:
                pass
        else:
            i += 1

print(timeit.timeit('equal2()', setup="from __main__ import equal2", number=5))


def equal1(n=1, start_el=1, sum_el=0):
    sum_el += start_el
    if start_el == n:
        if sum_el == n * (n + 1) / 2:
            print("Teory is true")
        else:
            pass
    else:
        start_el += 1
        return equal1(n, start_el, sum_el)

print(timeit.timeit('equal1(n=5, start_el=1, sum_el=0)', setup="from __main__ import equal1", number=5))
cProfile.run('equal1()')
cProfile.run('equal2()')
