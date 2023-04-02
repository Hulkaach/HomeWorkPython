# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# min max сами задаем

import random

array = [random.randint(-9, 10) for _ in range(random.randint(10, 20))]
print(f"Исходный массив: \n{array}")

num_min = int(input('Введите минимальное значение: '))
num_max = int(input('Введите максимальное значение: '))
result_num = []
result_index = []

for i in range(0, len(array)):
    if array[i] <= num_max and array[i] >= num_min:
        result_num.append(array[i])
        result_index.append(i)

print(f'Значения элементов массива между min - {num_min} и max - {num_max}:\n {result_num}')
print(f'Их индексы \n{result_index}')
