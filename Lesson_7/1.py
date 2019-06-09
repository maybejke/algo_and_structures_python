"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint
import timeit

def selection_sort(ary):
    a = ary
    for i in range(len(a)):
        idx_max = i
        for j in range(i + 1, len(a)):
            if a[j] > a[idx_max]:
                idx_max = j
        tmp = a[idx_max]
        a[idx_max] = a[i]
        a[i] = tmp
    return a


ary = [randint(-100, 100) for i in range(10)]
print(selection_sort(ary))
print(timeit.timeit("selection_sort(ary)", setup="from __main__ import selection_sort, ary", number=10000))
print("/\ В разы медленне чем улучшенный пузырьковый метод")

def selection_sort_upd(ary):
    n = 1
    m = 0
    while n < len(ary):
        for i in range(len(ary) - n):
            if ary[i] < ary[i+1]:
                ary[i], ary[i+1] = ary[i+1], ary[i]
                m = 1
        if m == 0:
            break
        n += 1
    return ary
print(selection_sort_upd(ary))
print(timeit.timeit("selection_sort_upd(ary)", setup="from __main__ import selection_sort_upd, ary", number=10000))


