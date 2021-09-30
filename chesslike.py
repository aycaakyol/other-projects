import sys
f = open(sys.argv[1],"r")
commands = [line.split() for line in f.readlines()]
f.close()
# My logic is that board is the chess board and pos is the coordinates of the chess board. In functions, i match the indexes of position and the piece.
board= ["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]
first_board=board.copy()
pos=["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8", "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7", "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6", "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5", "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4", "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3", "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]
blacks=["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
whites=["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]
# This is for printing the board. Because it's 8*8, it goes by printing 0-7 indexed items then 8-15 and so on...
def mapping(somelist):
    c, r = 0, 0
    print("------------------------")
    while c < 64:
        while r < 8:
            x = somelist[c:c+8]
            x = " ".join(x)
            print(x)
            r += 1
            c = c + 8
            if c==64:
                break
    print("------------------------")
# While writing the code, I noticed that the type of moves repeat. For example both rooks and queens go left, right, up and down.
# The main logic of these function is that it first checks by the position of the piece where can it go. For example if it is on the a column, it cannot go left.
# So I first check where it is.
def rook_moves(piece,color,not_color):
    # up
    if board.index(piece) > 7:                              # It cannot go up if it is on the 8th row (according to chess coordinates)
        for r in range(board.index(piece) - 8, 0, -8):      # Rook can move multiple times so  used a for loop here.
            if board[r] == "  ":                            # If it is empty, it can move
                possible_moves.append(pos[r])
                if r > 7 and board[r - 8] in not_color:     # In this code I'm checking if the square after this move has the other color's piece
                    possible_moves.append(pos[r - 8])       # It can take it, but has to stop after taking the piece.
                    break
            elif board[r] in not_color:                     # If the first square it checks is different color piece, it can take it but can not move anymore
                possible_moves.append(pos[r])
                break
            elif board[r] in color:                         # If the square has same color's piece, it can not move anymore
                break
    # down
    if board.index(piece) < 56:                             # Same logic for the other moves but with different changes in the index
        for u in range(board.index(piece) + 8, 64, 8):      # and different limits
            if board[u] == "  ":
                possible_moves.append(pos[u])
                if u < 56 and board[u + 8] in not_color:
                    possible_moves.append(pos[u + 8])
                    break
            elif board[u] in not_color:
                possible_moves.append(pos[u])
                break
            elif board[u] in color:
                break
    # left
    if board.index(piece) % 8 != 0:
        s = board.index(piece) - board.index(piece) % 8
        for j in range(board.index(piece) - 1, s - 1, -1):
            if board[j] == "  ":
                possible_moves.append(pos[j])
                if j % 8 != 0 and j - 1 > -1 and board[j - 1] in not_color:   # Added j - 1 > -1 here because, while it reduces the value of j, it
                    possible_moves.append(pos[j - 1])                         # it might become negative which would change the way the indexes are found
                    break
            elif board[j] in not_color:
                possible_moves.append(pos[j])
                break
            elif board[j] in color:
                break
    # right
    if board.index(piece) % 8 != 7:
        s = board.index(piece) - board.index(piece) % 8
        for t in range(board.index(piece) + 1, s + 8, 1):
            if board[t] == "  ":
                possible_moves.append(pos[t])
                if t % 8 != 7 and t + 1 < 64 and board[t + 1] in not_color:
                    possible_moves.append(pos[t + 1])
                    break
            elif board[t] in not_color:
                possible_moves.append(pos[t])
                break
            elif board[t] in color:
                break
    return possible_moves, board                                 # I've added all the possible moves in a list which will be used in showmoves and move functions

def white_bishop_moves(piece,color,not_color):
    if board.index(piece) > 7:                              # It cannot go up if it's not on the 8th row (by chess coordinates9
        # right up diagonal
        if board.index(piece) % 8 != 7:                     # It cannot go right if it is not the h column
            for a in range(board.index(piece) - 7, -1, -7): # By the indexes of the board this move goes by reducing the indexes by 7
                if a % 8 == 0:                              # If it is not the h column at last, reducing it 7 more would go to a column, which is impossible
                    break
                elif a % 8 != 0 and board[a] == "  ":       # If it is empty, the piece can move
                    possible_moves.append(pos[a])
                    if a % 8 != 7 and a - 7 > -1 and board[a - 7] in not_color: #If the next square has other color's piece, it can take it but has to stop
                        possible_moves.append(pos[a - 7])
                        break
                elif board[a] in not_color:            # If the first move can take the other color's piece, I taake it but have to stop
                    possible_moves.append(pos[a])
                    break
                elif board[a] in color:                # If it is the same color, it cannot move
                    break
        # left up diagonal
        if board.index(piece) % 8 != 0:                # Same logic here
            for z in range(board.index(piece) - 9, -1, -9):
                if z % 8 == 7:
                    break
                elif z % 8 != 7 and board[z] == "  ":
                    possible_moves.append(pos[z])
                    if z % 8 != 0 and z - 9 > -1 and board[z - 9] in not_color:
                        possible_moves.append(pos[z - 9])
                        break
                elif board[z] in not_color:
                    possible_moves.append(pos[z])
                    break
                elif board[z] in color:
                    break
    return possible_moves

def black_bishop_moves(piece,color,not_color):
    if board.index(piece) < 56:
        # right down diagonal
        if board.index(piece) % 8 != 7:
            for e in range(board.index(piece) + 9, 64, 9):
                if e % 8 == 0:
                    break
                elif e % 8 != 0 and board[e] == "  ":
                    possible_moves.append(pos[e])
                    if e % 8 != 7 and e + 9 < 64 and board[e + 9] in not_color:
                        possible_moves.append(pos[e + 9])
                        break
                elif board[e] in not_color:
                    possible_moves.append(pos[e])
                    break
                elif board[e] in color:
                    break
        # left down diagonal
        if board.index(piece) % 8 != 0:
            for m in range(board.index(piece) + 7, 64, 7):
                if m % 8 == 7:
                    break
                elif m % 8 != 7 and board[m] == "  ":
                    possible_moves.append(pos[m])
                    if m % 8 != 0 and m + 7 < 64 and board[m + 7] in not_color:
                        possible_moves.append(pos[m + 7])
                        break
                elif board[m] in not_color:
                    possible_moves.append(pos[m])
                    break
                elif board[m] in color:
                    break
    return possible_moves

def pawn_moves(condition,change,piece,color,not_color):
    if condition:              # The pawn can move up if it's not on 8th row and down if it's not on the first row so the condition is for checking that
        if board[board.index(piece) + change] == "  " or board[board.index(piece) + change] in not_color: # It can move if the square is empty or has
            possible_moves.append(pos[board.index(piece) + change])                                       # the opponent's piece
    return possible_moves, board

def showmoves(piece,color,not_color):
    global possible_moves
    possible_moves=[]           # Possible moves is an empty list and according to the condtions, if a square can be gone to, then I append the
    # WHITE PAWN                # position of the square's index to the list
    if piece == "p1" or piece == "p2" or piece == "p3" or piece == "p4" or piece == "p5" or piece == "p6" or piece == "p7" or piece == "p8":
        pawn_moves(board.index(piece) > 7,-8,piece,color,not_color)

    # BLACK PAWN
    if piece == "P1" or piece == "P2" or piece == "P3" or piece == "P4" or piece == "P5" or piece == "P6" or piece == "P7" or piece == "P8":
        pawn_moves(board.index(piece) < 56,8,piece, color, not_color)

    # KNIGHTS
    if piece == "n1" or piece == "n2" or piece == "N1" or piece == "N2":
        # L move
        if board.index(piece)==0:     # on some indexes it can only do some L moves, i saw the pattern and divided it to 25 sections
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
        if board.index(piece) == 1:
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
        if board.index(piece) == 8:
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
        if board.index(piece) == 9:
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
        if board.index(piece) == 6:
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
        if board.index(piece) == 7:
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
        if board.index(piece) == 14:
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
        if board.index(piece) == 15:
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
        if board.index(piece) == 48:
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
        if board.index(piece) == 49:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color :
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
        if board.index(piece) == 56:
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
        if board.index(piece) == 57:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color:
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
        if board.index(piece) == 54:
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color:
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
        if board.index(piece) == 55:
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color :
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
        if board.index(piece) == 62:
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color:
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
        if board.index(piece) == 63:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color:
                possible_moves.append(pos[board.index(piece) -17])
        if 9 < board.index(piece) < 14:
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
        if 49 < board.index(piece) < 54:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color :
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
        if 57 < board.index(piece) < 62:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color :
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
        if 1 < board.index(piece) < 6:
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
        if 15 < board.index(piece) < 41 and (board.index(piece)) % 8 == 0:
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
        if 16 < board.index(piece) < 42 and (board.index(piece)) % 8 == 1:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color :
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
        if 21 < board.index(piece) < 47 and (board.index(piece)) % 8 == 6:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color :
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
        if 22 < board.index(piece) < 48 and (board.index(piece)) % 8 == 7:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color :
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
        if 17<board.index(piece)<46 and 1 < board.index(piece) % 8 < 6:
            if board[board.index(piece)-17] == "  " or board[board.index(piece)-17] in not_color :
                possible_moves.append(pos[board.index(piece) -17])
            if board[board.index(piece)-15] == "  " or board[board.index(piece)-15] in not_color:
                possible_moves.append(pos[board.index(piece) -15])
            if board[board.index(piece)-10] == "  " or board[board.index(piece)-10] in not_color:
                possible_moves.append(pos[board.index(piece) -10])
            if board[board.index(piece)-6] == "  " or board[board.index(piece)-6] in not_color:
                possible_moves.append(pos[board.index(piece) -6])
            if board[board.index(piece)+6] == "  " or board[board.index(piece)+6] in not_color:
                possible_moves.append(pos[board.index(piece) +6])
            if board[board.index(piece)+10] == "  " or board[board.index(piece)+10] in not_color:
                possible_moves.append(pos[board.index(piece) +10])
            if board[board.index(piece)+17] == "  " or board[board.index(piece)+17] in not_color:
                possible_moves.append(pos[board.index(piece) +17])
            if board[board.index(piece)+15] == "  " or board[board.index(piece)+15] in not_color:
                possible_moves.append(pos[board.index(piece) +15])
        # diagonal moves
        if board.index(piece) % 8 != 0:
            if board.index(piece) > 7:
                if board[board.index(piece) - 9] == "  ":
                    possible_moves.append(pos[board.index(piece)-9])
            if board.index(piece) < 56:
                if board[board.index(piece)+7] == "  ":
                    possible_moves.append(pos[board.index(piece)+7])
        if board.index(piece) % 8 != 7:
            if board.index(piece) > 7:
                if board[board.index(piece) - 7] == "  ":
                    possible_moves.append(pos[board.index(piece)-7])
            if board.index(piece) < 56:
                if board[board.index(piece)+9] == "  ":
                    possible_moves.append(pos[board.index(piece)+9])

    # WHITE BISHOP
    if piece == "b1" or piece == "b2":
        white_bishop_moves(piece,color,not_color)

    # BLACK BISHOP
    if piece == "B1" or piece == "B2":
        black_bishop_moves(piece,color,not_color)

    # ROOKS
    if piece == "r1" or piece == "r2" or piece == "R1" or piece == "R2":
        rook_moves(piece,color,not_color)

    # QUEENS
    if piece == "qu" or piece == "QU":
        rook_moves(piece,color,not_color)
        black_bishop_moves(piece, color, not_color)
        white_bishop_moves(piece, color, not_color)

    # KINGS
    if piece == "ki" or piece == "KI":        # King can only make one move at a time
        if board.index(piece) % 8 != 0:       # I check the conditions and if it's possible it moves
            if board[board.index(piece) - 1] == "  " or board[board.index(piece) - 1] in not_color:      # left
                possible_moves.append(pos[board.index(piece)-1])
            if board.index(piece) > 7:
                if board[board.index(piece) - 9] == "  " or board[board.index(piece) - 9] in not_color:  # left up diagonal
                    possible_moves.append(pos[board.index(piece)-9])
            if board.index(piece) < 56:
                if board[board.index(piece)+7] == "  " or board[board.index(piece)+7] in not_color:      # left down diagonal
                    possible_moves.append(pos[board.index(piece)+7])
        if board.index(piece) % 8 != 7:
            if board[board.index(piece) + 1] == "  " or board[board.index(piece) + 1] in not_color:      # right
                possible_moves.append(pos[board.index(piece)+1])
            if board.index(piece) > 7:
                if board[board.index(piece) - 7] == "  " or board[board.index(piece) - 7] in not_color:  # right up diagonal
                    possible_moves.append(pos[board.index(piece)-7])
            if board.index(piece) < 56:
                if board[board.index(piece)+9] == "  " or board[board.index(piece)+9] in not_color:      # right down diagonal
                    possible_moves.append(pos[board.index(piece)+9])
        pawn_moves(board.index(piece) > 7, -8, piece, color, not_color)     # up
        pawn_moves(board.index(piece) < 56, 8, piece, color, not_color)     # down

    if len(possible_moves) != 0:     # This code is for the kings to not be taken
        for o in possible_moves:
            if board[pos.index(o)] == "KI" or board[pos.index(o)] == "ki":
                possible_moves.remove(o)

    return possible_moves
# If the square it wants to go is in possible moves it can go
def moves(piece,position,color,not_color):
    global board
    if position in showmoves(piece,color,not_color):
        board[board.index(piece)] = "  "
        board[pos.index(position)] = piece
        print("OK")
    else:
        print("FAILED")
    return board
# this for printing commands as strings
def print_instructions(alist):
    print(">", end="")
    print(" ".join([str(elem) for elem in alist]))
# for finding the color of the piece sot it won't take its own piece
def check_color(list):
    global whites, blacks, color, not_color
    if list in whites:
        color = whites
        not_color = blacks
    else:
        color = blacks
        not_color = whites
    return color, not_color
# this where input.txt is considered
def game():
    global board, first_board
    for m in range(len(commands)):
        if commands[m][0] == "initialize":
            print_instructions(commands[m])
            print("OK")
            board = first_board.copy()
            mapping(board)
        elif commands[m][0] == "exit":
            print_instructions(commands[m])
            exit()
        elif commands[m][0] == "print":
            print_instructions(commands[m])
            mapping(board)
        elif commands[m][0] == "showmoves":
            print_instructions(commands[m])
            check_color(commands[m][1])
            showmoves(commands[m][1],color,not_color)
            if len(possible_moves) == 0:
                print("FAILED")
            else:
                print(" ".join(sorted(list(set(possible_moves)))))
        elif commands[m][0] == "move":
            print_instructions(commands[m])
            check_color(commands[m][1])
            moves(commands[m][1],commands[m][2],color,not_color)

game()
















































































































































































































































































































































































































