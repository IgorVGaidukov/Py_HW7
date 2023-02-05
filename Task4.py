"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    is_police = 'нет'

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина едет', direction)

    def show_speed(self):
        print(f'Текущая скорость = {self.speed}')


class TownCar(Car):

    def show_speed(self):
        print(f'Текущая скорость = {self.speed}')
        if self.speed > 60:
            print(f'Вы превышаете скорость 60 км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'Текущая скорость = {self.speed}')
        if self.speed > 40:
            print(f'Вы превышаете скорость 40 км/ч!')


class PoliceCar(Car):
    is_police = 'да'


car1 = TownCar(80, 'белый', 'Volvo')
print(type(car1))
print(
    f'скорость: {car1.speed}, цвет: {car1.color}, название: {car1.name}, полиция: {car1.is_police}'
)
car1.go()
car1.show_speed()
car1.turn('вправо')
car1.stop()

car2 = SportCar(120, 'красный', 'Ferrari')
print(f'\n{type(car2)}')
print(
    f'скорость: {car2.speed}, цвет: {car2.color}, название: {car2.name}, полиция: {car2.is_police}'
)
car2.go()
car2.show_speed()
car2.turn('влево')
car2.stop()

car3 = WorkCar(40, 'желтый', 'GAZ')
print(f'\n{type(car3)}')
print(
    f'скорость: {car3.speed}, цвет: {car3.color}, название: {car3.name}, полиция: {car3.is_police}'
)
car3.go()
car3.show_speed()
car3.turn('прямо')
car3.stop()

car4 = PoliceCar(90, 'синий', 'Ford')
print(f'\n{type(car4)}')
print(
    f'скорость: {car4.speed}, цвет: {car4.color}, название: {car4.name}, полиция: {car4.is_police}'
)
car4.go()
car4.show_speed()
car4.turn('прямо')
car4.stop()