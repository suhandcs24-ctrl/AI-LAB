board = [" "] * 9

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def win(p):
    for a,b,c in [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

def minimax(ai):
    if win("O"): return 1
    if win("X"): return -1
    if " " not in board: return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = ai
            scores.append(minimax("X" if ai == "O" else "O"))
            board[i] = " "

    return max(scores) if ai == "O" else min(scores)

def computer():
    best = -2
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax("X")
            board[i] = " "

            if score > best:
                best = score
                move = i

    board[move] = "O"

while True:
    show()
    move = int(input("Your move (1-9): ")) - 1

    if board[move] != " ":
        print("Invalid move")
        continue

    board[move] = "X"

    if win("X"):
        show()
        print("You win!")
        break

    if " " not in board:
        show()
        print("Draw!")
        break

    computer()

    if win("O"):
        show()
        print("AI wins!")
        break
