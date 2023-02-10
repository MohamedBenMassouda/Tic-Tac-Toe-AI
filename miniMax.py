import sys

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

scores = {
    'X': -1,
    'O': 1,
    'tie': 0
}


def print_board(board):
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("-----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")


def best_move(board):
    bestScore = -sys.maxsize
    bestMove = [-1, -1]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score, count = miniMax(board, 0, False, 0)
                board[i][j] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = i, j

    print(f"Computer saw: {count} moves")
    return bestMove


def miniMax(board, depth, isMaximizing, count):
    result = game_logic(board)
    if result:
        return scores[result], count

    if isMaximizing:
        bestScore = -sys.maxsize
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score, count = miniMax(board, depth + 1, False, count + 1)
                    board[i][j] = ' '
                    bestScore = max(score, bestScore)

        return bestScore, count

    else:
        bestScore = sys.maxsize
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score, count = miniMax(board, depth + 1, True, count + 1)
                    board[i][j] = ' '
                    bestScore = min(score, bestScore)

        return bestScore, count


def nextTurn(turn):
    if turn == "X":
        return "O"

    return "X"


def play(board, turn):
    available = ["0 0", "0 1", "0 2", "1 0", "1 1", "1 2", "2 0", "2 1", "2 2"]
    count = 0
    while available:
        print(f"Available spots: {available}")
        if turn == 'X':
            row, col = map(int, input("Choose a spot: ").split())
            while f"{row} {col}" not in available:
                row, col = map(int, input("Choose a spot: ").split())

        else:
            row, col = best_move(board)

        print(row, col)
        board[row][col] = turn
        count += 1
        available.remove(f"{row} {col}")
        print_board(board)

        if game_logic(board):
            if count >= 5 and game_logic(board) == turn:
                print(f"{turn} wins")
                available = []

            elif count == 9 and game_logic(board) == 'tie':
                print("It's a tie")

        turn = nextTurn(turn)


def game_logic(board):
    # Checking Cols
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

    # Checking Rows
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Checking Diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False

    return 'tie'


def main():
    print_board(board)
    turn = input("Choose X or O: ")

    while turn not in ["X", "O"]:
        turn = input("Choose X or O: ")

    play(board, turn)


main()
