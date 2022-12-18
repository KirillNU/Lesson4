"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

#
# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Ввведите год рождения А.С.Пушкина:')
#
# day = input('Ввведите день рождения Пушкин?')
# while day != '6':
#     print("Не верно")
#     day = input('В какой день июня родился Пушкин?')
# print('Верно')


p_by = ''
b_month = ''
b_day = ''


def check_month():
    global b_month
    while not b_month.isdigit() or b_month != '6':
        b_month = input('Введите Число Месяца Рождения А.С. Пушкина (напр. 3) -> \n')
    return b_month


def check_day():
    global b_day
    while not b_day.isdigit() or b_day != '6':
        b_day = input('Введите Число Дня Рождения А.С. Пушкина (напр. 12) -> \n')
    return b_day


while not p_by.isdigit() or p_by != '1799':
    p_by = input('Введите Год Рождения А.С. Пушкина (напр. 1813) -> \n')
else:
    while b_month + b_day != '66':
        check_month()
        check_day()
    else:
        print(f'Верно 0{b_day} 0{b_month} {p_by}')
