def my_func(a, b, c):
    my_sum = [a, b, c]
    my_sum.remove(min(my_sum))
    return sum(my_sum)


a = int(input('Введите первое число - '))
b = int(input('Введите первое число - '))
c = int(input('Введите первое число - '))

print(my_func(a, b, c))
