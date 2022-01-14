# function that finds a sequence for
# solving the board with less than 100 recursions

import sudoku_Backtracking
import copy
import random

testingGrid = [
    [1, 0, 0, 8, 0, 0, 0, 0, 9],
    [0, 0, 0, 3, 0, 5, 0, 8, 7],
    [3, 9, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 5, 7, 9, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 4, 6, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 1, 5],
    [2, 8, 0, 5, 0, 1, 0, 0, 0],
    [9, 0, 0, 0, 0, 4, 0, 0, 3]]

result = 9999
while result > 100:
    values = list(random.sample(range(1, 10), 9))
    it = [0]
    grid = copy.deepcopy(testingGrid)
    it = sudoku_Backtracking.testingValues(grid, values, it)
    if it[0] < 100:
        result = it[0]
        print("Found a solution with " +
              str(it[0]) + " recursions using the sequence: " + str(values))
