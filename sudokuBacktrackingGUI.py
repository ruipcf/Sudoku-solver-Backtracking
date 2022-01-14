from decimal import HAVE_THREADS
import pygame
import random

# windows settings
sizeWin = (550, 550)
background_color = (255, 255, 255)  # white
firstColor = (0, 200, 0)  # green
buffer = 5

grid = [
    [1, 0, 0, 8, 0, 0, 0, 0, 9],
    [0, 0, 0, 3, 0, 5, 0, 8, 7],
    [3, 9, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 5, 7, 9, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 4, 6, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 1, 5],
    [2, 8, 0, 5, 0, 1, 0, 0, 0],
    [9, 0, 0, 0, 0, 4, 0, 0, 3]]


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


def find_empty(g):
    # find '0' values and return its position
    aux = len(g)
    for i in range(aux):
        for j in range(aux):
            if g[i][j] == 0:
                return (i, j)  # row, col

    return None


def sudokuSolver(win, values, g, it):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    find = find_empty(g)
    if not find:
        return True, it
    else:
        row, col = find

    it[0] += 1

    for i in values:
        if isValid(g, i, (row, col)):
            g[row][col] = i
            pygame.draw.rect(win, background_color, ((
                col+1)*50 + buffer, (row+1)*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
            value = myfont.render(str(i), True, (0, 0, 0))
            win.blit(value, ((col+1)*50 + 15, (row+1)*50))

            # draw a rectangle to clean the area where recursion text will be shown
            rect = (0, 510, 550, 550)
            win.fill((255, 255, 255), rect)
            text = "Recursions: " + str(it[0])
            text = myfont.render(text, True, (0, 0, 0))
            win.blit(text, (50, 500))

            pygame.time.delay(5)
            pygame.display.update()

            if sudokuSolver(win, values, g, it):
                text = str("Solved")
                text = myfont.render(text, True, (0, 255, 0))
                win.blit(text, (400, 500))
                pygame.display.update()
                return True, it

            it[0] += 1

            g[row][col] = 0
            pygame.draw.rect(win, background_color, ((
                col+1)*50 + buffer, (row+1)*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
            pygame.display.update()
            pygame.time.delay(5)

    return False


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode(sizeWin)
    pygame.display.set_caption("Sudoku solver using Backtracking algorithm")
    win.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    # draw grid 9x9 with 50x50px squares
    for i in range(0, 10):
        if(i % 3 == 0):
            # draw bold lines
            pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50),
                             (50 + 50*i, 500), 4)
            pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i),
                             (500, 50 + 50*i), 4)

        pygame.draw.line(win, (0, 0, 0), (50 + 50*i, 50), (50 + 50*i, 500), 2)
        pygame.draw.line(win, (0, 0, 0), (50, 50 + 50*i), (500, 50 + 50*i), 2)
    pygame.display.update()

    # draw the start sudoku grid
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0 < grid[i][j] < 10):
                value = myfont.render(
                    str(grid[i][j]), True, firstColor)
                win.blit(value, ((j+1)*50 + 15, (i+1)*50))
    pygame.display.update()

    it = [0]
    # sequence got using function to find a solution with less than 100 recursions
    values = (9, 5, 3, 8, 4, 7, 6, 1, 2)

    success, it = sudokuSolver(win, values, grid, it)
    if success:
        print("Sudoku grid solved with " + str(it[0]) + " iterations.")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
