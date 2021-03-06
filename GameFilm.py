import sys
from Film import Film
import Cartoon
import Documentary


class GameFilm(Film):
    def __init__(self):
        super().__init__()
        self.director = ""

    def read_from(self, stream):
        try:
            self.title = stream.readline().rstrip("\n")
            self.director = stream.readline().rstrip("\n")
            self.country = stream.readline().rstrip("\n")
        except Exception as e:
            print("Game movie data read error.")
            print(e)
            stream.close()
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f"Игровой фильм.\n"
                         f"\tНазвание: {self.title}\n"
                         f"\tРежиссер: {self.director}\n")
            stream.write(f"\tСтрана: {self.country}\n")
        except Exception as e:
            stream.close()
            print("Ошибка чтения игрового фильма!")
            print(e)
            sys.exit(1)

    def write_game_film_to(self, stream):
        try:
            self.write_to(stream)
            stream.write(f"\tКоличество гласных: {self.num_vowels()}\n")
        except Exception as e:
            stream.close()
            print("Ошибка записи игрового фильма!")
            print(e)
            sys.exit(1)

    def check_filmsM(self, film_2):
        if type(film_2) == Documentary.Documentary:
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Игровой, второй фильм: Документальный")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
        if type(film_2) == Cartoon.Cartoon:
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Игровой, второй фильм: Мультфильм")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
        if type(film_2) == GameFilm:
            print("Фильмы из одной категории.")
            print("Категория - первый фильм: Игровой, второй фильм: Игровой")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
