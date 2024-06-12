"""
Lauren & Aurelia
Checkers Project
Move Execution
Piece Key:
0 - empty slot
1 - player piece
2 - computer/player 2 piece
3 - player king
4 - computer/player 2 king
"""
import random
import turns
board = [[0, 2, 0, 2, 0, 2, 0, 2],
         [2, 0, 2, 0, 0, 0, 2, 0],
         [0, 2, 0, 2, 0, 2, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 2, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0]
         ]

#takes two ints (1,3) or (2,4) and a board and counts pieces on board
def count_pieces(num_1, num_2, board):
    count = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == num_1 or board[x][y] == num_2:
                count += 1
    return count

#tester lists

#takes a movement tuple and a game board (2 dimensional list) and executes the move (also turns piece to king if necessary)      
def move(tup, game_board):
    piece = 0
    computer_pieces = count_pieces(2, 4, board)
    player_pieces = count_pieces(1, 3, board)
    lst = []
    if abs(tup[0] - tup[2]) == 1 and abs(tup[1] - tup[3]) == 1:
        piece = game_board[tup[0]][tup[1]]
        game_board[tup[0]][tup[1]] = 0
        game_board[tup[2]][tup[3]] = piece
    if abs(tup[0] - tup[2]) == 2 and abs(tup[1] - tup[3]) == 2:
        index_out = (tup[0] + tup[2])//2
        index_in = (tup[1] + tup[3])//2
        piece = game_board[tup[0]][tup[1]]
        piece_p = game_board[index_out][index_in]
        game_board[tup[0]][tup[1]] = 0
        game_board[tup[2]][tup[3]] = piece
        game_board[index_out][index_in] = 0
        if piece_p in [2,4]:
            player_pieces -= 1
        if piece_p in [1,3]:
            computer_pieces -= 1
    if (abs(tup[0] - tup[2]) == 4 and abs(tup[1] - tup[3]) == 4) or (abs(tup[0] - tup[2]) == 4 and abs(tup[1] - tup[3]) == 0):
        if game_board[tup[0]][tup[1]] in [1,3]:
            lst = turns.turn_player(game_board)
            for x in lst:
                if x[0] == tup[0] and x[1] == tup[1] and x[2] == tup[2] and x[3] == tup[3]:
                    tup = x
        if game_board[tup[0]][tup[1]] in [2,4]:
            lst = turns.turn_computer(game_board)
            for x in lst:
                if x[0] == tup[0] and x[1] == tup[1] and x[2] == tup[2] and x[3] == tup[3]:
                    tup = x
        index_out = (tup[0] + tup[4])//2
        index_in = (tup[1] + tup[5])//2
        piece = game_board[tup[0]][tup[1]]
        piece_p = game_board[index_out][index_in]
        game_board[tup[0]][tup[1]] = 0
        game_board[tup[4]][tup[5]] = piece
        game_board[index_out][index_in] = 0
        if piece_p in [2,4]:
            computer_pieces -= 1
        if piece_p in [1,3]:
            player_pieces -= 1
        index_out = (tup[2] + tup[4])//2
        index_in = (tup[3] + tup[5])//2
        piece = game_board[tup[4]][tup[5]]
        piece_p = game_board[index_out][index_in]
        game_board[tup[4]][tup[5]] = 0
        game_board[tup[2]][tup[3]] = piece
        game_board[index_out][index_in] = 0
        if piece_p in [2,4]:
            computer_pieces -= 1
        if piece_p in [1,3]:
            player_pieces -= 1
        game_board[tup[2]][tup[3]] = piece
    if tup[2] == 0 and piece == 1:
        game_board[tup[2]][tup[3]] = 3
    if tup[2] == 7 and piece == 2:
        game_board[tup[2]][tup[3]] = 4

if __name__ == "__main__":
    move((5,4,1,4), board)
    for x in board:
        print(x)