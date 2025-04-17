"""
Consider a simple grid world with the following properties:
•⁠  ⁠The grid is 4x4 (4 rows and 4 columns).
•⁠  ⁠The agent can take four possible actions in each state: up, down, left, or right.
•⁠  ⁠The goal is located at position (3, 3), and the agent receives a reward of 1 for reaching the goal and 0 for all other positions.
•⁠  ⁠The agent's objective is to find the optimal policy that maximizes long-term rewards using Value Iteration.
Given this scenario:
1.⁠ ⁠What is the purpose of the get_next_state function in the grid world?
2.⁠ ⁠What is the significance of the discount factor (gamma) set to 0.9 in this scenario?
3.⁠ ⁠Explain how the Value Iteration process works and how it contributes to finding the optimal policy in this grid world example.
4.⁠ ⁠What is the resulting value function (V), and what does it represent?
5.⁠ ⁠Based on the final output of the optimal policy, how should the agent navigate the grid to reach the goal?
"""

import numpy as np

# Grid size and parameters
grid_size = 4
gamma = 0.9  # Discount factor
actions = {'up': (-1, 0),
           'down': (1, 0),
           'left': (0, -1),
           'right': (0, 1)}


def is_valid(state):
    """Check if the next state is within the grid"""
    return 0 <= state[0] < grid_size and 0 <= state[1] < grid_size


def value_iteration(threshold=1e-4):
    """Performs Value Iteration to compute optimal values and policy."""
    V = np.zeros((grid_size, grid_size))  # Initialize value table
    policy = np.full((grid_size, grid_size), '', dtype=object)  # Initialize policy table
    goal_state = (grid_size - 1, grid_size - 1)

    while True:
        delta = 0
        for i in range(grid_size):
            for j in range(grid_size):
                if (i, j) == goal_state:
                    continue  # Skip goal state

                max_value = float('-inf')
                best_action = None

                for action, (di, dj) in actions.items():
                    next_state = (i + di, j + dj)
                    if is_valid(next_state):
                        reward = 1 if next_state == goal_state else 0
                        value = reward + gamma * V[next_state]
                        if value > max_value:
                            max_value = value
                            best_action = action

                delta = max(delta, abs(V[i, j] - max_value))
                V[i, j] = max_value
                policy[i, j] = best_action

        if delta < threshold:
            break

    return V, policy


# Run Value Iteration
V, policy = value_iteration()
print("Optimal State Values:")
print(V)
print("\nOptimal Policy:")
print(policy)

