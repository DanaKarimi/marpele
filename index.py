import random


ask_to_play = "y"

game_bord = [
    [" ||| ", " ___ ", " +12 ", " ___ ", " ___ ", " ___ "],
    [" ___ ", " ___ ", " ___ ", " ___ ", " ___ ", " ___ "],
    [" +13 ", " ___ ", " ___ ", " -12 ", " ___ ", " ___ "],
    [" +11 ", " ___ ", " ___ ", " ___ ", " ___ ", " ___ "],
    [" ___ ", " ___ ", " ___ ", " -26 ", " ___ ", " ___ "],
    [" ___ ", " ___ ", " ___ ", " ___ ", " ___ ", " ___ "],
    [" ___ ", " -17 ", " ___ ", " ___ ", " ___ ", " ___ "],
]

for i in range(len(game_bord)):
    for j in range(len(game_bord[i])):
        print(game_bord[i][j], end=" ")
    print()


def Mar_va_Pele(i, j) -> int:
    if game_bord[i][j] != " ___ " and game_bord[i][j] != " ||| ":
        a = int(game_bord[i][j])
        c = j
        if a < 0:
            if a < -6:
                if a < -12:
                    if a < -18:
                        if a < -24:
                            i = i - 1
                            a = a + 6
                        i = i - 1
                        a = a + 6
                    i = i - 1
                    a = a + 6
                i = i - 1
                a = a + 6
            j = j + a
            if j < 0:
                i = i - 1
                j = c + (6 + j)
        elif a > 0:
            if a > 6:
                if a > 12:
                    if a > 18:
                        if a > 24:
                            i = i + 1
                            a = a - 6
                        i = i + 1
                        a = a - 6
                    i = i + 1
                    a = a - 6
                i = i + 1
                a = a - 6
            j = j + a
            if j > 5:
                i = i + 1
                j = c + (j - 6)
    return i, j


while ask_to_play.lower() == "y":

    tas = random.randint(1,6)
    print("Your Tas: ", tas)

    for i in range(7):
            for j in range(6):
                if game_bord[i][j] == " ||| ":
                    if i == 6:
                        if j == 0 and tas > 5:
                            print("You shod play again!..")
                            break
                        elif j == 1 and tas > 4:
                            print("You shod play again!..")
                            break
                        elif j == 2 and tas > 3:
                            print("You shod play again!..")
                            break
                        elif j == 3 and tas > 2:
                            print("You shod play again!..")
                            break
                        elif j == 4 and tas > 1:
                            print("You shod play again!..")
                            break
                    game_bord[i][j] = " ___ "
                    if tas + j > 5:
                        i = i + 1
                        j = j + tas - 6
                        i, j = Mar_va_Pele(i, j)
                        game_bord[i][j] = " ||| "
                        break
                    else:
                        j = j + tas
                        i, j = Mar_va_Pele(i, j)
                        game_bord[i][j] = " ||| "
                        break

            else:
                continue
            break




    for i in range(len(game_bord)):
        for j in range(len(game_bord[i])):
            print(game_bord[i][j], end=" ")
        print()

    for i in range(7):
            for j in range(6):
                if game_bord[i][j] == " ||| ":
                    if i == 6 and j == 5:
                        print("You Win..")
                        break
            else:
                continue
            break
    ask_to_play = input("If you want to play again, type 'y': ")
