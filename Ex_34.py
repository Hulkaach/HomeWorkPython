# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

# list1 = input('Введите строку. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами:\n')
list1 = ('Хорошо-живет-на-свете-Винни-Пух! Оттого-поет-он-эти-Песни-вслух')
# перевожу все знаки в нижний регистр и создаю список разбивкой по пробелам - функиця split() - по умолчанию разделители пробелы
list2 = list1.lower().split()
print(f'Введенный текст: \n{list1}')
print(f'Сделанный список из текста: \n{list2}')
vowels = ('уеыаоэяиюё')


def summa_glasnix(list):  # Функция заходит в каждое "слово" в списке и в каждом слове ищет сосотоит ли буква в заранее подготовленной строке с гласными буквами
    # и считает скольо там подходящих букв
    res = 0
    for word in list:
        for i in word:
            if i in vowels:
                res += 1
    return res


def ravenstvo(operator, list):  # Функция будет принимать заранее подготовленную функцию подсчета букв и перебором, как в обычном массиве считает сколько в списке одинаковых 
    # по кол-ву нужных букв слов
    result = 0
    temp = operator(list[0])
    for i in range(len(list)):
        if operator(list[i]) == temp:
            result += 1
        else:
            result -= 1
    return result


if ravenstvo(summa_glasnix, list2) == len(list2): # Тупо смотрим соответствует ли количество найденных одинаково длинных слов с нужными буквами и длину самого списка (если совпадают - то ок)
    print('Парам пам-пам')
else:
    print('Пам парам')