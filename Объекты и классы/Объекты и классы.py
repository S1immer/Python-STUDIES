# Создание класса
from pickle import PROTO


class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car stopped")


my_car = Car()
print(dir(my_car))

my_car.move()































# class Person:
#     """Класс для представления человека."""
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f"Имя: {self.name}")
#         print(f"Возраст: {self.age}")
#
#
# # Создаем объект класса Person
# john = Person("Джон", 30)
#
# # Вызываем метод объекта
# john.print_info()