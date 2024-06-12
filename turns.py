"""
Lauren & Aurelia
Checkers Project
Obtaining movement tuples
Piece Key:
0 - empty slot
1 - player piece
2 - computer piece
3 - player king
4 - computer king
Boolean Values Key:

"""
import random
import computer
computer_pieces = [2,4]
player_pieces = [1,3]
board_practice =[[0, 2, 0, 2, 0, 2, 0, 2],
                 [2, 0, 2, 0, 2, 0, 2, 0],
                 [0, 2, 0, 2, 0, 2, 0, 2],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 1, 0, 1, 0]
                 ]
#takes a list of computer pieces and player pieces and a game board, returns indexes of each piece
def indexes(lst, board):
    inds = []
    for x in range(8):
        for y in range(8):
            if board[x][y] in lst:
                inds.append((x, y))
    return inds

def valid_moves(out_index, in_index, board):
    piece = board[out_index][in_index]
    valids = []
    if piece == 1 or piece == 3:
        lst = turn_player(board)
        for x in lst:
            if x[0] == out_index and x[1] == in_index:
                valids.append((x[2], x[3]))
    if piece == 2 or piece == 4:
        lst = turn_computer(board)
        for x in lst:
            if x[0] == out_index and x[1] == in_index:
                valids.append((x[2], x[3]))
    return valids
#takes a valid list of pieces (ONLY computer_pieces) and returns a list of possible moves for the player or computer
# the returned list has tuples of length 4 or 5, the first two numbers are the outer and inner index of the piece that would be moved
# the third and fourth numbers are the outer and inner indexes the piece would move to, and the fifth number indicates a capture
#or a double capture if present
def turn_computer(board):
    possible_moves = []
    a = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 2 or board[x][y] == 4:
                index_out = x
                index_in = y
                out_1 = index_out - 1 >= 0
                out_2 = index_out - 2 >= 0
                in_1 = index_in - 1 >= 0
                in_2 = index_in - 2 >= 0
                out_3 = index_out - 3 >= 0
                out_4 = index_out - 4 >= 0
                in_3 = index_in - 3 >= 0
                in_4 = index_in - 4 >= 0
                try:
                    if board[index_out + 1][index_in - 1] == 0 and in_1:
                        possible_moves.append((index_out, index_in, index_out + 1, index_in - 1))
                    else:      
                        if not(board[index_out + 1][index_in - 1] in computer_pieces and in_1):
                            if board[index_out + 1][index_in - 1] in player_pieces and board[index_out + 2][index_in - 2] == 0 and in_1 and in_2:
                                possible_moves.append((index_out, index_in, index_out + 2, index_in - 2, 1))
                                if board[index_out + 3][index_in - 3] in player_pieces and board[index_out + 4][index_in - 4] == 0 and in_3 and in_4:
                                    possible_moves.append((index_out, index_in, index_out + 4, index_in - 4, index_out + 2, index_in - 2, 2))
                                if board[index_out + 3][index_in - 1] in player_pieces and board[index_out + 4][index_in] == 0:
                                    possible_moves.append((index_out, index_in, index_out + 4, index_in, index_out + 2, index_in - 2, 2))
                except IndexError:
                    a = 2
                try:
                    if board[index_out + 1][index_in + 1] == 0:
                        possible_moves.append((index_out, index_in, index_out + 1, index_in + 1))
                    else:
                        if not(board[index_out + 1][index_in + 1] in computer_pieces):
                            if board[index_out + 1][index_in + 1] in player_pieces and board[index_out + 2][index_in + 2] == 0:
                                possible_moves.append((index_out, index_in, index_out + 2, index_in + 2, 1))
                                if board[index_out + 3][index_in + 3] in player_pieces and board[index_out + 4][index_in + 4] == 0:
                                    possible_moves.append((index_out, index_in, index_out + 4, index_in + 4, index_out + 2, index_in + 2, 2))
                                if board[index_out + 3][index_in + 1] in player_pieces and board[index_out + 4][index_in] == 0:
                                    possible_moves.append((index_out, index_in, index_out + 4, index_in, index_out + 2, index_in + 2, 2))
                except IndexError:
                    a = 2
                if board[x][y] == 4:
                    try:
                        if board[index_out - 1][index_in - 1] == 0 and out_1 and in_1:
                            possible_moves.append((index_out, index_in, index_out - 1, index_in - 1))
                        else:
                            if not(board[index_out - 1][index_in - 1] in computer_pieces and out_1 and in_1):
                                if board[index_out - 1][index_in - 1] in player_pieces and board[index_out - 2][index_in - 2] == 0 and out_1 and in_1 and out_2 and in_2:
                                    possible_moves.append((index_out, index_in, index_out - 2, index_in - 2, 1))
                                    if board[index_out - 3][index_in - 3] in player_pieces and board[index_out - 4][index_in - 4] == 0 and out_3 and in_3 and out_4 and in_4:
                                        possible_moves.append((index_out, index_in, index_out - 4, index_in - 4, index_out - 2, index_in - 2,  2))
                                    if board[index_out - 3][index_in - 1] in player_pieces and board[index_out - 4][index_in] == 0 and out_3 and out_4:
                                        possible_moves.append((index_out, index_in, index_out - 4, index_in, index_out - 2, index_in - 2, 2))
                    except IndexError:
                        a = 2
                    try:
                        if board[index_out - 1][index_in + 1] == 0 and out_1:
                            possible_moves.append((index_out, index_in, index_out - 1, index_in + 1))
                        else:
                            if not(board[index_out - 1][index_in + 1] in computer_pieces and out_1):
                                if board[index_out - 1][index_in + 1] in player_pieces and board[index_out - 2][index_in + 2] == 0 and out_1 and out_2:
                                    possible_moves.append((index_out, index_in, index_out - 2, index_in + 2, 1))
                                    if board[index_out - 3][index_in + 3] in player_pieces and board[index_out - 4][index_in + 4] == 0 and out_3 and out_4:
                                        possible_moves.append((index_out, index_in, index_out - 4, index_in + 4, index_out - 2, index_in + 2, 2))
                                    if board[index_out - 3][index_in + 1] in player_pieces and board[index_out - 4][index_in] == 0 and out_3 and out_4:
                                        possible_moves.append((index_out, index_in, index_out - 4, index_in, index_out - 2, index_in + 2, 2))
                    except IndexError:
                        a = 2
    return possible_moves

 
#same as turn_computer but for the player
def turn_player(board):
    a = 0
    possible_moves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] == 1 or board[x][y] == 3:
                index_out = x
                index_in = y
                out_1 = index_out - 1 >= 0
                out_2 = index_out - 2 >= 0
                in_1 = index_in - 1 >= 0
                in_2 = index_in - 2 >= 0
                out_3 = index_out - 3 >= 0
                out_4 = index_out - 4 >= 0
                in_3 = index_in - 3 >= 0
                in_4 = index_in - 4 >= 0
                try:
                    if board[index_out - 1][index_in + 1] == 0 and out_1:
                        possible_moves.append((index_out, index_in, index_out - 1, index_in + 1))
                    else:
                        if not(board[index_out - 1][index_in + 1] in player_pieces and out_1):
                            if board[index_out - 1][index_in + 1] in computer_pieces and board[index_out - 2][index_in + 2] == 0 and out_1 and out_2:
                                possible_moves.append((index_out, index_in, index_out - 2, index_in + 2, 1))
                                if board[index_out - 3][index_in + 3] in computer_pieces and board[index_out - 4][index_in + 4] == 0 and out_3 and out_4:
                                    possible_moves.append((index_out, index_in, index_out - 4, index_in + 4, index_out - 2, index_in + 2, 2))
                                if board[index_out - 3][index_in + 1] in computer_pieces and board[index_out - 4][index_in] == 0 and out_3 and out_4:
                                    possible_moves.append((index_out, index_in, index_out - 4, index_in, index_out - 2, index_in + 2, 2))
                except IndexError:
                    a = 2
                try:
                    if board[index_out - 1][index_in - 1] == 0 and out_1 and in_1:
                        possible_moves.append((index_out, index_in, index_out - 1, index_in - 1))
                    else:
                        if not(board[index_out - 1][index_in - 1] in player_pieces and out_1 and in_1):
                            if board[index_out - 1][index_in - 1] in computer_pieces and board[index_out - 2][index_in - 2] == 0 and out_1 and in_1 and out_2 and in_2:
                                possible_moves.append((index_out, index_in, index_out - 2, index_in - 2, 1))
                                if board[index_out - 3][index_in - 3] in computer_pieces and board[index_out - 4][index_in - 4] == 0 and out_3 and out_4 and in_3 and in_4:
                                    possible_moves.append((index_out, index_in, index_out - 4, index_in - 4, index_out - 2, index_in - 2, 2))
                                if board[index_out - 3][index_in - 1] in computer_pieces and board[index_out - 4][index_in] == 0 and out_3 and out_4:
                                    possible_moves.append((index_out, index_in, index_out - 4, index_in, index_out - 2, index_in - 2, 2))
                except IndexError:
                    a = 2
                if board[x][y] == 3:
                    try:
                        if board[index_out + 1][index_in - 1] == 0 and in_1:
                            possible_moves.append((index_out, index_in, index_out + 1, index_in - 1))
                        else:
                            if not(board[index_out + 1][index_in - 1] in player_pieces and in_1):
                                if board[index_out + 1][index_in - 1] in computer_pieces and board[index_out + 2][index_in - 2] == 0 and in_1 and in_2:
                                    possible_moves.append((index_out, index_in, index_out + 2, index_in - 2, 1))
                                    if board[index_out + 3][index_in - 3] in computer_pieces and board[index_out + 4][index_in - 4] == 0 and in_3 and in_4:
                                        possible_moves.append((index_out, index_in, index_out - 4, index_in - 4, index_out + 2, index_in - 2, 2))
                                    if board[index_out + 3][index_in - 1] in computer_pieces and board[index_out + 4][index_in] == 0:
                                        possible_moves.append((index_out, index_in, index_out + 4, index_in, index_out + 2, index_in - 2, 2))
                    except IndexError:
                        a = 2
                    try:
                        if board[index_out + 1][index_in + 1] == 0:
                            possible_moves.append((index_out, index_in, index_out + 1, index_in + 1))
                        else:
                            if not(board[index_out + 1][index_in + 1] in player_pieces):
                                if board[index_out + 1][index_in + 1] in computer_pieces and board[index_out + 2][index_in + 2] == 0:
                                    possible_moves.append((index_out, index_in, index_out + 2, index_in + 2, 1))
                                    if board[index_out + 3][index_in + 3] in computer_pieces and board[index_out + 4][index_in + 4] == 0:
                                        possible_moves.append((index_out, index_in, index_out + 4, index_in + 4, index_out + 2, index_in + 2, 2))
                                    if board[index_out + 3][index_in + 1] in computer_pieces and board[index_out + 4][index_in] == 0:
                                        possible_moves.append((index_out, index_in, index_out + 4, index_in,  index_out + 2, index_in + 2, 2))
                    except IndexError:
                        a = 2
    return possible_moves

if __name__ == "__main__":
    print(turn_player(board_practice))
    print(turn_computer(board_practice))
    print(valid_moves(3, 6, board_practice))