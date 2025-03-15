import pygame

save = [0,0,0,0,0,0,0,0,0]

barva = "w"
start = [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " "," ", " ", " "], [" ", " "," ", " "," ", " "," "," "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " "," ", " ", " "], [" "," "," "," "," "," "," "," "]
hitboxw = ["ro", "kn", "bi", "qu", "pa"]
hitboxč = ["r", "n", "b", "q", "p"]
kralbox = ["k", "ki"]

running = True
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

WIDTH = 480
HEIGHT = int(WIDTH)
SQ_SIZE = WIDTH // 8
pygame.display.set_caption("šachy")
pygame_icon = pygame.image.load('ki.png')
pygame.display.set_icon(pygame_icon)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pieces_images = {
    "ro": pygame.image.load("ro.png"),
    "kn": pygame.image.load("kn.png"),
    "bi": pygame.image.load("bi.png"),
    "qu": pygame.image.load("qu.png"),
    "ki": pygame.image.load("ki.png"),
    "pa": pygame.image.load("pa.png"),
    "r": pygame.image.load("r.png"),
    "n": pygame.image.load("n.png"),
    "b": pygame.image.load("b.png"),
    "q": pygame.image.load("q.png"),
    "k": pygame.image.load("k.png"),
    "p": pygame.image.load("p.png")
}

pole = [
    ["ro", "kn", "bi", "qu", "ki", "bi", "kn", "ro"],
    ["pa", "pa", "pa", "pa", "pa", "pa", "pa", "pa"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "k", "q", "b", "n", "r"]
]

blank = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]
]

def end():
    running = True
    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                X, Y = get_clicked_square(mouse_pos)
                if 0 <= X < 8 and 0 <= Y < 8:
                    #print(X, x, Y, y)
                    running = False
    global poles
    global save
    global barva
    pole = [
    ["ro", "kn", "bi", "qu", "ki", "bi", "kn", "ro"],
    ["pa", "pa", "pa", "pa", "pa", "pa", "pa", "pa"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "k", "q", "b", "n", "r"]
    ]
    save = [0,0,0,0,0,0,0,0,1]
    barva ="w"
    draw_board(screen, save)

def check(board, blank):
    blank = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]
    ]
    sum = 1
    for row in range(8):
        for col in range(8):
            if board[row][col] == "ro":
                try:
                    while row + sum < 8:
                        if row + sum > 8:
                            break
                        if board[row + sum][col] == " ":
                            blank[row + sum][col] = "X"
                            sum += 1
                        elif board[row + sum][col] == "k":
                            blank[row + sum][col] = "X"
                            break
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8:
                        if row - sum < 0:
                            break
                        if board[row - sum][col] == " ":
                            blank[row - sum][col] = "X"
                            sum += 1
                        elif board[row - sum][col] == "k":
                            blank[row - sum][col] = "X"
                            break
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while col - sum < 8:
                        if col - sum < 0:
                            break
                        if board[row][col - sum] == " ":
                            blank[row][col - sum] = "X"
                            sum += 1
                        elif board[row][col - sum] == "k":
                            blank[row][col - sum] = "X"
                            break
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while col + sum < 8:
                        if col + sum > 8:
                            break
                        if board[row][col + sum] == " ":
                            blank[row][col + sum] = "X"
                            sum += 1
                        elif board[row][col + sum] == "k":
                            blank[row][col + sum] = "X"
                            break
                        else:
                            break
                except:
                    pass
            elif board[row][col] == "kn":
                try:
                    if board[row + 2][col + 1] == " " or board[row + 2][col + 1] == "k":
                        if row < 6 and col < 7:
                            blank[row + 2][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row + 2][col - 1] == " " or board[row + 2][col - 1] == "k":
                        if col != 0 and row < 6:
                            blank[row + 2][col - 1] = "X"
                except:
                    pass
                try:
                    if board[row - 2][col + 1] == " " or board[row - 2][col + 1] == "k":
                        if row > 1 and col < 7:
                            blank[row - 2][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row - 2][col - 1] == " " or board[row - 2][col - 1] == "k":
                        if row > 1 and col != 0:
                            blank[row - 2][col - 1] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col + 2] == " " or board[row + 1][col + 2] == "k":
                        if row < 7 and col < 6:
                            blank[row + 1][col + 2] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col - 2] == " " or board[row + 1][col - 2] == "k":
                        if row < 7 and col > 1:
                            blank[row + 1][col - 2] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col + 2] == " " or board[row - 1][col + 2] == "k":
                        if row != 0 and col < 6:
                            blank[row - 1][col + 2] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col - 2] == " " or board[row - 1][col - 2] == "k":
                        if row != 0 and col > 1:
                            blank[row - 1][col - 2] = "X"
                except:
                    pass
            elif board[row][col] == "pa":
                try:
                    if board[row + 1][col + 1] == " " or board[row + 1][col + 1] == "k":
                        blank[row + 1][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col - 1] == " " or board[row + 1][col - 1] == "k":
                        blank[row + 1][col - 1] = "X"
                except:
                    pass
            elif board[row][col] == "ki":
                try:
                    if board[row + 1][col] == " " or board[row + 1][col] == "k":
                        if row != 7:
                            blank[row + 1][col] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col] == " " or board[row - 1][col] == "k":
                        if row != 0:
                            blank[row - 1][col] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col + 1] == " " or board[row + 1][col + 1] == "k":
                        if row != 7 and col != 7:
                            blank[row + 1][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col - 1] == " " or board[row + 1][col - 1] == "k":
                        if row != 7 and col != 0:
                            blank[row + 1][col - 1] = "X"
                except:
                    pass
                try:
                    if board[row][col + 1] == " " or board[row][col + 1] == "k":
                        if col != 7:
                            blank[row][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row][col - 1] == " " or board[row][col - 1] == "k":
                        if col != 0:
                            blank[row][col - 1] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col + 1] == " " or board[row - 1][col + 1] == "k":
                        if row != 0 and col != 7:
                            blank[row - 1][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col - 1] == " " or board[row - 1][col - 1] == "k":
                        if row != 0 and col != 0:
                            blank[row - 1][col - 1] = "X"
                except:
                    pass
            elif board[row][col] == "bi":
                sum = 1
                try:
                    while row + sum < 8 and col + sum < 8:
                        if row + sum > 8 or col + sum > 8:
                            break
                        if pole[row + sum][col + sum] == " " or pole[row + sum][col + sum] == "k":
                            blank[row + sum][col + sum] = "X"
                            if pole[row + sum][col + sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row + sum < 8 and col - sum < 8:
                        if row + sum > 8 or col - sum < 0:
                            break
                        if pole[row + sum][col - sum] == " " or pole[row + sum][col - sum] == "k":
                            blank[row + sum][col - sum] = "X"
                            if pole[row + sum][col - sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8 and col + sum < 8 or pole[row - sum][col + sum] == "k":
                        if row - sum < 0 or col + sum > 8:
                            break
                        if pole[row - sum][col + sum] == " ":
                            blank[row - sum][col + sum] = "X"
                            if pole[row - sum][col + sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8 and col - sum < 8:
                        if row - sum < 0 or col - sum < 0:
                            break
                        if pole[row - sum][col - sum] == " " or pole[row - sum][col - sum] == "k":
                            blank[row - sum][col - sum] = "X"
                            if pole[row - sum][col - sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
            elif board[row][col] == "qu":
                sum = 1
                try:
                    while row + sum < 8 and col + sum < 8:
                        if pole[row + sum][col + sum] == " " or pole[row + sum][col + sum] == "k":
                            blank[row + sum][col + sum] = "X"
                            if pole[row + sum][col + sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row + sum < 8 and col - sum < 8 or pole[row + sum][col - sum] == "k":
                        if col - sum < 0:
                            break
                        if pole[row + sum][col - sum] == " ":
                            blank[row + sum][col - sum] = "X"
                            if pole[row + sum][col - sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8 and col + sum < 8:
                        if row - sum < 0:
                            break
                        if pole[row - sum][col + sum] == " " or pole[row - sum][col + sum] == "k":
                            blank[row - sum][col + sum] = "X"
                            if pole[row - sum][col + sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8 and col - sum < 8 or pole[row - sum][col - sum] == "k":
                        if col - sum < 0 or row - sum < 0:
                            break
                        if pole[row - sum][col - sum] == " ":
                            blank[row - sum][col - sum] = "X"
                            if pole[row - sum][col - sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row + sum < 8:
                        if board[row + sum][col] == " " or board[row + sum][col] == "k":
                            blank[row + sum][col] = "X"
                            if board[row + sum][col] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8:
                        if row - sum < 0:
                            break
                        if board[row - sum][col] == " " or board[row - sum][col] == "k":
                            blank[row - sum][col] = "X"
                            if board[row - sum][col] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while col - sum < 8:
                        if col - sum < 0:
                            break
                        if board[row][col - sum] == " " or board[row][col - sum] == "k":
                            blank[row][col - sum] = "X"
                            if board[row][col - sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while col + sum < 8:
                        if board[row][col + sum] == " " or board[row][col + sum] == "k":
                            blank[row][col + sum] = "X"
                            if board[row][col + sum] == "k":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
    found = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == "k":
                found = 1
                break
        if found == 1:
            break
        else:
            pass
    count = 0
    try:
        if blank[row + 1][col] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row + 1][col - 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row + 1][col + 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row][col + 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row][col - 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row - 1][col + 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row - 1][col - 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row - 1][col] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row][col] == "X":
            count += 1
    except:
        pass
    #print(save[6], "savevee")
    if blank[row][col] == "X":
        save [0], save[1], save[2] = 1, col, row
        if save[6] == 1:
            save[6] = 2
        elif save[6] == 0:
            save[6] = 1
    elif row == 0 or row == 7:
        if col == 0 or col == 7:
            if count == 4:
                save [0], save[1], save[2] = 2, col, row
                if save[6] == 1:
                    save[6] = 2
                elif save[6] == 0:
                    save[6] = 1
        else:
            if count == 6:
                save [0], save[1], save[2] = 2, col, row
                if save[6] == 1:
                    save[6] = 2
                elif save[6] == 0:
                    save[6] = 1
    elif col == 0 or col == 7:
        if row == 0 or row == 7:
            if count == 4:
                save [0], save[1], save[2] = 2, col, row
                if save[6] == 1:
                    save[6] = 2
                elif save[6] == 0:
                    save[6] = 1
        else:
            if count == 6:
                save [0], save[1], save[2] = 2, col, row
                if save[6] == 1:
                    save[6] = 2
                elif save[6] == 0:
                    save[6] = 1
    elif count == 9:
        save [0], save[1], save[2] = 2, col, row
        if save[6] == 1:
            save[6] = 2
        elif save[6] == 0:
            save[6] = 1
    else:
        save[6] = 0
    #for i in range(8):
        #print(blank[i])
    #print("")
    #print(save[6], "save")
    #print("")
    blank = [
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "]
    ]
    #print(" ")
    #for i in range(8):
    #    print(board[i])
    #print(" ")
    #for i in range(8):
    #    print(blank[i])
    sum = 1
    for row in range(8):
        for col in range(8):
            if board[row][col] == "r":
                try:
                    while row + sum < 8:
                        if board[row + sum][col] == " " or board[row + sum][col] == "ki":
                            blank[row + sum][col] = "X"
                            if board[row + sum][col] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8:
                        if row - sum < 0:
                            break
                        if board[row - sum][col] == " " or board[row - sum][col] == "ki":
                            blank[row - sum][col] = "X"
                            if board[row - sum][col] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while col - sum < 8:
                        if col - sum < 0:
                            break
                        if board[row][col - sum] == " " or board[row][col - sum] == "ki":
                            blank[row][col - sum] = "X"
                            if board[row][col - sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while col + sum < 8:
                        if board[row][col + sum] == " " or board[row][col + sum] == "ki":
                            blank[row][col + sum] = "X"
                            if board[row][col + sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
            elif board[row][col] == "n":
                try:
                    if board[row + 2][col + 1] == " " or board[row + 2][col + 1] == "ki":
                        if row < 6 and col < 7:
                            blank[row + 2][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row + 2][col - 1] == " " or board[row + 2][col - 1] == "ki":
                        if row < 6 and col > 0:
                            blank[row + 2][col - 1] = "X"
                except:
                    pass
                try:
                    if board[row - 2][col + 1] == " " or board[row - 2][col + 1] == "ki":
                        if row > 1 and col < 7:
                            blank[row - 2][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row - 2][col - 1] == " " or board[row - 2][col - 1] == "ki":
                        if row > 1 and col > 0:
                            blank[row - 2][col - 1] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col + 2] == " " or board[row + 1][col + 2] == "ki":
                        if row < 7 and col < 6:
                            blank[row + 1][col + 2] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col - 2] == " " or board[row + 1][col - 2] == "ki":
                        if row < 7 and col > 1:
                            blank[row + 1][col - 2] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col + 2] == " " or board[row - 1][col + 2] == "ki":
                        if row > 0 and col < 6:
                            blank[row - 1][col + 2] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col - 2] == " " or board[row - 1][col - 2] == "ki":
                        if row > 0 and col > 1:
                            blank[row - 1][col - 2] = "X"
                except:
                    pass
            elif board[row][col] == "p":
                try:
                    if board[row - 1][col + 1] == " " or board[row + 1][col + 1] == "ki":
                        if row > 0 and col < 7:
                            blank[row - 1][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col - 1] == " " or board[row + 1][col - 1] == "ki":
                        if row > 0 and col > 0:
                            blank[row - 1][col - 1] = "X"
                except:
                    pass
            elif board[row][col] == "k":
                try:
                    if board[row + 1][col] == " " or board[row + 1][col] == "ki":
                        if row != 7:
                            blank[row + 1][col] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col] == " " or board[row - 1][col] == "ki":
                        if row != 0:
                            blank[row - 1][col] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col + 1] == " " or board[row + 1][col + 1] == "ki":
                        if row != 7 and col != 7:
                            blank[row + 1][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row + 1][col - 1] == " " or board[row + 1][col - 1] == "ki":
                        if row != 7 and col != 0:
                            blank[row + 1][col - 1] = "X"
                except:
                    pass
                try:
                    if board[row][col + 1] == " " or board[row][col + 1] == "ki":
                        if col != 7:
                            blank[row][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row][col - 1] == " " or board[row][col - 1] == "ki":
                        if col != 0:
                            blank[row][col - 1] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col + 1] == " " or board[row - 1][col + 1] == "ki":
                        if row != 0 and col != 7:
                            blank[row - 1][col + 1] = "X"
                except:
                    pass
                try:
                    if board[row - 1][col - 1] == " " or board[row - 1][col - 1] == "ki":
                        if row != 0 and col != 0:
                            blank[row - 1][col - 1] = "X"
                except:
                    pass
            elif board[row][col] == "b":
                sum = 1
                try:
                    while row + sum < 8 and col + sum < 8:
                        if row + sum > 8 or col + sum > 8:
                            break
                        if pole[row + sum][col + sum] == " " or pole[row + sum][col + sum] == "ki":
                            blank[row + sum][col + sum] = "X"
                            if pole[row + sum][col + sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row + sum < 8 and col - sum < 8:
                        if row + sum > 8 or col - sum < 0:
                            break
                        if pole[row + sum][col - sum] == " " or pole[row + sum][col - sum] == "ki":
                            blank[row + sum][col - sum] = "X"
                            if pole[row + sum][col - sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8 and col + sum < 8 or pole[row - sum][col + sum] == "ki":
                        if row - sum < 0 or col + sum > 8:
                            break
                        if pole[row - sum][col + sum] == " ":
                            blank[row - sum][col + sum] = "X"
                            if pole[row - sum][col + sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8 and col - sum < 8:
                        if row - sum < 0 or col - sum < 0:
                            break
                        if pole[row - sum][col - sum] == " " or pole[row - sum][col - sum] == "ki":
                            blank[row - sum][col - sum] = "X"
                            if pole[row - sum][col - sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
            elif board[row][col] == "q":
                sum = 1
                try:
                    while row + sum < 8 and col + sum < 8:
                        if pole[row + sum][col + sum] == " " or pole[row + sum][col + sum] == "ki":
                            blank[row + sum][col + sum] = "X"
                            if pole[row + sum][col + sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row + sum < 8 and col - sum < 8 or pole[row + sum][col - sum] == "ki":
                        if pole[row + sum][col - sum] == " ":
                            blank[row + sum][col - sum] = "X"
                            if pole[row + sum][col - sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8 and col + sum < 8:
                        if pole[row - sum][col + sum] == " " or pole[row - sum][col + sum] == "ki":
                            blank[row - sum][col + sum] = "X"
                            if pole[row - sum][col + sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8 and col - sum < 8 or pole[row - sum][col - sum] == "ki":
                        if pole[row - sum][col - sum] == " ":
                            blank[row - sum][col - sum] = "X"
                            if pole[row - sum][col - sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row + sum < 8:
                        if board[row + sum][col] == " " or board[row + sum][col] == "ki":
                            blank[row + sum][col] = "X"
                            if board[row + sum][col] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while row - sum < 8:
                        if board[row - sum][col] == " " or board[row - sum][col] == "ki":
                            blank[row - sum][col] = "X"
                            if board[row - sum][col] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while col - sum < 8:
                        if board[row][col - sum] == " " or board[row][col - sum] == "ki":
                            blank[row][col - sum] = "X"
                            if board[row][col - sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
                sum = 1
                try:
                    while col + sum < 8:
                        if board[row][col + sum] == " " or board[row][col + sum] == "ki":
                            blank[row][col + sum] = "X"
                            if board[row][col + sum] == "ki":
                                break
                            sum += 1
                        else:
                            break
                except:
                    pass
    found = 0
    for row in range(8):
        for col in range(8):
            if board[row][col] == "ki":
                found = 1
                break
        if found == 1:
            break
        else:
            pass
    count = 0
    try:
        if blank[row + 1][col] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row + 1][col - 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row + 1][col + 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row][col + 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row][col - 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row - 1][col + 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row - 1][col - 1] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row - 1][col] == "X":
            count += 1
    except:
        pass
    try:
        if blank[row][col] == "X":
            count += 1
    except:
        pass
    if blank[row][col] == "X":
        save[3], save[4], save[5] = 1, col, row
        if save[7] == 1:
            save[7] = 2
        elif save[7] == 0:
            save[7] = 1
    elif row == 0 or row == 7:
        if col == 0 or col == 7:
            if count == 4:
                save[3], save[4], save[5] = 2, col, row
                if save[7] == 1:
                    save[7] = 2
                elif save[7] == 0:
                    save[7] = 1
        else:
            if count == 6:
                save[3], save[4], save[5] = 2, col, row
                if save[7] == 1:
                    save[7] = 2
                elif save[7] == 0:
                    save[7] = 1
    elif col == 0 or col == 7:
        if row == 0 or row == 7:
            if count == 4:
                save[3], save[4], save[5] = 2, col, row
                if save[7] == 1:
                    save[7] = 2
                elif save[7] == 0:
                    save[7] = 1
        else:
            if count == 6:
                save[3], save[4], save[5] = 2, col, row
                if save[7] == 1:
                    save[7] = 2
                elif save[7] == 0:
                    save[7] = 1
    elif count == 9:
        save[3], save[4], save[5] = 2, col, row
        if save[7] == 1:
            save[7] = 2
        elif save[7] == 0:
            save[7] = 1
    else:
        save[7] = 0
    #print(save[3])
    #for i in range(8):
    #    print(blank[i])


def draw_board(screen, save):
    if save[8] == 1:
        global pole
        pole = [
        ["ro", "kn", "bi", "qu", "ki", "bi", "kn", "ro"],
        ["pa", "pa", "pa", "pa", "pa", "pa", "pa", "pa"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["r", "n", "b", "k", "q", "b", "n", "r"]
        ]
        save[8] = 0
    board = pole
    check(board, blank)
    for row in range(8):
        for col in range(8):
            color = LIGHT_GRAY if (row + col) % 2 == 0 else DARK_GRAY
            pygame.draw.rect(screen, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[row][col]
            if piece != ' ':
                piece_image = pygame.image.load(f"{piece}.png")
                piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                screen.blit(piece_image, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    if save[0] == 1:
        pygame.draw.rect(screen, (175,0,0), pygame.Rect(save[1] * SQ_SIZE, save[2] * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        piece = pole[save[2]][save[1]]
        piece_image = pygame.image.load(f"{piece}.png")
        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
        screen.blit(piece_image, pygame.Rect(save[1] * SQ_SIZE, save[2] * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        save[0], save[1], save[2] = 0, 0, 0
        if save[6] == 2:
            for row in range(8):
                for col in range(8):
                    piece = pole[col][row]
                    if piece in hitboxw:
                        pygame.draw.rect(screen, (0,255,0), pygame.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                        piece_image = pygame.image.load(f"{piece}.png")
                        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                        screen.blit(piece_image, pygame.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            end()
    elif save[0] == 2:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(save[1] * SQ_SIZE,save[2] * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        piece = pole[save[2]][save[1]]
        piece_image = pygame.image.load(f"{piece}.png")
        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
        screen.blit(piece_image, pygame.Rect(save[1] * SQ_SIZE, save[2] * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        save[0], save[1], save[2] = 0, 0, 0
        if save[6] == 2:
            for row in range(8):
                for col in range(8):
                    piece = pole[col][row]
                    if piece in hitboxw:
                        pygame.draw.rect(screen, (0,255,0), pygame.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                        piece_image = pygame.image.load(f"{piece}.png")
                        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                        screen.blit(piece_image, pygame.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            end()
    if save[3] == 1:
        pygame.draw.rect(screen, (175,0,0), pygame.Rect(save[4] * SQ_SIZE, save[5] * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        piece = pole[save[5]][save[4]]
        piece_image = pygame.image.load(f"{piece}.png")
        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
        screen.blit(piece_image, pygame.Rect(save[4] * SQ_SIZE, save[5] * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        save[3], save[4], save[5] = 0, 0, 0
        if save[7] == 2:
            for row in range(8):
                for col in range(8):
                    piece = pole[col][row]
                    if piece in hitboxč:
                        pygame.draw.rect(screen, (0,255,0), pygame.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                        piece_image = pygame.image.load(f"{piece}.png")
                        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                        screen.blit(piece_image, pygame.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            end()
    elif save[3] == 2:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(save[4] * SQ_SIZE, save[5] * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        piece = pole[save[5]][save[4]]
        piece_image = pygame.image.load(f"{piece}.png")
        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
        screen.blit(piece_image, pygame.Rect(save[4] * SQ_SIZE, save[5] * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        save[3], save[4], save[5] = 0, 0, 0
        if save[7] == 2:
            for row in range(8):
                for col in range(8):
                    piece = pole[col][row]
                    if piece in hitboxč:
                        pygame.draw.rect(screen, (0,255,0), pygame.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                        piece_image = pygame.image.load(f"{piece}.png")
                        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                        screen.blit(piece_image, pygame.Rect(row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            end()

def get_clicked_square(pos):
    row = pos[1] // SQ_SIZE
    col = pos[0] // SQ_SIZE
    return row, col


def bp(x, y, color):
    sum = 1
    while x + sum < 8 and y + sum < 8:
        if pole[x + sum][y + sum] == " ":
            pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            sum += 1
        elif pole[x + sum][y + sum] in hitboxč:
            pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[x + sum][y + sum]
            piece_image = pygame.image.load(f"{piece}.png")
            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
            screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            break
        else:
            break
    sum = 1
    while x - sum < 8 and y - sum < 8:
        if pole[x - sum][y - sum] == " ":
            pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            sum += 1
        elif pole[x - sum][y - sum] in hitboxč:
            pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[x - sum][y - sum]
            piece_image = pygame.image.load(f"{piece}.png")
            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
            screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            break
        else:
            break
    sum = 1
    while x + sum < 8 and y - sum < 8:
        if pole[x + sum][y - sum] == " ":
            pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            sum += 1
        elif pole[x + sum][y - sum] in hitboxč:
            pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[x + sum][y - sum]
            piece_image = pygame.image.load(f"{piece}.png")
            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
            screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            break
        else:
            break
    sum = 1
    while x - sum < 8 and y + sum < 8:
        if pole[x - sum][y + sum] == " ":
            pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            sum += 1
        elif pole[x - sum][y + sum] in hitboxč:
            pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[x - sum][y + sum]
            piece_image = pygame.image.load(f"{piece}.png")
            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
            screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            break
        else:
            break


def ro(x, y, color):
    sum = 1
    while x + sum < 8:
        if pole[x + sum][y] == " ":
            pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            sum += 1
        elif pole[x + sum][y] in hitboxč:
            pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[x + sum][y]
            piece_image = pygame.image.load(f"{piece}.png")
            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
            screen.blit(piece_image, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            break
        else:
            break
    sum = 1
    while y + sum < 8:
        if pole[x][y + sum] == " ":
            pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            sum += 1
        elif pole[x][y + sum] in hitboxč:
            pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[x][y + sum]
            piece_image = pygame.image.load(f"{piece}.png")
            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
            screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            break
        else:
            break
    sum = 1
    while x - sum > -1:
        if pole[x - sum][y] == " ":
            pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            sum += 1
        elif pole[x - sum][y] in hitboxč:
            pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[x - sum][y]
            piece_image = pygame.image.load(f"{piece}.png")
            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
            screen.blit(piece_image, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            break
        else:
            break
    sum = 1
    while y - sum > -1:
        #print(pole[x][y - sum])
        if pole[x][y - sum] == " ":
            pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            sum += 1
        elif pole[x][y - sum] in hitboxč:
            pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            piece = pole[x][y - sum]
            piece_image = pygame.image.load(f"{piece}.png")
            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
            screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            break
        else:
            break

def move(clicked_piece, x, y):
    global barva
    #print(barva)
    color = (255, 25, 25)
    sum = 1
    running = True
    if barva == "w":
        if clicked_piece == "ro":
            while x + sum < 8:
                if pole[x + sum][y] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while y + sum < 8:
                if pole[x][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x][y + sum] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum > -1:
                if pole[x - sum][y] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while y - sum > -1:
                #print(pole[x][y - sum])
                if pole[x][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x][y - sum] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            pygame.display.update()
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            okay = 0
            sum = 1
            # kontrola pohybu
            if X == x or Y == y:
                if x > X:
                    while x - sum != X:
                        if pole[x - sum][y] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x - sum][y] in hitboxč or pole[x - sum][y] in hitboxw:
                            if x - sum == X:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                elif x < X:
                    while x + sum != X:
                        if pole[x + sum][y] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x + sum][y] in hitboxč or pole[x + sum][y] in hitboxw:
                            if x + sum == X:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                elif y < Y:
                    while y + sum != Y:
                        if pole[x][y + sum] == " ":
                            sum += 1
                            okay = 0
                        if pole[x][y + sum] in hitboxč or pole[x][y + sum] in hitboxw:
                            if y + sum == Y:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                elif y > Y:
                    while y - sum != Y:
                        if pole[x][y - sum] == " ":
                            sum += 1
                            okay = 0
                        if pole[x][y - sum] in hitboxč or pole[x][y - sum] in hitboxw:
                            if y - sum == Y:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                draw_board(screen, save)
                if okay == 0:
                    if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                        draw_board(screen, save)
                    else:
                        pole[x][y] = " "
                        pole[X][Y] = "ro"
                        barva = "b"
                    # print(pole[0], "\n", pole[1], "\n", pole[2], "\n", pole[3], "\n", pole[4], "\n", pole[5], "\n", pole[6], "\n", pole[7])
                    draw_board(screen, save)
            else:
                draw_board(screen, save)
        elif clicked_piece == "bi":
            while x + sum < 8 and y + sum < 8:
                if pole[x + sum][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y + sum] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum < 8 and y - sum < 8:
                if pole[x - sum][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y - sum] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x + sum < 8 and y - sum < 8:
                if pole[x + sum][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y - sum] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum < 8 and y + sum < 8:
                if pole[x - sum][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y + sum] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            pygame.display.update()
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            sum = 1
            okay = 0
            if x < X and y < Y:
                while x + sum != X or y + sum != Y:
                    if pole[x + sum][y + sum] == " ":
                        sum += 1
                        okay = 0
                    elif pole[x + sum][y + sum] in hitboxč or pole[x + sum][y + sum] in hitboxw:
                        if y + sum == Y and x + sum == X:
                            draw_board(screen, save)
                            break
                        else:
                            okay = 1
                            draw_board(screen, save)
                            break
            elif x > X and y < Y:
                while x - sum != X or y + sum != Y:
                    if pole[x - sum][y + sum] == " ":
                        sum += 1
                        okay = 0
                    elif pole[x - sum][y + sum] in hitboxč or pole[x - sum][y + sum] in hitboxw:
                        if y + sum == Y and x - sum == X:
                            draw_board(screen, save)
                            break
                    else:
                        okay = 1
                        draw_board(screen, save)
                        break
            elif x > X and y > Y:
                while x - sum != X or y - sum != Y:
                    if pole[x - sum][y - sum] == " ":
                        sum += 1
                        okay = 0
                    elif pole[x - sum][y - sum] in hitboxč or pole[x - sum][y - sum] in hitboxw:
                        if y - sum == Y and x - sum == X:
                            draw_board(screen, save)
                            break
                    else:
                        okay = 1
                        draw_board(screen, save)
                        break
            elif x < X and y > Y:
                while x + sum != X or y - sum != Y:
                    if pole[x + sum][y - sum] == " ":
                        sum += 1
                        okay = 0
                    elif pole[x + sum][y - sum] in hitboxč or pole[x + sum][y - sum] in hitboxw:
                        if y - sum == Y and x + sum == X:
                            draw_board(screen, save)
                            break
                    else:
                        okay = 1
                        draw_board(screen, save)
                        break
            else:
                okay = 1
            if okay == 0:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "bi"
                    barva = "b"
                # print(pole[0], "\n", pole[1], "\n", pole[2], "\n", pole[3], "\n", pole[4], "\n", pole[5], "\n", pole[6], "\n", pole[7])
                draw_board(screen, save)
            else:
                draw_board(screen, save)
        elif clicked_piece == "qu":
            bp(x, y, color)
            ro(x,y, color)
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            sum = 1
            okay = 0
            if X == x or Y == y:
                if X == x:
                    okay = 0
                elif Y == y:
                    okay = 0
            else:
                okay = 0
                if x < X and y < Y:
                    while x + sum != X or y + sum != Y:
                        if pole[x + sum][y + sum] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x + sum][y + sum] in hitboxč or pole[x + sum][y + sum] in hitboxw:
                            if y + sum == Y and x + sum == X:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                elif x > X and y < Y:
                    while x - sum != X or y + sum != Y:
                        if pole[x - sum][y + sum] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x - sum][y + sum] in hitboxč or pole[x - sum][y + sum] in hitboxw:
                            if y + sum == Y and x - sum == X:
                                draw_board(screen, save)
                                break
                        else:
                            okay = 1
                            draw_board(screen, save)
                            break
                elif x > X and y > Y:
                    while x - sum != X or y - sum != Y:
                        if pole[x - sum][y - sum] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x - sum][y - sum] in hitboxč or pole[x - sum][y - sum] in hitboxw:
                            if y - sum == Y and x - sum == X:
                                draw_board(screen, save)
                                break
                        else:
                            okay = 1
                            draw_board(screen, save)
                            break
                elif x < X and y > Y:
                    while x + sum != X or y - sum != Y:
                        if pole[x + sum][y - sum] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x + sum][y - sum] in hitboxč or pole[x + sum][y - sum] in hitboxw:
                            if y - sum == Y and x + sum == X:
                                draw_board(screen, save)
                                break
                        else:
                            okay = 1
                            draw_board(screen, save)
                            break
                else:
                    okay = 1
            if okay == 0:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "qu"
                    barva = "b"
                # print(pole[0], "\n", pole[1], "\n", pole[2], "\n", pole[3], "\n", pole[4], "\n", pole[5], "\n", pole[6], "\n", pole[7])
                draw_board(screen, save)
            else:
                draw_board(screen, save)
        elif clicked_piece == "kn":
            try:
                if pole[x + 1][y + 2] == " " or pole[x + 1][y + 2] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 2) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y + 2]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 2) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y + 2] == " " or pole[x - 1][y + 2] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 2) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y + 2]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 2) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 1][y - 2] == " " or pole[x + 1][y - 2] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 2) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y - 2]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 2) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y - 2] == " " or pole[x - 1][y - 2] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 2) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y - 2]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 2) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 2][y - 1] == " " or pole[x - 2][y - 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 2][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 2][y + 1] == " " or pole[x - 2][y + 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 2][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 2][y - 1] == " " or pole[x + 2][y - 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 2][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 2][y + 1] == " " or pole[x + 2][y + 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 2][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            if x + 2 == X and y + 1 == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "kn"
                    barva = "b"
                    draw_board(screen, save)
            elif x + 2 == X and y - 1 == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "kn"
                    barva = "b"
                    draw_board(screen, save)
            elif x - 2 == X and y - 1 == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "kn"
                    barva = "b"
                    draw_board(screen, save)
            elif x - 2 == X and y + 1 == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "kn"
                    barva = "b"
                    draw_board(screen, save)
            elif x + 1 == X and y + 2 == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "kn"
                    barva = "b"
                    draw_board(screen, save)
            elif x + 1 == X and y - 2 == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "kn"
                    barva = "b"
                    draw_board(screen, save)
            elif x - 1 == X and y - 2 == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "kn"
                    barva = "b"
                    draw_board(screen, save)
            elif x - 1 == X and y + 2 == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "kn"
                    barva = "b"
                    draw_board(screen, save)
        elif clicked_piece == "ki":
            try:
                if pole[x + 1][y] == " " or pole[x + 1][y] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 1][y + 1] == " " or pole[x + 1][y + 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 1][y -1] == " " or pole[x + 1][y - 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x][y -1] == " " or pole[x][y -1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x][y + 1] == " " or pole[x][y + 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y] == " " or pole[x - 1][y] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y + 1] == " " or pole[x - 1][y + 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y -1] == " " or pole[x - 1][y - 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            if x + 1 == X and y + 1 == Y \
                    or x - 1 == X and y + 1 == Y \
                    or x + 1 == X and y - 1 == Y \
                    or x - 1 == X and y - 1 == Y \
                    or x == X and y - 1 == Y \
                    or x == X and y + 1 == Y \
                    or x + 1 == X and y == Y \
                    or x - 1 == X and y == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "ki"
                    barva = "b"
                    draw_board(screen, save)
        elif clicked_piece == "pa":
            dva = 0
            if x == 1:
                dva = 1
                try:
                    if pole[x + 1][y] == " ":
                        pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                except:
                    pass
                try:
                    if pole[x + 2][y] == " " or pole[x + 2][y] in hitboxč:
                        if pole[x + 2][y] in hitboxč:
                            pass
                        else:
                            pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                            piece = pole[x + 2][y]
                            piece_image = pygame.image.load(f"{piece}.png")
                            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                            screen.blit(piece_image, pygame.Rect((y) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                except:
                    pass
            else:
                if pole[x + 1][y] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    try:
                        piece = pole[x + 1][y]
                        piece_image = pygame.image.load(f"{piece}.png")
                        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                        screen.blit(piece_image, pygame.Rect((y) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    except:
                        pass
            try:
                if pole[x + 1][y + 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 1][y - 1] in hitboxč:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            if x + 1 == X and y == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    if X == 7:
                        pole[x][y] = " "
                        pole[X][Y] = "qu"
                        barva = "b"
                        draw_board(screen, save)
                    else:
                        pole[x][y] = " "
                        pole[X][Y] = "pa"
                        barva = "b"
                        draw_board(screen, save)
            elif dva == 1:
                if x + 2 == X and y == Y:
                    if pole[X][Y] in hitboxw or pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                        draw_board(screen, save)
                    else:
                        pole[x][y] = " "
                        pole[X][Y] = "pa"
                        barva = "b"
                        draw_board(screen, save)
                else:
                    draw_board(screen, save)
            elif x + 1 == X and y + 1 == Y:
                if X == 7:
                    pole[x][y] = " "
                    pole[X][Y] = "qu"
                    barva = "b"
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "pa"
                    barva = "b"
                    draw_board(screen, save)
            elif x + 1 == X and y - 1 == Y:
                if X == 7:
                    pole[x][y] = " "
                    pole[X][Y] = "qu"
                    barva = "b"
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "pa"
                    barva = "b"
                    draw_board(screen, save)
            else:
                draw_board(screen, save)
    elif barva == "b":
        if clicked_piece == "r":
            while x + sum < 8:
                if pole[x + sum][y] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while y + sum < 8:
                if pole[x][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x][y + sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum > -1:
                if pole[x - sum][y] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while y - sum > -1:
                #print(pole[x][y - sum])
                if pole[x][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x][y - sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            pygame.display.update()
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            okay = 0
            sum = 1
            # kontrola pohybu
            if X == x or Y == y:
                if x > X:
                    #print("x > X")
                    while x - sum != X:
                        #print(y - sum, "s")
                        if pole[x - sum][y] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x - sum][y] in hitboxč or pole[x - sum][y] in hitboxw:
                            if x - sum == X:
                                draw_board(screen, save)
                                break
                            else:
                                #print("lol")
                                okay = 1
                                draw_board(screen, save)
                                break
                elif x < X:
                    while x + sum != X:
                        if pole[x + sum][y] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x + sum][y] in hitboxč or pole[x + sum][y] in hitboxw:
                            if x + sum == X:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                elif y < Y:
                    while y + sum != Y:
                        if pole[x][y + sum] == " ":
                            sum += 1
                            okay = 0
                        if pole[x][y + sum] in hitboxč or pole[x][y + sum] in hitboxw:
                            if y + sum == Y:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                elif y > Y:
                    while y - sum != Y:
                        if pole[x][y - sum] == " ":
                            sum += 1
                            okay = 0
                        if pole[x][y - sum] in hitboxč or pole[x][y - sum] in hitboxw:
                            if y - sum == Y:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                draw_board(screen, save)
                if okay == 0:
                    if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                        draw_board(screen, save)
                    else:
                        pole[x][y] = " "
                        pole[X][Y] = "r"
                        barva = "w"
                    # print(pole[0], "\n", pole[1], "\n", pole[2], "\n", pole[3], "\n", pole[4], "\n", pole[5], "\n", pole[6], "\n", pole[7])
                    draw_board(screen, save)
            else:
                draw_board(screen, save)
        elif clicked_piece == "b":
            while x + sum < 8 and y + sum < 8:
                if pole[x + sum][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y + sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum < 8 and y - sum < 8:
                if pole[x - sum][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y - sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x + sum < 8 and y - sum < 8:
                if pole[x + sum][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y - sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum < 8 and y + sum < 8:
                if pole[x - sum][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y + sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            pygame.display.update()
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            sum = 1
            okay = 0
            if x < X and y < Y:
                while x + sum != X or y + sum != Y:
                    if pole[x + sum][y + sum] == " ":
                        sum += 1
                        okay = 0
                    elif pole[x + sum][y + sum] in hitboxč or pole[x + sum][y + sum] in hitboxw:
                        if y + sum == Y and x + sum == X:
                            draw_board(screen, save)
                            break
                        else:
                            okay = 1
                            draw_board(screen, save)
                            break
            elif x > X and y < Y:
                while x - sum != X or y + sum != Y:
                    if pole[x - sum][y + sum] == " ":
                        sum += 1
                        okay = 0
                    elif pole[x - sum][y + sum] in hitboxč or pole[x - sum][y + sum] in hitboxw:
                        if y + sum == Y and x - sum == X:
                            draw_board(screen, save)
                            break
                    else:
                        okay = 1
                        draw_board(screen, save)
                        break
            elif x > X and y > Y:
                while x - sum != X or y - sum != Y:
                    if pole[x - sum][y - sum] == " ":
                        sum += 1
                        okay = 0
                    elif pole[x - sum][y - sum] in hitboxč or pole[x - sum][y - sum] in hitboxw:
                        if y - sum == Y and x - sum == X:
                            draw_board(screen, save)
                            break
                    else:
                        okay = 1
                        draw_board(screen, save)
                        break
            elif x < X and y > Y:
                while x + sum != X or y - sum != Y:
                    if pole[x + sum][y - sum] == " ":
                        sum += 1
                        okay = 0
                    elif pole[x + sum][y - sum] in hitboxč or pole[x + sum][y - sum] in hitboxw:
                        if y - sum == Y and x + sum == X:
                            draw_board(screen, save)
                            break
                    else:
                        okay = 1
                        draw_board(screen, save)
                        break
            else:
                okay = 1
            if okay == 0:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "b"
                    barva = "w"
                # print(pole[0], "\n", pole[1], "\n", pole[2], "\n", pole[3], "\n", pole[4], "\n", pole[5], "\n", pole[6], "\n", pole[7])
                draw_board(screen, save)
            else:
                draw_board(screen, save)
        elif clicked_piece == "q":
            while x + sum < 8 and y + sum < 8:
                if pole[x + sum][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y + sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum < 8 and y - sum < 8:
                if pole[x - sum][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y - sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x + sum < 8 and y - sum < 8:
                if pole[x + sum][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y - sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum < 8 and y + sum < 8:
                if pole[x - sum][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y + sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x + sum < 8:
                if pole[x + sum][y] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x + sum][y] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + sum][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect(y * SQ_SIZE, (x + sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while y + sum < 8:
                if pole[x][y + sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x][y + sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y + sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while x - sum > -1:
                if pole[x - sum][y] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x - sum][y] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - sum][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect(y * SQ_SIZE, (x - sum) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            sum = 1
            while y - sum > -1:
                #print(pole[x][y - sum])
                if pole[x][y - sum] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    sum += 1
                elif pole[x][y - sum] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y - sum]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - sum) * SQ_SIZE, x * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    break
                else:
                    break
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            sum = 1
            okay = 0
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            #print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            sum = 1
            okay = 0
            if X == x or Y == y:
                if X == x:
                    okay = 0
                elif Y == y:
                    okay = 0
            else:
                okay = 0
                if x < X and y < Y:
                    while x + sum != X or y + sum != Y:
                        if pole[x + sum][y + sum] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x + sum][y + sum] in hitboxč or pole[x + sum][y + sum] in hitboxw:
                            if y + sum == Y and x + sum == X:
                                draw_board(screen, save)
                                break
                            else:
                                okay = 1
                                draw_board(screen, save)
                                break
                elif x > X and y < Y:
                    while x - sum != X or y + sum != Y:
                        if pole[x - sum][y + sum] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x - sum][y + sum] in hitboxč or pole[x - sum][y + sum] in hitboxw:
                            if y + sum == Y and x - sum == X:
                                draw_board(screen, save)
                                break
                        else:
                            okay = 1
                            draw_board(screen, save)
                            break
                elif x > X and y > Y:
                    while x - sum != X or y - sum != Y:
                        if pole[x - sum][y - sum] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x - sum][y - sum] in hitboxč or pole[x - sum][y - sum] in hitboxw:
                            if y - sum == Y and x - sum == X:
                                draw_board(screen, save)
                                break
                        else:
                            okay = 1
                            draw_board(screen, save)
                            break
                elif x < X and y > Y:
                    while x + sum != X or y - sum != Y:
                        if pole[x + sum][y - sum] == " ":
                            sum += 1
                            okay = 0
                        elif pole[x + sum][y - sum] in hitboxč or pole[x + sum][y - sum] in hitboxw:
                            if y - sum == Y and x + sum == X:
                                draw_board(screen, save)
                                break
                        else:
                            okay = 1
                            draw_board(screen, save)
                            break
                else:
                    okay = 1
            if okay == 0:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "q"
                    barva = "w"
                # print(pole[0], "\n", pole[1], "\n", pole[2], "\n", pole[3], "\n", pole[4], "\n", pole[5], "\n", pole[6], "\n", pole[7])
                draw_board(screen, save)
            else:
                draw_board(screen, save)
        elif clicked_piece == "n":
            try:
                if pole[x + 1][y + 2] == " " or pole[x + 1][y + 2] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 2) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y + 2]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 2) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y + 2] == " " or pole[x - 1][y + 2] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 2) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y + 2]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 2) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 1][y - 2] == " " or pole[x + 1][y - 2] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 2) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y - 2]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 2) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y - 2] == " " or pole[x - 1][y - 2] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 2) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y - 2]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 2) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 2][y - 1] == " " or pole[x - 2][y - 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 2][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 2][y + 1] == " " or pole[x - 2][y + 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 2][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 2][y - 1] == " " or pole[x + 2][y - 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 2][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 2][y + 1] == " " or pole[x + 2][y + 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 2][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x + 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            if x + 2 == X and y + 1 == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "n"
                    barva = "w"
                    draw_board(screen, save)
            elif x + 2 == X and y - 1 == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "n"
                    barva = "w"
                    draw_board(screen, save)
            elif x - 2 == X and y - 1 == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "n"
                    barva = "w"
                    draw_board(screen, save)
            elif x - 2 == X and y + 1 == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "n"
                    barva = "w"
                    draw_board(screen, save)
            elif x + 1 == X and y + 2 == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "n"
                    barva = "w"
                    draw_board(screen, save)
            elif x + 1 == X and y - 2 == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "n"
                    barva = "w"
                    draw_board(screen, save)
            elif x - 1 == X and y - 2 == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "n"
                    barva = "w"
                    draw_board(screen, save)
            elif x - 1 == X and y + 2 == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "n"
                    barva = "w"
                    draw_board(screen, save)
        elif clicked_piece == "p":
            dva = 0
            if x == 6:
                dva = 1
                try:
                    if pole[x - 1][y] == " ":
                        pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                except:
                    pass
                try:
                    if pole[x - 2][y] == " " or pole[x - 2][y] in hitboxw:
                        if pole[x - 2][y] in hitboxw:
                            pass
                        else:
                            pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                            piece = pole[x - 2][y]
                            piece_image = pygame.image.load(f"{piece}.png")
                            piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                            screen.blit(piece_image, pygame.Rect((y) * SQ_SIZE, (x - 2) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                except:
                    pass
            else:
                if pole[x - 1][y] == " ":
                    pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    try:
                        piece = pole[x - 1][y]
                        piece_image = pygame.image.load(f"{piece}.png")
                        piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                        screen.blit(piece_image, pygame.Rect((y) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    except:
                        pass
            try:
                if pole[x - 1][y + 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y - 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            print(X, x, Y, y)
                            running = False
            if x - 1 == X and y == Y:
                if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    if X == 1:
                        pole[x][y] = " "
                        pole[X][Y] = "q"
                        barva = "w"
                        draw_board(screen, save)
                    else:
                        pole[x][y] = " "
                        pole[X][Y] = "p"
                        barva = "w"
                        draw_board(screen, save)
            elif dva == 1:
                if x - 2 == X and y == Y:
                    if pole[X][Y] in hitboxw or pole[X][Y] in kralbox:
                        draw_board(screen, save)
                    else:
                        if X == 0:
                            pole[x][y] = " "
                            pole[X][Y] = "q"
                            barva = "w"
                            draw_board(screen, save)
                        else:
                            pole[x][y] = " "
                            pole[X][Y] = "p"
                            barva = "w"
                            draw_board(screen, save)
                else:
                    draw_board(screen, save)
            elif x - 1 == X and y + 1 == Y:
                if X == 0:
                    pole[x][y] = " "
                    pole[X][Y] = "q"
                    barva = "w"
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "p"
                    barva = "w"
                    draw_board(screen, save)
            elif x - 1 == X and y - 1 == Y:
                if X == 0:
                    pole[x][y] = " "
                    pole[X][Y] = "q"
                    barva = "w"
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "p"
                    barva = "w"
                    draw_board(screen, save)
        elif clicked_piece == "k":
            try:
                if pole[x + 1][y] == " " or pole[x + 1][y] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 1][y + 1] == " " or pole[x + 1][y + 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x + 1][y -1] == " " or pole[x + 1][y - 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x + 1][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x + 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x][y -1] == " " or pole[x][y -1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x][y + 1] == " " or pole[x][y + 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y] == " " or pole[x - 1][y] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y + 1] == " " or pole[x - 1][y + 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y + 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y + 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y + 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            try:
                if pole[x - 1][y -1] == " " or pole[x - 1][y - 1] in hitboxw:
                    pygame.draw.rect(screen, color, pygame.Rect((y - 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                    piece = pole[x - 1][y - 1]
                    piece_image = pygame.image.load(f"{piece}.png")
                    piece_image = pygame.transform.scale(piece_image, (SQ_SIZE, SQ_SIZE))
                    screen.blit(piece_image, pygame.Rect((y - 1) * SQ_SIZE, (x - 1) * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            except:
                pass
            while running:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        X, Y = get_clicked_square(mouse_pos)
                        if 0 <= X < 8 and 0 <= Y < 8:
                            print(X, x, Y, y)
                            running = False
            draw_board(screen, save)
            if x + 1 == X and y + 1 == Y \
                    or x - 1 == X and y + 1 == Y \
                    or x + 1 == X and y - 1 == Y \
                    or x - 1 == X and y - 1 == Y \
                    or x == X and y - 1 == Y \
                    or x == X and y + 1 == Y \
                    or x + 1 == X and y == Y \
                    or x - 1 == X and y == Y:
                if pole[X][Y] in hitboxč or pole[X][Y] in kralbox:
                    draw_board(screen, save)
                else:
                    pole[x][y] = " "
                    pole[X][Y] = "ki"
                    barva = "b"
                    draw_board(screen, save)


draw_board(screen, save)

while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x, y = get_clicked_square(mouse_pos)
            if 0 <= x < 8 and 0 <= y < 8:
                clicked_piece = pole[x][y]
                print("Clicked piece:", clicked_piece, x, y)
                move(clicked_piece, x, y)
