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

a = int(game_bord[2][3])
print(10 + a)



def mar(i, j):
    if game_bord[i][j] == " -12 ":
        if j == 0:
            i = i - 1
            j = j + 5
        else:
            j = j - 1
    elif game_bord[i][j] == " -2 ":
        if j == 0:
            i = i - 1
            j = j + 4
        elif j == 1:
            i = i - 1
            j = j + 5
        else:
            j = j - 2
    elif game_bord[i][j] == " -3 ":
        if j == 0 or j == 1 or j == 2:
            i = i - 1
            j = j + 3
        else:
            j = j - 3
    elif game_bord[i][j] == " -4 ":
        if j == 0 or j == 1 or j == 2 or j == 3:
            i = i - 1
            j = j + 2
        else:
            j = j - 4
    elif game_bord[i][j] == " -5 ":
        if j == 0 or j == 1 or j == 2 or j == 3 or j == 4:
            i = i - 1
            j = j + 1
        else:
            j = j - 5
    elif game_bord[i][j] == " -6 ":
        i = i - 1
    return i, j


# def pele(i, j):
#     if game_bord[i][j] == " -1 ":


while ask_to_play.lower() == "y":


    tas = random.randint(1,6)
    print("Your Tas: ", tas)

    for i in range(7):
            for j in range(6):
                if game_bord[i][j] == " || ":
                    game_bord[i][j] = " __ "
                    if tas + j > 5:
                        i = i + 1
                        j = j + tas - 6
                        i, j = mar(i, j)
                        game_bord[i][j] = " || "
                        break
                    else:
                        j = j + tas
                        i, j = mar(i, j)
                        game_bord[i][j] = " || "
                        break
            else:
                continue
            break




    for i in range(len(game_bord)):
        for j in range(len(game_bord[i])):
            print(game_bord[i][j], end=" ")
        print()


    ask_to_play = input("If you want to play again, type 'y': ")
