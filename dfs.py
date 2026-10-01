start = input("Initial state: ")
goal = input("Final state: ")

stack = [(start, 0)]
visited = set()

while stack:
    state, depth = stack.pop()

    if state == goal:
        print("Goal found at depth", depth)
        break

    if state not in visited:
        visited.add(state)
        for i in range(len(state)):
            stack.append((state, depth + 1))
else:
    print("Goal not found")
