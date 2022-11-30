# def mult_list(*args):
#     mult = 1
#     for x in args:
#          mult *=x
#     return mult
#
# print(mult_list(1, 2, 3, 4, mult_list(2)))
#
# p = mult_list
#
# print (id(p), id(mult_list()))


def simple_separator():
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********
    """
    return '*' * 10


# print(simple_separator())


def long_separator(count):
    """
      Функция создает разделитель из звездочек число которых можно регулировать параметром count
      :param count: количество звездочек
      :return: строка разделитель, примеры использования ниже
      """
    return ('*' * count)


# print(long_separator(6))


def separator(symbol, count):
    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    return (symbol * count)


# print(separator('&', 7))


def hello_world():
    """
    Функция печатает Hello World в формате:
    **********

    Hello World!

    ##########
    :return: None
    """
    print(separator('\"', 10), '\n')
    print('Hello World!', '\n')
    print(separator('#', 10))


# hello_world()

def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    print(separator('\"', 10), '\n')
    print(f'Hello {who}', '\n')
    print(separator('#', 10))


# hello_who('Pete')

def pow_many(power, *args):
    """
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
    """
    total = 0
    for i in args:
        total += i
    return total ** power


# print(pow_many(2, 1, 2, 3, 4) == 100)

def print_key_val(**kwargs):
    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
    for key, value in kwargs.items():
        print(f'{key} --> {value}')


# print_key_val(name='Max', age=21)
# print_key_val(animal='Cat', is_animal=True)


def filter_function(**kwargs):
    list_filtered = []
    for i in kwargs:
       if i in list_filtered:
           list_filtered.append(i)
       else:
           pass

    return list_filtered


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    pass

# print(function([1, 2, 3, 4, 5]))


# print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
# print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
# print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
# print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
