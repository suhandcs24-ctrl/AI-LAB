
import heapq

class PuzzleState:
    def __init__(self, board, g=0, h=0, parent=None):
        self.board = tuple(board)
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(self.board)

def get_misplaced_tiles(state_board, goal_board):
    count = 0

    for i in range(len(state_board)):
        if state_board[i] != 0 and state_board[i] != goal_board[i]:
            count += 1

    return count

def get_neighbors(state):
    neighbors = []

    board = list(state.board)
    blank = board.index(0)

    row = blank // 3
    col = blank % 3

    moves = []

    if row > 0:
        moves.append(-3)      # Up
    if row < 2:
        moves.append(3)       # Down
    if col > 0:
        moves.append(-1)      # Left
    if col < 2:
        moves.append(1)       # Right

    for move in moves:
        new_board = board.copy()

        new_board[blank], new_board[blank + move] = \
            new_board[blank + move], new_board[blank]

        neighbors.append(PuzzleState(new_board))

    return neighbors

def a_star_misplaced(start_board, goal_board):

    start = PuzzleState(start_board)

    start.h = get_misplaced_tiles(start.board, goal_board)
    start.f = start.g + start.h

    open_list = []
    heapq.heappush(open_list, start)

    open_dict = {start.board: start.g}
    closed = set()

    while open_list:

        current = heapq.heappop(open_list)

        if current.board in open_dict:
            if open_dict[current.board] == current.g:
                del open_dict[current.board]

        # Goal reached
        if current.board == tuple(goal_board):

            path = []

            while current:
                path.append(current.board)
                current = current.parent

            return path[::-1]

        closed.add(current.board)

        for neighbor in get_neighbors(current):

            if neighbor.board in closed:
                continue

            new_g = current.g + 1

            if (neighbor.board in open_dict and
                    open_dict[neighbor.board] <= new_g):
                continue

            neighbor.g = new_g
            neighbor.h = get_misplaced_tiles(
                neighbor.board,
                goal_board
            )
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current

            heapq.heappush(open_list, neighbor)
            open_dict[neighbor.board] = new_g

    return None

# ---------------------------------------
# INITIAL STATE
# ---------------------------------------

start = [
    2, 8, 3,
    1, 6, 4,
    7, 0, 5
]

# ---------------------------------------
# GOAL STATE
# ---------------------------------------

goal = [
    1, 2, 3,
    8, 0, 4,
    7, 6, 5
]

# ---------------------------------------
# RUN A*
# ---------------------------------------

solution = a_star_misplaced(start, goal)

# ---------------------------------------
# PRINT RESULT
# ---------------------------------------

if solution:

    print("Initial State:")
    print("2 8 3")
    print("1 6 4")
    print("7 0 5")

    print("\nGoal State:")
    print("1 2 3")
    print("8 0 4")
    print("7 6 5")

    print("\nHeuristic h(n) =", get_misplaced_tiles(start, goal))

    print("\nSolution:")
    print("Number of moves =", len(solution) - 1)

    for i, board in enumerate(solution):

        print("\nStep", i)

        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

        print("h(n) =", get_misplaced_tiles(board, goal))

else:
    print("No solution")
