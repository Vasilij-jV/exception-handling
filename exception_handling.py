# -*- confing: utf-8 -*-

def string_to_int(st):
    try:
        return int(st)
    except ValueError as exc:
        print(f'Функция принимает аргумент "st" правильного типа - {type(st)}, но не корректного значения - {exc}')
    finally:
        print(f'Функция отработала')


value_string_to_int = string_to_int('4')
print(value_string_to_int, '\n')


def read_file(filename):
    try:
        # with open(filename, 'w') as file:
        with open(filename, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError as exc:
        print(f'Файл {filename} не найден. Ошибка - {exc}')
    except IOError as exc:
        print(f'Ошибка вода/вывода при работе с файлом {filename}. Ошибка - {exc}')
    finally:
        print(f'Функция отработала')


value_read_file = read_file('myfile.txt')
print(value_read_file, '\n')


a = 7
b = 5
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as exc:
        print(f'Нельзя делить на ноль. Ошибка - {exc}')
    except TypeError as exc:
        print(f'Недопустимый тип {type(a)} или {type(b)} значения. Ошибка - {exc}')
    finally:
        print(f'Функция отработала')


value_divide_numbers = divide_numbers(a, b)
print(value_divide_numbers, '\n')

lst = [8, 'dsfl', {'a': 34}]
index = 2.4
def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError as exc:
        print(f'Индекс {index} вне диапазона списка. Ошибка {exc}')
    except TypeError as exc:
        print(f'Индекс {index} должен быть целым числом. Ошибка {exc}')
    finally:
        print(f'Функция отработала')


value_access_list_element = access_list_element(lst, index)
print(value_access_list_element, '\n')
