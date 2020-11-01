# реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов

def chek_num(user_string):
    """ проверка на ввод чисел(+целые +дробные +отрицательные) """
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


def my_func(user_arg1, user_arg2, user_arg3):
    """ принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов """
    my_list = [user_arg1, user_arg2, user_arg3]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


print(my_func(chek_num("Введите первый аргумент >>> "),
              chek_num("Введите второй аргумент >>> "),
              chek_num("Введите третий аргумент >>> ")))
