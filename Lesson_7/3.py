"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint


m = int(input("put m: "))
size = 2 * m + 1
range_ = 100

arr = [randint(0, range_) for i in range(size)]
print("Random arr: ", arr)

left = 0
right = len(arr) - 1
while left <= right:
    for i in range(left, right):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    right -= 1
    for i in range(right, left, -1):
        if arr[i-1] > arr[i]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
    left += 1

print("sorted:", arr)
print("median:", arr[m])