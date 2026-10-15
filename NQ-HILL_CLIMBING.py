import random

def calculate_cost(state):
    h = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                h += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

def get_neighbors(state):
    neighbors = []
    n = len(state)

    for col in range(n):
        for row in range(n):
            if row != state[col]:
                neighbor = list(state)
                neighbor[col] = row
                neighbors.append(neighbor)

    random.shuffle(neighbors)
    return neighbors

def hill_climbing_4_queens():
    restart_count = 0

    while True:
        current_state = [random.randint(0, 3) for _ in range(4)]
        current_cost = calculate_cost(current_state)
        restart_count += 1

        visited = {tuple(current_state)}

        print(f"\nRestart #{restart_count}")
        print(f"Initial State: {current_state}, h = {current_cost}")

        step = 1
        max_steps = 5

        while current_cost != 0 and step <= max_steps:
            neighbors = get_neighbors(current_state)

            # Select the best unvisited neighbor
            unvisited = [
                neighbor for neighbor in neighbors
                if tuple(neighbor) not in visited
            ]

            if not unvisited:
                print("No unvisited neighbors. Restarting...")
                break

            best_neighbor = min(unvisited, key=calculate_cost)
            best_cost = calculate_cost(best_neighbor)

            print(f"\nStep {step}:")
            print(f"Current State: {current_state}, h = {current_cost}")
            print(f"Chosen Next State: {best_neighbor}, h = {best_cost}")

            current_state = best_neighbor
            current_cost = best_cost
            visited.add(tuple(current_state))
            step += 1

        if current_cost == 0:
            print(f"\nSolution Found: {current_state}, h = 0")
            return current_state

        if step > max_steps:
            print("\nFive steps completed. Restarting...")

def print_board(state):
    print("\nFinal Board:")
    for row in range(4):
        print(" ".join(
            "Q" if state[col] == row else "."
            for col in range(4)
        ))

if __name__ == "__main__":
    solution = hill_climbing_4_queens()
    print_board(solution)
