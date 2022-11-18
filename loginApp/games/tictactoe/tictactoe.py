'''
"Tic Tac Toe"
Eshaan Tripathi
10/12/22
Play tic tac toe
'''

#define rows list
rows = [['','',''],['','',''],['','','']]

#define player move lists and total_moves variables
player1 = []
player2 = []
total_moves = 0

#import sys library
import sys

#print greeting message
print("Hello, Welcome to tic tac toe.")

#create for loop to simulate each player move.
for i in range(5):
    #ask for player1 move
    player1_move = input("Please enter player 1's move (ex: r2c1): ")

    #check whether or not that move has already been taken.
    while player1_move in player2 or player1_move in player1:
        player1_move = input("Whoops that space is taken. Please enter move (ex: r2c1): ")
    #if it isnt taken, append player move
    player1.append(player1_move)
    total_moves+=1

    #derive the row and column values
    p1move = player1_move.replace("r",'')
    p1move_div = p1move.split('c')

    p1r = int(p1move_div[0])-1
    p1c = int(p1move_div[1])-1

    #set the location in the 2d list as the X
    rows[p1r][p1c] = "X"

    #print the board
    for i in rows:
        print(i)

    
    #check if the player has won
    for l in rows:
        w_cp1 = 0
        for i in l:
            for j in i:
                if j == 'X':
                    w_cp1+=1
        if w_cp1 == 3:
            print("Player 1 wins.")
            sys.exit()
        
    #making columns list    

    col1 = [rows[0][0],rows[1][0],rows[2][0]]
    col2 = [rows[0][1],rows[1][1],rows[2][1]]
    col3 = [rows[0][2],rows[1][2],rows[2][2]]

    cols = []

    cols.append(col1)
    cols.append(col2)
    cols.append(col3)

    #checking vertical wins
    for g in cols:
        w_cp1 = 0

        for i in g:
            if i == "X":
                w_cp1+=1

        if w_cp1 == 3:
            print("Player 1 wins.")
            sys.exit()

    #checking diagonal wins
    if rows[0][0] == "X" and rows[1][1] == "X" and rows[2][2] == "X":
        print("Player 1 wins.")
        sys.exit()

    if rows[0][2] == "X" and rows[1][1] == "X" and rows[2][0] == "X":
        print("Player 1 wins.")
        sys.exit()


    #asking for player 2 move
    player2_move = input("Please enter player 2's move (ex: r2c1): ")

    #checking if that move has already been taken
    while player2_move in player2 or player2_move in player1:
        player2_move = input("Whoops that space is taken. Please enter move (ex: r2c1): ")
    #add move to player 2 list
    player2.append(player2_move)

    #increment total moves
    total_moves+=1

    #derive location of symbol
    p2move = player2_move.replace("r",'')
    p2move_div = p2move.split('c')

    p2r = int(p2move_div[0])-1
    p2c = int(p2move_div[1])-1

    #set location of symbol
    rows[p2r][p2c] = "O"

    #print symbol
    for i in rows:
        print(i)

    #check for horizontal wins
    for l in rows:
        w_cp2 = 0
        for i in l:
            for j in i:
                if j == 'O':
                    w_cp2+=1
        if w_cp2 == 3:
            print("Player 2 wins.")
            sys.exit()

    #get columns and store in cols list
    col1 = [rows[0][0],rows[1][0],rows[2][0]]
    col2 = [rows[0][1],rows[1][1],rows[2][1]]
    col3 = [rows[0][2],rows[1][2],rows[2][2]]

    cols = []

    cols.append(col1)
    cols.append(col2)
    cols.append(col3)

    #check for vertical wins
    for g in cols:
        w_cp2 = 0

        for i in g:
            if i == "O":
                w_cp2+=1

        if w_cp2 == 3:
            print("Player 2 wins.")
            sys.exit()

    #check for diagonal wins.
    if rows[0][0] == "O" and rows[1][1] == "O" and rows[2][2] == "O":
        print("Player 2 wins.")
        sys.exit()

    if rows[0][2] == "O" and rows[1][1] == "O" and rows[2][0] == "O":
        print("Player 2 wins.")
        sys.exit()