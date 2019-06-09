"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint


def selection_sort(array_to_sort):
    a = array_to_sort
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
