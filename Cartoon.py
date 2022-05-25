import sys
from enum import Enum
from Film import Film
import Documentary
import GameFilm


class WayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3


class Cartoon(Film):
    def __init__(self):
        super().__init__()
        self.way_to_create = None

    def read_from(self, stream):
        try:
            self.title = stream.readline().rstrip("\n")
        except Exception as e:
            stream.close()
            print("Ошибка чтения мультфильма!")
            print(e)
            sys.exit(1)
        try:
            k = int(stream.readline())
        except Exception as e:
            print(f"Ошибка преобразования числа.")
            print(e)
            stream.close()
            sys.exit(1)

        match k:
            case WayToCreate.drawn.value:
                self.way_to_create = WayToCreate.drawn
            case WayToCreate.puppet.value:
                self.way_to_create = WayToCreate.puppet
            case WayToCreate.plasticine.value:
                self.way_to_create = WayToCreate.plasticine
            case _:
                stream.close()
                print(f"Введен неверный тип объекта: {k}")
                sys.exit(1)
        try:
            self.country = stream.readline().rstrip("\n")
        except Exception as e:
            stream.close()
            print("Ошибка чтения мультфильма!")
            print(e)
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f"Мультфильм.\n"
                         f"\tНазвание: {self.title}\n"
                         f"\tСпособ создания: ")
        except Exception as e:
            stream.close()
            print("Ошибка записи мультфильма!")
            print(e)
            sys.exit(1)
        try:
            k = self.way_to_create
        except Exception as e:
            print(f"Ошибка преобразования числа.")
            print(e)
            stream.close()
            sys.exit(1)

        match k:
            case WayToCreate.drawn:
                stream.write(f"Нарисованный\n")
            case WayToCreate.puppet:
                stream.write(f"Кукольный \n")
            case WayToCreate.plasticine:
                stream.write(f"Пластилиновый\n")
            case _:
                stream.close()
                print(f"Введен неверный тип объекта: {k}")
                sys.exit(1)
        try:
            stream.write(f"\tСтрана: {self.country}\n")
        except Exception as e:
            stream.close()
            print("Ошибка записи мультфильма!")
            print(e)
            sys.exit(1)

    def check_filmsM(self, film_2):
        if type(film_2) == Documentary.Documentary:
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Мультфильм, второй фильм: Документальный")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
        if type(film_2) == Cartoon:
            print("Фильмы из одной категории.")
            print("Категория - первый фильм: Мультфильм, второй фильм: Мультфильм")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
        if type(film_2) == GameFilm.GameFilm:
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Мультфильм, второй фильм: Игровой")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
