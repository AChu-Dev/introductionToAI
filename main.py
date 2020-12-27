import tensorflow as tf
import gui
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model as lm

print('TensorFlow version: ', tf.__version__)




def dataChecker(array):
    global variableArray
    variableArray = []
    #try:
    for x in range(9):
        if len(array[x]) != 9 or len(array) != 9:
            print("Not sufficent number of arrays")
            break
        for y in range(9):
            if array[x][y] < 0 or array[x][y] > 9:
                print("Values incorrect")
                break
    else:       # change due to break statement so it does not continue
         findEmptySpace(array)
    # except Exception:
    #     print("Exception has occured:", Exception)
    # try:
    #     leftPointer = 0
    #     levelPointer = 0
    #     while levelPointer == 8 and leftPointer == 8:
    #         if leftPointer == 8:
    #             leftPointer = 0
    #             levelPointer += 1
    #         if array[levelPointer][leftPointer] < 0 or array[levelPointer][leftPointer] > 9:
    #             return False
    #     return True
    # except NameError:
    #     return NameError


def findEmptySpace(array):
    for x in range(len(array)):
        for y in range(len(array)):
            if array[x][y] == 0:
                fillEmptySpace(array, x, y)
    else:
        print(array)


def fillEmptySpace(array, x, y, startPoint=1):
    for var in range(startPoint, 10):
        if not checkSubGrid(array, x, var) or not checkRow(array, x, y, var) or not checkColumn(array, x, y, var):
            var += 1
        else:
            array[x][y] = var
            save([x, y, var])
            break
    else: # break and else statement issue
        backtrack(array)


def checkSubGrid(array, x, variable):
    for y in range(9):
        if array[x][y] == variable:
            return False
    else:
        return True


def checkRow(array, x, y, variable):
    if x == 0 or x == 1 or x == 2:
        rowX = [0, 1, 2]
    elif x == 3 or x == 4 or x == 5:
        rowX = [3, 4, 5]
    elif x == 6 or x == 7 or x == 8:
        rowX = [6, 7, 8]

    if y == 0 or y == 1 or y == 2:
        rowY = [0, 1, 2]
    elif y == 3 or y == 4 or y == 5:
        rowY = [3, 4, 5]
    elif y == 6 or y == 7 or y == 8:
        rowY = [6, 7, 8]

    for forX in rowX:
        for forY in rowY:
            if array[forX][forY] == variable:
                return False
    else:
        return True


def checkColumn(array, x, y, variable):
    if x == 0 or x == 3 or x == 6:
        columnX = [0, 3, 6]
    elif x == 1 or x == 4 or x == 7:
        columnX = [1, 4, 7]
    elif x == 2 or x == 5 or x == 8:
        columnX = [2, 5, 8]

    if y == 0 or y == 1 or y == 2:
        columnY = [0, 1, 2]
    elif y == 3 or y == 4 or y == 5:
        columnY = [3, 4, 5]
    elif y == 6 or y == 7 or y == 8:
        columnY = [6, 7, 8]

    for forX in columnX:
        for forY in columnY:
            if array[forX][forY] != variable:
                return True
    else:
        return False


def backtrack(array):
    print('Backtrack')
   # try:
    if len(variableArray) != 0:
        lastPosition = variableArray.pop()  # Array contents [x, y, value]
    else:
        print("Sudoku cannot be solved")
    # array[x][y] = 0
    # print(lastPosition[0], ' ', lastPosition[1])
    array[lastPosition[0]][lastPosition[1]] = 0
    # print(lastPosition)
    if lastPosition[2]+1 > 9: # check if can go back further just in case of possible solutions
        print("Exceeds variable size")
        backtrack(array)
    else:
        fillEmptySpace(array, lastPosition[0], lastPosition[1], lastPosition[2]+1)
    # except Exception:
    #     print("Exception Backtrack: ", Exception)


def save(arrayOfValues):
    #try:
    variableArray.append(arrayOfValues)
    print(variableArray)
    #except Exception:
    #    print("Saving Exception ", Exception)


if __name__ == '__main__':
    startTime = time.time()
    # gui.main()
    dataChecker([[9, 0, 0, 8, 0, 1, 0, 7, 5], [1, 0, 0, 0, 9, 0, 0, 8, 4], [0, 0, 2, 0, 0, 0, 0, 0, 0],
                 [4, 3, 0, 5, 1, 8, 0, 9, 6], [0, 2, 0, 7, 0, 0, 4, 1, 0], [5, 6, 1, 4, 0, 9, 3, 0, 0],
                 [0, 0, 0, 0, 6, 0, 7, 0, 2], [0, 7, 0, 0, 3, 1, 5, 4, 0], [0, 0, 0, 0, 5, 0, 6, 0, 3]])

    print(f"{(time.time() - startTime)} Compilation Time")

# 0  1  2| 0  1  2| 0  1  2
# 3  4  5| 3  4  5| 3  4  5
# 6  7  8| 6  7  8| 6  7  8
# ----------------------------
# 0  1  2| 0  1  2| 0  1  2
# 3  4  5| 3  4  5| 3  4  5
# 6  7  8| 6  7  8| 6  7  8
# -----------------------------
# 0  1  2| 0  1  2| 0  1  2
# 3  4  5| 3  4  5| 3  4  5
# 6  7  8| 6  7  8| 6  7  8

# 0  1  2
# 3  4  5
# 6  7  8

# 0  1  2 | 3  4  5 | 6  7  8
# 9  10 11| 12 13 14| 15 16 17
# 18 19 20| 21 22 23| 24 25 26
# ----------------------------
# 27 28 29| 30 31 32| 33 34 35
# 36 37 38| 39 40 41| 42 43 44
# 45 46 47| 48 49 50| 51 52 53
# -----------------------------
# 54 55 56| 57 58 59| 60 61 62
# 63 64 65| 66 67 68| 69 70 71
# 72 73 74| 75 76 77| 78 79 80
