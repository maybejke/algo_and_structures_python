# 4.	Определить, какое число в массиве встречается чаще всего.

from random import random


a = []
b = None
count = 0

for i in range(int(random()*50)):
    a.append(int(random()*100))

for i in a:
    if a.count(i) > count:
        count, b = a.count(i), i

print(f'В списке {a}, наибольшее количество раз {count} встречается число {b}.')