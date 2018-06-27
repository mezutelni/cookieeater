import random,os,sys,time,keyboard,winsound

if sys.platform == "win32":
    clr = "cls"
elif sys.platform == "linux" or sys.platform == "linux2":
    clr = "clear"


board = ["|"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","|"]
line = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]

board_max_x = board_max_y = 15
board_min_x = board_min_y = 0

points = 0
moves = 0
char = "o"

player_x = player_y = 7
player_coords = [player_x,player_y,moves,char]

star_x = random.randint(board_min_x+1,board_max_x-2)
star_y = random.randint(board_min_y+1,board_max_y-2)
star_coords = [star_x,star_y]

#This function draws map with player and point, it takes 7 args which are player x and y coordinate, point x and y coordinate, amount of points, amount of moves made by player, and char(graphical representation of player)
def drawMap(star_x,star_y,player_x,player_y,points,moves,char):

    for i in range(0,16):
        if i == star_y and i == player_y and star_x == player_x:
            points = points + 1
            x = random.randint(board_min_x+1,board_max_x-2)
            y = random.randint(board_min_y+1,board_max_y-2)
            while x == star_x:
                x = random.randint(board_min_x+1,board_max_x-2)
            while y == star_y:
                y = random.randint(board_min_y+1,board_max_y-2)
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
    player_coords = [player_x,player_y,moves,char]
    return player_coords

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
    os.system(clr)
    zwrot = drawMap(star_coords[0],star_coords[1],player_coords[0],player_coords[1],points,moves,char)

    char = player_coords[3]
    moves = player_coords[2]

    points = zwrot[2]
    
    star_coords[0] = zwrot[0]
    star_coords[1] = zwrot[1]

    #star_coords = starMove(star_coords[0],star_coords[1])
    player_coords = move(player_coords[0],player_coords[1],moves,char)