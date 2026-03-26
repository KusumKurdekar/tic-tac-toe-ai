board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")


def player_move():
    while True:
        move = input("Enter position (1-9): ")

        if not move.isdigit():
            print("Enter a number!")
            continue

        move = int(move) - 1

        if move < 0 or move > 8:
            print("Invalid position!")
            continue

        if board[move] != " ":
            print("Spot already taken!")
            continue

        board[move] = "X"
        break


def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


def is_draw():
    return " " not in board


def minimax(b, is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -1000
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


while True:
    print_board()
    player_move()

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

    if is_draw():
        print_board()
        print("Draw!")
        break