import sys
from Film import Film
import Cartoon
import GameFilm


class Documentary(Film):
    def __init__(self):
        super().__init__()
        self.year_of_issue = 0

    def read_from(self, stream):
        try:
            self.title = stream.readline().rstrip("\n")
            self.year_of_issue = int(stream.readline())
            self.country = stream.readline().rstrip("\n")
        except Exception as e:
            stream.close()
            print("Ошибка чтения документального фильма!")
            print(e)
            sys.exit(1)

    def write_to(self, stream):
        try:
            stream.write(f"Документальный фильм.\n"
                         f"\tНазвание: {self.title}\n"
                         f"\tГод создания: {self.year_of_issue}\n")
            stream.write(f"\tСтрана: {self.country}\n")
        except Exception as e:
            stream.close()
            print("Ошибка записи документального фильма!")
            print(e)
            sys.exit(1)

    def check_filmsM(self, film_2):
        if type(film_2) == Documentary:
            print("Фильмы из одной категории.")
            print("Категория - первый фильм: Документальный, второй фильм: Документальный")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
        if type(film_2) == Cartoon.Cartoon:
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Документальный, второй фильм: Мультфильм")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
        if type(film_2) == GameFilm.GameFilm:
            print("Фильмы из разных категорий.")
            print("Категория - первый фильм: Документальный, второй фильм: Игровой")
            print(f"Название - первый фильм: {self.title}, второй фильм: {film_2.title}")
            print()
