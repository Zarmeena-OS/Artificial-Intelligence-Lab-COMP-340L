import heapq


def manhattan_distance(node, goal):
    """Compute the Manhattan distance heuristic."""
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def a_star(grid, start, goal):
    """
    Implements the A* algorithm to find the shortest path in a 2D grid with obstacles.

    Parameters:
    grid  : List[List[int]]  → 2D grid where 0 = open space, 1 = obstacle
    start : Tuple[int, int]  → (x, y) starting coordinates
    goal  : Tuple[int, int]  → (x, y) goal coordinates

    Returns:
    path  : List[Tuple[int, int]] → The shortest path as a list of coordinates, or empty if no path.
    """

    # Grid dimensions
    rows, cols = len(grid), len(grid[0])

    # Possible movements (Up, Down, Left, Right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Priority queue (Min-Heap) for A* search
    open_list = []
    heapq.heappush(open_list, (0, start))  # (f-score, (x, y))

    # Dictionaries to store cost and parent path
    g_score = {start: 0}  # Cost from start to each node
    came_from = {}  # Store parent nodes to reconstruct path

    while open_list:
        _, current = heapq.heappop(open_list)  # Get node with lowest f-score

        # Goal check
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse to get path from start to goal

        x, y = current
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)

            # Ensure within grid bounds
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue

            # Skip obstacles
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue

            # Compute new g-score
            tentative_g_score = g_score[current] + 1  # Cost is always 1 per move

            # If new path is better, update
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current  # Track path

    return []  # Return empty if no path exists


# Example Usage
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)  # Top-left corner
    goal = (4, 4)  # Bottom-right corner

    path = a_star(grid, start, goal)
    print("Shortest Path:", path)
