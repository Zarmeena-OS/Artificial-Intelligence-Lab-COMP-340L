import heapq


def manhattan_distance(a, b):
    """Computes the Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_unweighted(grid, start, goal):
    """
    A* algorithm for an unweighted graph where movement cost is uniform.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    open_set = []
    heapq.heappush(open_set, (0, start))  # (f-score, node)

    g_score = {start: 0}
    came_from = {}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path

        x, y = current
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1  # Uniform cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
                    came_from[neighbor] = current

    return None  # No path found


def reconstruct_path(came_from, current):
    """Reconstructs the path from the goal to the start."""
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


# Example grid (0 = open, 1 = obstacle)
grid_unweighted = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

start = (0, 0)
goal = (3, 3)

path_unweighted = a_star_unweighted(grid_unweighted, start, goal)
print("Shortest Path (Unweighted Graph):", path_unweighted)
