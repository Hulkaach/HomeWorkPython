# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# Пример
# 5 -> 1 0 1 1 0
# 2

import random
coin = input('Введите количество монеток: ')

while str.isdigit(coin) == False: # Проверяем содержатся ли цифры в веденными пользвателем данными 
    coin = input('Введите количество монеток: ')

if int(coin) == 0:
    print('Если монет нет, то и переворачивать нечего')
elif int(coin) == 1:
    print('Если всего одна монетка, то и переврачивать ничего не надо')
else:
    coins = [random.randint(0, 1)for i in range(int(coin))] # создаем список с рандомными цифрами и размерностью, введенной пользователем
    count_heads = 0
    count_tails = 0
    for j in coins:
        if j == 0:
            count_tails += 1
        if j == 1:
            count_heads += 1
    print(coins)
    if count_heads < count_tails:
            print(
        f"Минимальное число монеток, которые нужно перевернуть, составляет {count_heads}")
    else:
            print(
        f"Минимальное число монеток, которые нужно перевернуть, составляет {count_tails}")
 