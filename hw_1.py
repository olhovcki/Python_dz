from sys import argv

try:
    script_name, hours, bid, award = argv
    print(f'Результат работы скрипта - {script_name} =', (float(hours) * float(bid)) + float(award))
except TypeError:
    print('Error!')
except ValueError:
    print('Error!')