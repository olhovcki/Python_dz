def sum_number(number):
    amount_number = 0
    for i in number:
        if i.lower() == 'n':
            return amount_number, True
        try:
            amount_number += int(i)
        except TypeError:
            continue
    return amount_number, False


stop = False
result = 0
while not stop:
    tmp, stop = sum_number(
        str(input('Введите числа, разделенные пробелом или N для выхода: ')).split()
    )
    result += tmp
    print(f'Промежуточный результат: {result}')

print(f'Результат: {result}')
