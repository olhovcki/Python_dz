from random import randint

with open('test5.txt', mode='w+', encoding='utf-8') as f:
    f.write(" ".join([str(randint(1, 500)) for _ in range(10000)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))
