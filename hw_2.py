with open('test2.txt', 'r', encoding='utf-8') as f:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
    print(*usefulness, f'всего строк - {len(usefulness)}.', sep='\n')
