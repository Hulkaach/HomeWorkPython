# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# an = a1  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a1 = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('Введите разность элементов арифметической прогрессии: '))
n = int(input('Введите количество элементов арифметической прогрессии: '))

array = []
for i in range(n):
    array.append(a1+i*d)

print(array)


def sum_progression(first_element, difference, quantity):
    if quantity == 0:
        return 0
    return first_element + sum_progression(first_element+difference, difference, quantity-1)


print(f"Сумма элементов прогрессии равна - {sum_progression(a1, d, n)}")
