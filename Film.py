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

            case 3:
                from Documentary import Documentary
                film = Documentary()

            case _:
                stream.close()
                raise Exception("Error type!")

        film.read_from(stream)
        return film
