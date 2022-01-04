
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]


def sudokuSolver(g, it):
    find = find_empty(g)
    if not find:
        return True, it
    else:
        row, col = find

    it[0] += 1

    for i in range(1, 10):
        if isValid(g, i, (row, col)):
            g[row][col] = i

            if sudokuSolver(g, it):
                return True, it

            g[row][col] = 0

    return False


def isValid(g, num, pos):
    # verify if 'num' is valid in a specific 'pos(row,col)'

    # number of elements in each row/column
    aux = len(g)

    # Check each row
    for i in range(aux):
        if g[pos[0]][i] == num and pos[1] != i:
            return False

    # Check each column
    for i in range(aux):
        if g[i][pos[1]] == num and pos[0] != i:
            return False

    # Check each square
    sx = pos[1] // 3
    sy = pos[0] // 3

    for i in range(sy*3, sy*3 + 3):
        for j in range(sx * 3, sx*3 + 3):
            if g[i][j] == num and (i, j) != pos:
                return False

    return True


def printSudokuGrid(g):
    # print sudoku grid
    aux = len(g)
    for i in range(aux):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(aux):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(g[i][j])
            else:
                print(str(g[i][j]) + " ", end="")


def find_empty(g):
    # find '0' values and return its position
    aux = len(g)
    for i in range(aux):
        for j in range(aux):
            if g[i][j] == 0:
                return (i, j)  # row, col

    return None


if __name__ == "__main__":
    print("\n\nSudoku Initial Grid\n")
    printSudokuGrid(grid)
    it = [0]
    success, it = sudokuSolver(grid, it)
    if success:
        print("Sudoku grid solved with " +
              str(it[0]) + " iterations.")
        print("\n\nSudoku Solved\n")
        printSudokuGrid(grid)
    else:
        print("\n\nNo solution founded")
