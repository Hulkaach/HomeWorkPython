# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

print('Введите размер шоколадки')
n = int(input('Введите количество столбиков шоколадки: '))
m = int(input('Введите количество строчек шоколадки: '))
k = int(input('Введите какое количество долек Вы хотите отломить: '))

if k == m*n:
    print('Вы можете забрать шоколадку целиком, ломать не нужно')
elif k > n*m:
    print('Вы не можете отломить такой кусок, поскольку сама шоколадка меньше))')

if k % m == 0 or k % n == 0:
    print(F"{n} {m} {k} -> Шоколадку можно разделить на прямоугольники") 
else:
    print(F"{n} {m} {k} -> Шоколадку нельзя разделить на прямоугольники") 
