import math


# Tic-Tac-Toe board setup
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]


# Function to print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)


# Check if game is over
def is_terminal(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


# Function to evaluate board state
def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 10
            elif row[0] == 'O':
                return -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10
    return 0


# Get valid moves
def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']


# Apply a move
def make_move(board, move, player):
    new_board = [row[:] for row in board]
    new_board[move[0]][move[1]] = player
    return new_board


# Alpha-Beta Pruning Algorithm
def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    if is_terminal(board) or depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in get_valid_moves(board):
            new_board = make_move(board, move, 'X')
            eval = alpha_beta_pruning(new_board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_valid_moves(board):
            new_board = make_move(board, move, 'O')
            eval = alpha_beta_pruning(new_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# Minimax function
def minimax(board, depth, maximizing_player):
    best_move = None
    if maximizing_player:
        max_eval = -math.inf
        for move in get_valid_moves(board):
            new_board = make_move(board, move, 'X')
            eval = alpha_beta_pruning(new_board, depth - 1, -math.inf, math.inf, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
    else:
        min_eval = math.inf
        for move in get_valid_moves(board):
            new_board = make_move(board, move, 'O')
            eval = alpha_beta_pruning(new_board, depth - 1, -math.inf, math.inf, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
    return best_move


# Main game loop
def play_tic_tac_toe():
    board = create_board()
    while not is_terminal(board):
        print_board(board)
        human_move = tuple(map(int, input("Enter row and column (0-2): ").split()))
        board = make_move(board, human_move, 'O')
        if is_terminal(board):
            break
        computer_move = minimax(board, 3, True)
        board = make_move(board, computer_move, 'X')
    print_board(board)
    print("Game Over!")


# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()
