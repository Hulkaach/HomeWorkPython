# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример
# 4 4 -> 2 2
# 5 6 -> 2 3

import random
import math
num_X = random.randint(1, 1000)
num_Y = random.randint(1, 1000)

print(num_X,num_Y)
sum_num = num_X + num_Y
multiplication_num = num_X * num_Y

half_sum = sum_num/2
temp_x = multiplication_num-(half_sum*half_sum)
if temp_x < 0:
    temp_x *=-1

x = half_sum-math.sqrt(temp_x)
y = half_sum+math.sqrt(temp_x)

print(f"Сумма цифр, загаданых Петей составляет - {sum_num}")
print(f"Произведение цифр, загаданых Петей составляет - {multiplication_num}\n")
print(f"Числа загаданные Петей это {int(x)} и {int(y)}\n") 
print(f"Проверка {num_X} и {num_Y}") 