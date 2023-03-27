# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# # Затем пользователь вводит сами элементы множеств.
import random

n = int(input("Введите размерность первого массива: "))
m = int(input("Введите размерность второго массива: "))
list1 = [random.randint(1, 10) for _ in range(1, n)]
list2 = [random.randint(1, 10) for _ in range(1, m)]

print(f"Изначальный первый массив: {list1}")
print(f"Изначальный второй массив: {list2}")

list1 = set(list1)
list2 = set(list2)

print(f"Отформатированный в множество первый массив: {list1}")
print(f"Отформатированный в множество второй массив: {list2}")

list3 = list1.intersection(list2)

print(f"Элементы, которые встечаются в обоих массивах: {list3}")
print(f"Отсортированные в порядке возрастания элементы, которые встечаются в обоих массивах: {sorted(list3)}")

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
