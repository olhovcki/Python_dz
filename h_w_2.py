list_s = list(input('Введите любую строку: '))
print(list_s)
list_s[:-1:2], list_s[1::2] = list_s[1::2], list_s[:-1:2]
print(list_s)