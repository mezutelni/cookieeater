import random,os,sys,time,keyboard,winsound

os.system("cls")
board = ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"]
line = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]

points = 0
moves = 0
char = "o"
player_x = 7
player_y = 7
playerCoords = [player_x,player_y,moves,char]
x = random.randint(1,12)
y = random.randint(1,13)
starCoords = [x,y]

#This function draws map with player and point, it takes 7 args which are player x and y coordinate, point x and y coordinate, amount of points, amount of moves made by player, and char(graphical representation of player)
def drawMap(star_x,star_y,player_x,player_y,points,moves,char):
    
    while star_x == 0 or star_x == 13:
        star_x == random.randint(1,12)


    for i in range(0,16):
        if i == star_y and i == player_y and star_x == player_x:
            points = points + 1
            x = random.randint(1,12)
            y = random.randint(1,13)
            while x == star_x:
                x = random.randint(1,12)
            while y == star_y:
                y = random.randint(1,13)
            star_x = x
            star_y = y
            winsound.PlaySound("bite.wav", winsound.SND_ASYNC)
            
            
        elif i == star_y:
            board[star_x] = "+"
            if i == player_y:
                board[player_x] = char
        elif i == player_y:
                board[player_x] = char
        if i == 0 or i == 15:
            print(*line)
        else:
            print(*board)

        board[player_x] = " "
        board[star_x] = " "
        
        board[0] = "|"
        board[15] = "|"

    print("Points: %s" % points)
    zwrot = [star_x,star_y,points]
    return zwrot

def moveLeft(player_x):
    if player_x == 1:
        return player_x
    return player_x-1

def moveUp(player_y):
    if player_y == 1:
        return player_y
    return player_y-1

def moveRight(player_x):
    if player_x == 13:
        return player_x
    return player_x+1

def moveDown(player_y):
    if player_y == 13:
        return player_y
    return player_y+1

#This funciom, listens for key press, and then changes x or y coordinate of player (depends on key pressed)
def move(player_x,player_y,moves,char):
    keyboard.read_key()
    if keyboard.is_pressed("left"):
        player_x = moveLeft(player_x)
        moves += 1
        char = ">"
    elif keyboard.is_pressed("up"):
        player_y = moveUp(player_y)
        moves += 1
        char = "v"
    elif keyboard.is_pressed("right"):
       player_x = moveRight(player_x)
       moves += 1
       char = "<"
    elif keyboard.is_pressed("down"):
        player_y = moveDown(player_y)
        moves += 1
        char = "^"
    elif keyboard.is_pressed("ctrl+c"):
        print("Thanks for playing, you moved "+str(moves)+" times")
        time.sleep(2)
        sys.exit(0)
    playerCoords = [player_x,player_y,moves,char]
    return playerCoords

#This function, is responsible for point movement, it's still on todo
def starMove(star_x,star_y):
    if star_x > 2 and star_x<11:
        if star_y>2 and star_y<11:
            if 1 == random.randint(1,2):
                z = random.randint(-1,1)
                star_y = star_y+z
                coords = [star_x,star_y]
                return coords
            elif 2 == random.randint(1,2):
                z = random.randint(-1,1)
                star_x = star_x+z
                coords = [star_x,star_y]
                return coords
        else:
                z = random.randint(-1,1)
                star_y = star_y+z
                coords = [star_x,star_y]
                return coords
    elif star_y > 2 and star_y<11:
        if star_x>2 and star_x<11:
            if 1 == random.randint(1,2):
                z = random.randint(-1,1)
                star_y = star_y+z
                coords = [star_x,star_y]
                return coords
            elif 2 == random.randint(1,2):
                z = random.randint(-1,1)
                star_x = star_x+z
                coords = [star_x,star_y]
                return coords
        else:
                z = random.randint(-1,1)
                star_y = star_y+z
                coords = [star_x,star_y]
                return coords
    elif star_x <= 2:
        star_x = star_x++1
    elif star_x >=12:
        star_x = star_x-1
    elif star_y<=2:
        star_y = star_y-1
    elif star_y >=12:
        star_y = stra_y+1
    coords = [star_x,star_y]
    return coords



while 1:
    os.system("cls")
    zwrot = drawMap(starCoords[0],starCoords[1],playerCoords[0],playerCoords[1],points,moves,char)

    char = playerCoords[3]
    moves = playerCoords[2]

    points = zwrot[2]
    
    starCoords[0] = zwrot[0]
    starCoords[1] = zwrot[1]
    #starCoords = starMove(starCoords[0],starCoords[1])
    playerCoords = move(playerCoords[0],playerCoords[1],moves,char)
    os.system("cls")

    