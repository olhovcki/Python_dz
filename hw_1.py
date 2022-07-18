import time
from itertools import cycle

Traffic_Signal = (
    ('RED', 7),
    ('YELLOW', 2),
    ('GREEN', 5),
)


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        for i in cycle(Traffic_Signal):
            self.__color = i[0]
            print(f'Цвет светофора: {self.__color} ожидайте: {i[1]} сек.')
            time.sleep(i[1])


tl = TrafficLight()
tl.running()
