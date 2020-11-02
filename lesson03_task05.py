# >>>программа запрашивает у пользователя строку чисел, разделенных пробелом,
# при нажатии Enter должна выводиться сумма чисел
# >>>пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter,
# сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме
# >>>но если вместо числа вводится специальный символ, выполнение программы завершается
# если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу

def my_func(user_str):
    """ сложение чисел введенных в строке, выход по спец символам """
    my_bool = True
    result_sum = 0
    while my_bool:
        str_list = input(user_str).split()
        user_sum \
            = 0.0
        for i in range(len(str_list)):
            if str_list[i] == 'q' or str_list[i] == 'й':
                my_bool = False
                break
            elif str_list[i].isdigit():
                user_sum = user_sum + float(str_list[i])
            elif not str_list[i].isdigit():
                try:
                    user_sum = user_sum + float(str_list[i])
                except ValueError:
                    print("\x1b[31m", 'Ошибка! Вводите только числа!', "\x1b[0m")
                    continue
        result_sum = result_sum + user_sum
        print('Текущая сумма >>> ', result_sum)
    return result_sum


print('\n\x1b[34mИтоговая сумма всех числовых строк >>>\x1b[0m',
      my_func('Введите числа через пробел(завершить: "q" или "и") >>> '))
