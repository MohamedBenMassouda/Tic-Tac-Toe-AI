board: list = [1, 2, 3,
               4, 5, 6,
               7, 8, 9]

def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def check_winner():
    if board[0] == board[1] == board[2]:
        return board[0]
    elif board[3] == board[4] == board[5]:
        return board[3]
    elif board[6] == board[7] == board[8]:
        return board[6]
    elif board[0] == board[3] == board[6]:
        return board[0]
    elif board[1] == board[4] == board[7]:
        return board[1]
    elif board[2] == board[5] == board[8]:
        return board[2]
    elif board[0] == board[4] == board[8]:
        return board[0]
    elif board[2] == board[4] == board[6]:
        return board[2]

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if i in board:
            return False

    return "Draw"


def best_move():
    bestScore = -1000
    bestMove = 0

    for i in range(1, 10):
        if board[i - 1] == "X" or board[i - 1] == "O":
            continue

        board[i - 1] = "O"
        score = miniMax(board, 0, False)
        board[i - 1] = i
        if score > bestScore:
            bestScore = score
            bestMove = i

    return bestMove


def miniMax(board, depth, isMaximizing):
    result = check_winner()
    if result:
        if result == "X":
            return -1
        elif result == "O":
            return 1
        elif result == "Draw":
            return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(1, 10):
            if board[i - 1] == "X" or board[i - 1] == "O":
                continue

            board[i - 1] = "O"
            score = miniMax(board, depth + 1, False)
            board[i - 1] = i
            bestScore = max(score, bestScore)

        return bestScore

    else:
        bestScore = 1000
        for i in range(1, 10):
            if board[i - 1] == "X" or board[i - 1] == "O":
                continue

            board[i - 1] = "X"
            score = miniMax(board, depth + 1, True)
            board[i - 1] = i
            bestScore = min(score, bestScore)

        return bestScore


def next_turn(turn): # X -> O, O -> X
    if turn == "X":
        return "O"

    return "X"

def play_game():
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = "X"
    count = 0
    while available:
        if turn == 'X':
            print_board()
            place = int(input("Enter a number: "))
            while place not in available:
                place = int(input("Enter a number: "))

        else:
            place = best_move()

        available.remove(place)
        board[place - 1] = turn
        count += 1

        if check_winner():
            if count >= 5 and check_winner() == turn:
                print_board()
                print(f"{turn} wins!")
                available = []
                break

            elif check_winner() == "Draw" and count == 9:
                print("Draw!")
                available = []
                break

        turn = next_turn(turn)
        print()

    else:
        print_board()
        if check_winner() == "Draw":
            print("Draw!")


play_game()