def int_fync(my_word):
    return my_word.title()


print(int_fync('прИвеТ'))

my_words = input('Введите строку: ').split()
print(*[int_fync(m)for m in my_words])
