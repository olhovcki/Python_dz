def my_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Ошибка! Делить на 0 нельзя!')
        return


my_res = my_division(
    a=int(input('Введите первое число - ')),
    b=int(input('Введите второе число - '))
)

print(f'Результат = {my_res}')
