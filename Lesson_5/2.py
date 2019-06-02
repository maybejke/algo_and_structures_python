"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

a = input("Введите первое 16-ое число: ")
b = input("Введите второе 16-ое число: ")

ma = []
mb = []

#развбиваем на список
for i in a:
    ma.append(i)
for i in b:
    mb.append(i)
print(ma, mb)

a = '0x'
b = '0x'

#Приводим к виду 0xcf1 0x7c9fe
for i in ma:
    a += i
print(a)

for i in mb:
    b += i
print(b)

#преобразуем в 10-тичные числа
a, b = int(a, 16), int(b, 16)
print(a, b)
# обратно в 16ричный вид
c, d = hex(a + b), hex(a * b)
print(c, d)

# summa = deque()
summa = []
# multipl = deque()
multipl = []

for i in range(2, len(c)):
    summa.append(c[i].upper())
print(f"Сумма чисел {summa}")
for i in range(2, len(d)):
    multipl.append(d[i].upper())
print(f"Произведение чисел {multipl}")

#Не понял смысла deque