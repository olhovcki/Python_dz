class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return '%s %s %s' % (self.position, self.name, self.surname)

    def get_total_income(self):
        try:
            return self._income['wage'] + self._income['bonus']
        except TypeError:
            print('Ошибка в отчете о доходах')
        return 0


worker_1 = Position('Ivan', 'Pupkin', 'Engineer', {"wage": 55000, "bonus": 15920})
print(worker_1.get_full_name())
print(f'Заработал в этом месяце: {worker_1.get_total_income()} рублей')
