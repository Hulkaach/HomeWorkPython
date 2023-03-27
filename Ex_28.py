# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))


def sum(number1, number2):
    if int(number2) == 0:
        return int(number1)
    return 1 + sum(number1, number2-1)


print(sum(first_number, second_number))
