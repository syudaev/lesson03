# программа принимает действительное положительное число x и целое отрицательное число y
# необходимо выполнить возведение числа x в степень y
# задание необходимо реализовать в виде функции my_func(x, y)
# при решении задания необходимо обойтись без встроенной функции возведения числа в степень
# ** Подсказка:** попробуйте решить задачу двумя способами
# первый — возведение в степень с помощью оператора **
# второй — более сложная реализация без оператора **, предусматривающая использование цикла

def chek_num(user_string):
    """ проверка на ввод чисел(+целые +дробные +отрицательные) """
    while True:
        try:
            user_chek = input(user_string)
            if user_chek.isdigit():
                user_chek = int(user_chek)
                return user_chek
            else:
                user_chek = float(user_chek)
                return user_chek
        except ValueError:
            print('\x1b[31mОшибка! Вводите только числа!\x1b[0m')
        continue


def my_exp_st(x, y):
    """ возведение в степень с помощью оператора **"""
    try:
        z = x ** y
        return z
    except OverflowError:
        return 'Компьютер не смог!'


def my_exp(x, y):
    """ возведение в степень с использованием цикла"""
    i, z = 1, x
    if y == 0:
        return 1
    while i < abs(y):
        z = z * x
        i += 1
    if y < 0:
        return 1 / z
    return z


user_float = chek_num('Введите действительное положительное число >>> ')
user_int = chek_num('Введите целое отрицательное число >>> ')

print('\n\x1b[34mВозведение в степень с помощью оператора ** >>>\x1b[0m',
      f'{my_exp_st(user_float, user_int)}')
print('\x1b[34mВозведение в степень с использованием цикла >>>\x1b[0m',
      f'{my_exp(user_float, user_int)}')
