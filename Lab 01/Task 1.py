from collections import deque

# Possible moves (Up, Down, Left, Right) with index shifts in a 1D list
MOVES = {
    'Up': -3,
    'Down': 3,
    'Left': -1,
    'Right': 1
}


def get_blank_position(state):
    """Finds the index of the blank tile (0)."""
    return state.index(0)


def move_blank(state, move):
    """Moves the blank tile and returns a new state if valid, otherwise None."""
    blank_index = get_blank_position(state)
    new_index = blank_index + MOVES[move]

    # Ensure the move is valid within bounds
    row, col = divmod(blank_index, 3)
    new_row, new_col = divmod(new_index, 3)
    if 0 <= new_row < 3 and 0 <= new_col < 3:
        new_state = list(state)
        new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
        return new_state
    return None


def get_neighbors(state):
    """Returns a list of possible new states and their corresponding moves."""
    neighbors = []
    for move in MOVES:
        new_state = move_blank(state, move)
        if new_state:
            neighbors.append((new_state, move))
    return neighbors


def depth_limited_search(state, goal, depth, path, visited):
    """Performs depth-limited DFS."""
    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(tuple(state))

    for neighbor, move in get_neighbors(state):
        if tuple(neighbor) not in visited:
            result = depth_limited_search(neighbor, goal, depth - 1, path + [move], visited)
            if result:
                return result

    return None


def iterative_deepening_dfs(initial, goal):
    """Runs IDDFS with increasing depth limit until solution is found."""
    depth = 0
    while True:
        visited = set()
        result = depth_limited_search(initial, goal, depth, [], visited)
        if result:
            return result
        depth += 1


# Define initial and goal states
initial_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]  # 0 represents the blank tile
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

# Solve the puzzle
solution = iterative_deepening_dfs(initial_state, goal_state)

# Print the solution
if solution:
    print("Solution found!")
    print("Moves:", solution)
else:
    print("No solution found.")