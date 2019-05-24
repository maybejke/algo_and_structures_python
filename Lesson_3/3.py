#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random, randint


a = []
N = int(random()*10)
for i in range(N):
    a.append(int(random()*100))
print(N)
print(a)

for i in range(N):
    f = True
    for j in range(N):
        if a[i] == a[j] and a != j:
            f = False
            break
        if f == True:
            print(a[i], end=' ')