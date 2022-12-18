"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

def main_menu():
    print('1. пополнение счета \n')
    print('2. покупка \n')
    print('3. история покупок \n')
    print('4. выход \n')


account_balance = 0
purchase_price = ''
purchase_type = ''
acc_add = ''
purchase_history = {}

while True:
    main_menu()
    user_input = input('Выберите пункт меню \n ->')

    if user_input == '1':
        acc_add = input('Введите величину пополнения \n ->')
        try:
            account_balance += float(acc_add)
            print('Ваш балансac', account_balance)
        except:
            print('Велчина пополнения должно быть Число')
    elif user_input == '2':
        purchase_price = input('Введите сумму покупки: \n ->')
        try:
            if float(purchase_price) <= account_balance:
                purchase_type = input('Введите название покупки \n ->')
                if purchase_type in purchase_history.keys():
                    purchase_history[purchase_type] += float(purchase_price)
                    account_balance -= float(purchase_price)
                    print('Текущий балансac', account_balance)
                else:
                    purchase_history.update({purchase_type: float(purchase_price)})
                    account_balance -= float(purchase_price)
                    print('Текущий балансac', account_balance)
            else:
                print('Недостаточно средств на счёте')
        except:
            print('Проверьте введенную сумму')

    elif user_input == '3':
        print('История покупок:')
        for key, value in purchase_history.items():
            print(f'{key}: {value}')
    elif user_input == '4':
        break
    else:
        print('Неверный пункт меню')
