def my_fync_1(x, y):
    return x ** y


def my_fync_2(x, y):
    result = 1
    for i in range(0, abs(y)):
        result /= x
    return result


loyal_x = False
loyal_y = False
x = None
y = None
while not loyal_x or not loyal_y:
    if x and y:
        print('Ошибка вовода')
    if not loyal_x:
        x = float(input('Введите действительное положительное число: '))
    if not loyal_y:
        y = int(input('Введите целое отрицательное число: '))
    loyal_x = x > 0
    loyal_y = y < 0

print(f'Результат вычисления, вариант 1: {my_fync_1(x, y)}')
print(f'Результат вычисления, функции 2: {my_fync_2(x, y)}')
