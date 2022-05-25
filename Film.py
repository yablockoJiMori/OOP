import sys


class Film:
    def __init__(self):
        self.title = ""
        self.country = ""

    def read_from(self, stream):
        pass

    def write_to(self, stream):
        pass

    def write_game_film_to(self, stream):
        pass

    def check_filmsM(self, film_2):
        pass

    @staticmethod
    def create_from(stream, line):
        try:
            k = int(line)
        except Exception as e:
            print(f"Ошибка преобразования числа. ({line})")
            print(e)
            stream.close()
            sys.exit(1)
        match k:
            case 1:
                from GameFilm import GameFilm
                film = GameFilm()

            case 2:
                from Cartoon import Cartoon
                film = Cartoon()

            case 3:
                from Documentary import Documentary
                film = Documentary()

            case _:
                stream.close()
                print(f"Введен неверный тип объекта: {k}")
                sys.exit(1)

        film.read_from(stream)
        return film

    def num_vowels(self):
        vowels = set("aeiouауоыиэяюёеAEIOUАУОЫИЭЯЮЁЕ")
        amount = 0
        for letter in self.title:
            if letter in vowels:
                amount += 1
        return amount

    def match(self, other):
        return self.num_vowels() < other.num_vowels()

    @staticmethod
    def check_film(film_1, film_2):
        film_1.check_filmsM(film_2)







