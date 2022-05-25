import sys
from Film import Film


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
