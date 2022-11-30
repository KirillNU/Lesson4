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


print(separator('&', 7))
