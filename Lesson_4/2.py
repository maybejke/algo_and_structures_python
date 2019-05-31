"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import timeit


def sie(lim, n):
    def sieve(n):
        a = [x for x in range(n + 1)]
        a[1] = 0
        lst = []
        i = 2
        while i <= n:
            if a[i] != 0:
                lst.append(a[i])
                for j in range(i, n + 1, i):
                    a[j] = 0
            i += 1
        return lst
    while len(sieve(n)) < lim:
        n += 1
    return sieve(n).pop()


def nosieve(lim, n):
    def nosieve_algo(n):
        lst = []
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
        return lst
    while len(nosieve_algo(n)) < lim:
        n += 1
    return nosieve_algo(n).pop()


lim = int(input("Введите номер простого числа: "))
n = 2


print(sie(lim, n))
print(nosieve(lim, n))

print(timeit.timeit("sie(100, 2)", setup="from __main__ import sie", number=10))
print(timeit.timeit("nosieve(100, 2)", setup="from __main__ import nosieve", number=10))


# Решето работает быстрее на большем порядковом номере.