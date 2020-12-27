import tensorflow as tf
import gui
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model as lm

print('TensorFlow version: ', tf.__version__)



def dataChecker(array):
    try:
        for x in range(9):
            if len(array[x]) != 9:
                print("Not sufficent number of arrays")
                break
            for y in range(9):
                if array[x][y] < 0 or array[x][y] > 9:
                    print("Values incorrect")
                    break
        else:
            findEmptySpace(array)
    except Exception:
        print("Exception has occured:")
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
                print(array[x][y], x, y)
                fillEmptySpace(array, x, y)
    else:
        print(array)

def fillEmptySpace(array, x, y):
    variables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for var in variables:
        if not checkSubGrid(array, x, var) or not checkRow(array, x, var) or not checkColumn(array, x, var):
            var += 1
        elif var == 9:
            backtrack()
        array[x][y] = var

def checkSubGrid(array, subArray, variable):
    for x in range(9):
        if array[subArray][x] == variable:
            return False
    else:
        return True

def checkRow(array, subArray, variable):
    row = 0
    if array == 0 or array == 1 or array == 2:
        pass
    elif array == 3 or array == 4 or array == 5:
        pass
    elif array == 6 or array == 7 or array == 8:
        pass

def checkColumn(array, subArray, variable):
    if array == 0 or array == 3 or array == 6:
        pass
    elif array == 1 or array == 4 or array == 7:
        pass
    elif array == 2 or array == 5 or array == 8:
        pass

def backtrack():
    pass

if __name__ == '__main__':
    startTime = time.time()
    # gui.main()
    dataChecker([[9, 0, 0, 8, 0, 1, 0, 7, 5], [1, 0, 0, 0, 9, 0, 0, 8, 4], [0, 0, 2, 0, 0, 0, 0, 0, 0],
                [4, 3, 0, 5, 1, 8, 0, 9, 6], [0, 2, 0, 7, 0, 0, 4, 1, 0], [5, 6, 1, 4, 0, 9, 3, 0, 0],
                [0, 0, 0, 0, 6, 0, 7, 0, 2], [0, 7, 0, 0, 3, 1, 5, 4, 0], [0, 0 ,0, 0, 5, 0, 6, 0, 3]])

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
