import numpy


def sudokuSolver(array):
    # try:
    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y] == 0:
                for value in range(1, 10):
                    if checkValues(array, x, y, value):
                        array[x][y] = value
                        # backtracking
    print(array)


def checkValues(array, x, y, value):
    for row in range(9):
        if array[x][row] == value:
            return False
    for column in range(9):
        if array[column][y] == value:
            return False
    if x == 0 or x == 1 or x == 2:
        rowX = [0, 1, 2]
    elif x == 3 or x == 4 or x == 5:
        rowX = [3, 4, 5]
    else:
        rowX = [6, 7, 8]
    if y == 0 or y == 1 or y == 2:
        rowY = [0, 1, 2]
    elif y == 3 or y == 4 or y == 5:
        rowY = [3, 4, 5]
    else:
        rowY = [6, 7, 8]
    for numX in rowX:
        for numY in rowY:
            if array[numX][numY] == value:
                return False
    return True


if __name__ == '__main__':
    array = numpy.array([[0, 0, 2, 0, 1, 5, 0, 7, 8],
                         [1, 8, 0, 0, 6, 3, 4, 0, 0],
                         [0, 0, 4, 0, 2, 0, 5, 6, 1],
                         [0, 9, 6, 0, 0, 7, 0, 3, 0],
                         [0, 1, 0, 3, 0, 6, 0, 0, 5],
                         [0, 0, 3, 2, 0, 4, 0, 9, 6],
                         [0, 3, 0, 0, 0, 0, 0, 0, 0],
                         [6, 4, 9, 8, 3, 0, 2, 0, 7],
                         [0, 0, 7, 0, 0, 0, 0, 1, 0]])
    sudokuSolver(array)
