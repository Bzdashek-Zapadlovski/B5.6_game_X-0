def greeting():
    print("----------------------")
    print("         ИГРА         ")
    print("                      ")
    print("    крестики-нолики   ")
    print("----------------------")
    print("      введите: x y    ")
    print("   x - номер строки   ")
    print("   y - номер столбца  ")

playing_field = [[" "] * 3 for i in range(3)]
def field_image():
    print()
    print("     | 0 | 1 | 2 |")
    print(" ----------------")
    for a, row in enumerate(playing_field):
        row_str = f"   {a} | {' | '.join(row)} | "
        print(row_str)
        print(" ----------------")
    print()

def motion():
    while True:
        coordinates = input("     Можете ходить:   ").split()

        if len(coordinates) != 2:
            print("  Введите пожалуйста две координаты!  ")
            continue

        x, y = coordinates

        if not(x.isdigit()) or not(y.isdigit()):
            print("  Введите пожалуйста числа!   ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("  Указанные координаты находятся за пределами игрового поля!  ")
            continue

        if playing_field[x][y] != " ":
            print("   Данную клетку кто-то занял до Вас!  ")
            continue

        return x, y

def check_win():
    win_coordinates = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                       ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                       ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)))
    for coordinates in win_coordinates:
        symbols = []

        for z in coordinates:
            symbols.append(playing_field[z[0]][z[1]])

        if symbols == ["X", "X", "X"]:
            print("  Победу одержал игрок который ставит крестики!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("  Победу одержал игрок который ставит нолики!!!")
            return True
    return False

greeting()

move = 0
while True:
    move += 1
    field_image()
    if move % 2 == 1:
        print("  Сейчас ходит игрок который ставит крестики  ")
    else:
        print("  Сейчас ходит игрок который ставит нолики  ")

    x, y = motion()

    if move % 2 == 1:
        playing_field[x][y] = "X"
    else:
        playing_field[x][y] = "0"

    if check_win():
        break

    if move == 9:
        print("   Победила дружба!!!   ")
        break