# Задача №49. Решение в группах
# Создать телефонный справочник с # возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер # телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в # текстовом файле
# 3. Пользователь может ввести одну из # характеристик для поиска определенной
# записи(Например имя или фамилию # человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n', '').split(sep=',')
            data_array.append(item)
    return data_array


def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')


def add_item(filename, lastname='', firstname='', secondname='', phone=''):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)

def change(filename, id, data):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        if data_array[i][0] == id:
            if data == 1:
                data_array[i][1] = input('Фамилия ')
            if data == 2:
                data_array[i][2] = input('Имя ')
            if data == 3:
                data_array[i][3] = input('Отчество ')
            if data == 4:
                data_array[i][4] = input('Телефон ')
    write_file(filename, data_array)

def delete(filename, id):
    data = read_file(filename)
    for i in range(1, len(data)):
        if data[i][0] == id:
            del data[i]
    write_file(filename, data)

def show_all_items(filename):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        print("ID: ", data_array[i][0], "Фамилия: ", data_array[i][1], "Имя: ",
              data_array[i][2], "Отчество: ", data_array[i][3], "Телефон: ", data_array[i][4])


def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2:
        add_item(filename)
    elif user_operation == 3:
        id = input('Укажите ID записи: ')
        variable = int(input('Что изменить? 1 - Фамилия, 2 - Имя, 3 - Отчество, 4 - Телефон'))
        change(filename,id,variable)
        show_all_items(filename)
    elif user_operation == 4:
        id = input('Укажите ID записи: ')
        delete(filename,id)


filename = 'file.txt'
menu()
