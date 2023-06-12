def is_safe(board, row, col):
    # Sprawdzenie wiersza
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Sprawdzenie górnej przekątnej
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Sprawdzenie dolnej przekątnej
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens(board, col + 1):
                return True

            board[i][col] = 0

    return False


def print_solution(board):
    for row in board:
        print(row)


def solve_n_queens_problem(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens(board, 0):
        print("Brak rozwiązania")
    else:
        print_solution(board)


# Przykład użycia
n = 16
solve_n_queens_problem(n)
