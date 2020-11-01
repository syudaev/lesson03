# реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление
# числа запрашивать у пользователя
# предусмотреть обработку ситуации деления на ноль

def chek_num(user_string):
    """проверка и обработка ввода значений численного типа int и float"""
    while True:
        user_chek = input(user_string)
        if user_chek.isdigit():
            user_chek = int(user_chek)
            return user_chek
        try:
            user_chek = float(user_chek)
            return user_chek
        except ValueError:
            print("\x1b[31m", 'Ошибка! Вводите только числа!', "\x1b[0m")
            continue


def chek_numeric(arg_divider, arg_divided):
    """проверка и обработка ситуации деления на ноль"""
    try:
        return arg_divider / arg_divided  # user_division
    except ZeroDivisionError:
        return print("\n\x1b[31m", 'Ошибка! Делить на ноль нельзя!', "\x1b[0m")


user_divider = chek_num("Введите число делитель >>> ")
user_divided = chek_num("Введите число делимое >>> ")
user_division = chek_numeric(user_divider, user_divided)
if user_division is not None:
    print(f'\n {user_division:.4f}')
