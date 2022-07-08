def greater_next(some_list):
    for i in range(1, len(some_list)):
        if some_list[i] > some_list[i-1]:
            yield some_list[i]


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Полученный список:', end=' ')
print(list(greater_next(my_list)))