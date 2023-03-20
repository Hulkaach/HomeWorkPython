# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random
found_number = 0

array_length = input("Введите длину массива: ")
while array_length.isdigit() == False or int(array_length) == 0:
    array_length = input("Введите длину массива: ") 

search_number = input("Введите число, которое необходимо проверить: ")
while search_number.isdigit() == False or int(array_length) == 0:
    search_number = input("Введите натуральное число, которое необходимо проверить: ") 

array = [random.randint(1,10) for _ in range(int(array_length))]
print(array)

set_array = set(array)
print(f"Преобразованный массив \n {set_array}")

for i in set_array:
    if (int(i)/int(search_number)) <= 1:
        found_number = i
  
print(f"Наиболее близкое число к введенному '{search_number}' из вышеуказанного массива - это число {found_number}")
