# -*- confing: utf-8 -*-

# Класс для заполнения списка сообщениями об ошибках
class ListMessages:
    messages = []

    def add_message(self, message):
        self.messages.append(message)


def string_to_int(st):
    list_messages = ListMessages()
    try:
        int(st)
    except ValueError as exc:
        list_messages.add_message(
            f'Функция принимает аргумент "st" правильного типа - {type(st)}, \n но не корректного значения - {exc}')
    else:
        list_messages.add_message(f'Функция работает правильно')
        return int(st)
    finally:
        list_messages.add_message(f'Функция отработала\n')


value_1 = string_to_int('4')
print(value_1, '\n')


def read_file(filename):
    file = None
    list_messages = ListMessages()
    try:
        # with open(filename, 'w') as file:
        file = open(filename, 'r', encoding='utf8')
        content = file.read()
    except FileNotFoundError as exc:
        list_messages.add_message(f'Файл {filename} не найден. Ошибка - {exc}')
    except IOError as exc:
        list_messages.add_message(f'Ошибка вода/вывода при работе с файлом {filename}. Ошибка - {exc}')
    else:
        list_messages.add_message(f'Функция работает правильно')
        return content
    finally:
        list_messages.add_message(f'Функция отработала\n')
        if file is not None:
            file.close()


value_2 = read_file('myfile.txt')
print(value_2, '\n')


def divide_numbers(a, b):
    list_messages = ListMessages()
    try:
        a / b
    except ZeroDivisionError as exc:
        list_messages.add_message(f'Нельзя делить на ноль. Ошибка - {exc}')
    except TypeError as exc:
        list_messages.add_message(f'Недопустимый тип {type(a)} или {type(b)} значения. Ошибка - {exc}')
    else:
        list_messages.add_message(f'Функция работает правильно')
        return a / b
    finally:
        list_messages.add_message(f'Функция отработала\n')


value_3 = divide_numbers(8, 4)
print(value_3, '\n')

lst = [8, 'dsfl', {'a': 34}]
index = 2


def access_list_element(ls, ind):
    list_messages = ListMessages()
    try:
        ls[ind]
    except IndexError as exc:
        list_messages.add_message(f'Индекс {ind} вне диапазона списка. Ошибка {exc}')
    except TypeError as exc:
        list_messages.add_message(f'Индекс {ind} должен быть целым числом. Ошибка {exc}')
    else:
        list_messages.add_message(f'Функция работает правильно')
        return ls[ind]
    finally:
        list_messages.add_message(f'Функция отработала\n')


value_4 = access_list_element(lst, index)
print(value_4, '\n')

# Функция для записи сообщений из списка из класса ListMessages в файл error_box.txt
def print_error_box():
    access_list = ListMessages.messages
    with open('error_box.txt', mode='w+', encoding='utf8') as file:
        for elem in access_list:
            file.write(elem + '\n')


print_error_box()

