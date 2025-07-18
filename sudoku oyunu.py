board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Tahtayı ekrana yazdıran fonksiyon
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Sudoku tahtasını fonksiyon
def solve_board(board, find_empty=None):
    # Tahta dolu mu diye kontrol et
    empty_pos = find_empty(board)
    if not empty_pos:
        return True
    else:
        row, col = empty_pos  #satır, stun

    # Boş hücreyi dene
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve_board(board):
                return True
            board[row][col] = 0

    return False


# Belirli hücreye sayı yerleştirilip yerleştirilemeyeceğini kontrol eden fonksiyonun kodu
def is_valid(board, num, pos):
    # Aynı satırda aynı sayı yok mu diye kontrol eder
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Aynı sütunda aynı sayı yok mu diye kontrol eder
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # 3x3'lük kutuda aynı sayı yok mu diye kontrol eder
    box_row = pos[0] // 3   # // anlamı .....
    box_col = pos[1] // 3

    for i in range(box_row * 3,
                   box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

print_board(board)