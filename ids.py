def depth_limited_search(state, goal, depth, path, visited):
    if state == goal:
        return path

    if depth == 0:
        return None

    visited.add(state)

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero = nr * 3 + nc
            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                result = depth_limited_search(
                    new_state,
                    goal,
                    depth - 1,
                    path + [new_state],
                    visited
                )

                if result is not None:
                    return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        visited = set()

        solution = depth_limited_search(
            start,
            goal,
            depth,
            [start],
            visited
        )

        if solution is not None:
            return solution

        depth += 1


print("Enter initial state:")
start = tuple(map(int, input().split()))

print("Enter goal state:")
goal = tuple(map(int, input().split()))

solution = ids(start, goal)

if solution:
    print("\nSolution:")

    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

    print("Number of moves:", len(solution) - 1)
else:
    print("No solution found")
