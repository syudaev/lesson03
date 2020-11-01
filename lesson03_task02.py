# реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон
# функция должна принимать параметры как именованные аргументы
# реализовать вывод данных о пользователе одной строкой

def chek_num(user_string):
    """проверка и обработка ввода года рождения в интервале от 1900 до 2020"""
    while True:
        try:
            user_chek = int(input(user_string))
            if 1900 <= user_chek <= 2020:
                return user_chek
            else:
                print('\x1b[31mОшибка! Введите год в интервале от 1900 до 2020!\x1b[0m')
        except ValueError:
            print('\x1b[31m"Ошибка! Введите год в интервале от 1900 до 2020!\x1b[0m')
        continue


def my_func(name, surname, birth, city, email, phone):
    """передаются именованные переменные в случайном порядке, "склейка" строки и возврат строки"""
    return ' '.join([name, surname, birth, city, email, phone])


user_name = input('Введите имя: ')
user_surname = input('Введите фамилию: ')
user_birth = str(chek_num('Введите год рождения: '))
user_city = input('Введите город проживания: ')
user_email = input('Введите email: ')
user_phone = input('Введите номер телефона: ')

print('\n\x1b[34m', my_func(birth=user_birth, surname=user_surname, phone=user_phone, name=user_name,
                            email=user_email, city=user_city), '\x1b[0m')
