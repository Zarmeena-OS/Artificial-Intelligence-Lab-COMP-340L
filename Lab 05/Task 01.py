# Function to Evaluate the Board
def evaluate_state(grid):
    """
    Analyzes the board and returns a score.
    """
    winning_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]

    for a, b, c in winning_patterns:
        if grid[a] == grid[b] == grid[c] and grid[a] != " ":
            return 1 if grid[a] == "X" else -1  # AI (+1) / Human (-1)

    if " " not in grid:
        return 0  # Draw

    return None  # Game is still active


# Function for Human Player's Best Move
def human_strategy(grid):
    """
    Determines the optimal move for the player minimizing the AI's score.
    """
    game_result = evaluate_state(grid)
    if game_result is not None:
        return game_result

    optimal_value = float("inf")
    for index in range(9):
        if grid[index] == " ":
            grid[index] = "O"  # Simulating human move
            optimal_value = min(optimal_value, ai_strategy(grid))
            grid[index] = " "  # Undo move

    return optimal_value


# Function for AI's Best Move
def ai_strategy(grid):
    """
    Determines the best move for the AI maximizing its own score.
    """
    game_result = evaluate_state(grid)
    if game_result is not None:
        return game_result

    best_value = float("-inf")
    for index in range(9):
        if grid[index] == " ":
            grid[index] = "X"  # Simulating AI move
            best_value = max(best_value, human_strategy(grid))
            grid[index] = " "  # Undo move

    return best_value


# Minimax Algorithm to Find Best Move for AI
def best_move(grid):
    """
    Implements Minimax to find the most favorable move for AI.
    """
    top_score = float("-inf")
    chosen_move = -1

    for index in range(9):
        if grid[index] == " ":
            grid[index] = "X"  # AI move simulation
            move_score = human_strategy(grid)
            grid[index] = " "  # Undo move

            if move_score > top_score:
                top_score = move_score
                chosen_move = index

    return chosen_move


# Function to Display the Board
def show_board(grid):
    """
    Prints the Tic-Tac-Toe grid.
    """
    print("\n")
    print(f"{grid[0]} | {grid[1]} | {grid[2]}")
    print("--+---+--")
    print(f"{grid[3]} | {grid[4]} | {grid[5]}")
    print("--+---+--")
    print(f"{grid[6]} | {grid[7]} | {grid[8]}")
    print("\n")


# Game Execution Function
def start_game():
    """
    Runs the Tic-Tac-Toe game loop.
    """
    grid = [" "] * 9
    user_turn = True  # Human starts

    while True:
        show_board(grid)

        if evaluate_state(grid) == 1:
            print("AI is the Winner!")
            break
        elif evaluate_state(grid) == -1:
            print("Congratulations! You Win!")
            break
        elif evaluate_state(grid) == 0:
            print("It's a Tie!")
            break

        if user_turn:
            try:
                user_move = int(input("Select your position (0-8): "))
                if grid[user_move] == " ":
                    grid[user_move] = "O"
                    user_turn = False
                else:
                    print("Invalid choice! Try again.")
            except (ValueError, IndexError):
                print("Enter a valid position (0-8).")
        else:
            print("AI is making a move...")
            ai_decision = best_move(grid)
            if ai_decision != -1:
                grid[ai_decision] = "X"
                user_turn = True
            else:
                print("Unexpected error: No valid move found!")


# Launch the Game
start_game()






