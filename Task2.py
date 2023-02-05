"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    mass = 0
    thickness = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return self._width * self._length * self.mass * self.thickness


my_road = Road(5000, 20)
my_road.mass = 25
my_road.thickness = 0.05
total_mass = my_road.calc()

print(
    f'Необходимая масса асфальта: {my_road._width}м*{my_road._length}м*{my_road.mass}кг*{my_road.thickness}м = {total_mass:.0f} кг = {total_mass*0.001:.0f} т'
)
