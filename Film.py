class Film:
    def __init__(self):
        self.title = ""

    def read_from(self, stream):
        pass

    def write_to(self, stream):
        pass

    @staticmethod
    def create_from(stream, line):

        k = int(line)

        match k:
            case 1:
                from GameFilm import GameFilm
                film = GameFilm()

            case 2:
                from Cartoon import Cartoon
                film = Cartoon()

            case _:
                stream.close()
                raise Exception("Error type!")

        film.read_from(stream)
        return film

    def num_vowels(self):
        vowels = set("aeiouауоыиэяюёеAEIOUАУОЫИЭЯЮЁЕ")
        amount = 0
        for letter in self.title:
            if letter in vowels:
                amount += 1
        return amount
