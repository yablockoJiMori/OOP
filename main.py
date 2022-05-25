import sys

from DList import DList

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Ошибка. Ожидалось принять файлы ввода и вывода.")
        sys.exit(1)

    print("Старт")

    try:
        with open(sys.argv[2], "w", encoding="utf-8") as file_out:
            print("Файл output.txt отчищен.")
    except Exception as e:
        print(f"Ошибка открытия файла {sys.argv[2]}")
        print(e)
        sys.exit(1)

    container = DList()
    container.read_from(sys.argv[1])

    print("Файл прочитан.")

    container.sort()
    container.write_to(sys.argv[2])
    container.write_game_film_to(sys.argv[2])
    container.clear()

    print("Контейнер отчищен")
    container.write_to(sys.argv[2])

    print("Стоп.")



