# Задание 1

a = 5
b = 8
print('a =', a, '\nb =', b)
c = int(input('В какую степень возвести? - '))
print(a, 'в степени', c, ' = ', a ** c, '\n', b, 'в степени', c, ' = ', b ** c)

# Задание 2

add_mi_sec = int(input('Введите время в секундах - '))
mi_sec = add_mi_sec % 60
mi_minute = add_mi_sec % 3600 // 60
mi_hour = add_mi_sec // 3600
print('%02d:%02d:%02d' % (mi_hour, mi_minute, mi_sec))

# Задание 3

n = input('Введите число - ')
a = int(n)
b = int(n + n)
c = int(n + n + n)
print(a + b + c)

# Задание 4

a = int(input('Введите целое положительное число - '))
b = a % 10
c = a // 10
while c > 0:
    if c % 10 > b:
        b = c % 10
    c = c // 10
print('Наибольшая цифра в числе:', a, "=", b)

# Задание 5

mi_revenue = int(input('Введите значение выручки - '))
mi_costs = int(input('Введите значение издержек - '))

if mi_revenue > mi_costs:
    print('Ваша фирма является прибыльной!')
else:
    print('Ваша фирма является убыточной!')

# Задание 6

mi_revenue = int(input('Введите значение выручки - '))
mi_costs = int(input('Введите значение издержек - '))

if mi_revenue > mi_costs:
    mi_profit = mi_revenue - mi_costs
    mi_profitability_revenue = mi_profit / mi_revenue * 100
    print('Ваша фирма является прибыльной!', '\nРентабельность составит -', '%.2f' % mi_profitability_revenue, '%')
    num_employees = int(input('Сколько у Вас сотрудников? - '))
    mi_profit_employees = mi_profit / num_employees
    print('Прибыль на одного сотрудника составит -', '%.2f' % mi_profit_employees, 'тубриков')
else:
    print('Ваша фирма является убыточной!')

# Задание 7

a = 5
b = 56
day_counter = 0

while a < b:
    a = a * 0.1 + a
    day_counter += 1
    print(day_counter, '- й день:', '%.2f' % a)
