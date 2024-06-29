import numpy as np

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def make_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'X'):
        return -10 + depth
    if check_win(board, 'O'):
        return 10 - depth
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    ai_player = 'O'
    current_player = 'X'
    
    while True:
        print_board(board)
        if current_player == human_player:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if not make_move(board, row, col, human_player):
                print("Invalid move, try again.")
                continue
        else:
            row, col = best_move(board)
            make_move(board, row, col, ai_player)
            print(f"AI played at: ({row}, {col})")
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

play_game()
