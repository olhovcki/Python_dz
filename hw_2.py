class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calc(self, weight_pm: int = 120, depth: int = 1):
        return self._width * self._length * weight_pm * depth


road = Road(5000, 20)
print(road.calc())
