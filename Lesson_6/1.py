"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile



@profile
def function():
    data = {}
    n = int(input("Введите количество предприятий: "))
    p = 0
    for i in range(n):
        pname = input((str(i+1) + " Наименование предприятия: "))
        p_1kv = int(input("Прибыль за первый квартал: "))
        p_2kv = int(input("Прибыль за второй квартал: "))
        p_3kv = int(input("Прибыль за трейтий квартал: "))
        p_4kv = int(input("Прибыль за четвертый квартал: "))
        # p_sred = (p_1kv + p_2kv + p_3kv + p_4kv)/4
        p_god = (p_1kv + p_2kv + p_3kv + p_4kv)
        data[pname] = p_god
        p += p_god
    avrg = p / n

    print(f"Средняя прибыль за год  всех предприятий: {avrg}")
    print(f"{data}")

    for i in data:
        if data[i] > avrg:
            print(f"Предприятия прибыль больше среднего: {i}")
    for i in data:
        if data[i] < avrg:
            print(f"Предприятия прибыль меньше среднего: {i}")

function()

@profile
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

@profile
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


# так понимаю не большие объемы, забирает по 10 мб и успокаивается. macOS.