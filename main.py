import gui
import time
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import linear_model as lm
import sys


global array

def dataChecker(array):
    global variableArray
    global backtrackArray
    variableArray = []
    backtrackArray = []
    #try:
    for x in range(9):
        if len(array[x]) != 9 or len(array) != 9:
            print("Not sufficient number of arrays")
            break
        for y in range(9):
            if array[x][y] < 0 or array[x][y] > 9:
                print("Values incorrect")
                return False
    else:
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
                print(x, y)
                fillEmptySpace(array, x, y)
    else:
        print(array)
        # z = 0
        # for x in array:
        #     print(array[x])
        #     if z == 2:
        #         z = 0
        #         print("\n")
        #     z += 1


def fillEmptySpace(array, x, y, startPoint=1, endPoint=10):#, value = 0):
    for var in range(startPoint, endPoint):
        if not checkSubGrid(array, x, var) or not checkRow(array, x, y, var) or not checkColumn(array, x, y, var):# or value != 0:
            var += 1
        else:
            array[x][y] = var
            save([x, y, var])
            return True
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

    if y == 0 or y == 3 or y == 6:
        columnY = [0, 3, 6]
    elif y == 1 or y == 4 or y == 7:
        columnY = [1, 4, 7]
    elif y == 2 or y == 5 or y == 8:
        columnY = [2, 5, 8]

    for forX in columnX:
        for forY in columnY:
            if array[forX][forY] != variable:
                return False
    else:
        return True


def backtrack(array):
    print('Backtrack')
    # try:
    if len(variableArray) != 0:
        lastPosition = variableArray.pop()
        backtrackSave([lastPosition[0], lastPosition[1]])
    else:
        return False
    array[lastPosition[0]][lastPosition[1]] = 0
    if lastPosition[2] >= 9:
        backtrack(array)
    else:
        fillEmptySpace(array, lastPosition[0], lastPosition[1], lastPosition[2]+1)

def backtrackSave(arrayOfBacktrackValues):
    backtrackArray.append(arrayOfBacktrackValues)

def backtrackClean():
    for x in range(len(backtrackArray)):
        value = backtrackArray.pop()

        fillEmptySpace(array, value[0], value[1])

def save(arrayOfValues):
    #try:
    variableArray.append(arrayOfValues)
    print(variableArray)
    #except Exception:
    #    print("Saving Exception ", Exception)


def checkUniqueRange(array):
    print("Checking Numbers for being in the correct format\n")
    if (len(array) == 9):
        # print("3 * 3 Sudoku Checker")
        # print(str(array[1]) + "\t" + str(array[2]) + "\t" +  str(array[3]) + "\n")
        # print(str(array[4]) + "\t" + str(array[5]) + "\t" +  str(array[6]) + "\n")
        # print(str(array[7]) + "\t" + str(array[8]) + "\t" +  str(array[9]) + "\n")

        print("array in: " + str(array))
        arrayToSet = set(array)
        print("Set array: " + str(arrayToSet))
        print("length of array: " + str(len(array)))
        print("length of set: " + str(len(arrayToSet)))
        for x in array:
            value = int(x)
            print("value in array: " + str(value))
            if (1 <= value <= 9) and (len(array) == len(arrayToSet)):
                print("Succeded as Numbers are in Range\n")
                return True
            else:
                print('Failed due to numbers being out of range or not all numbers being distinct')
                return False
            # print('Failed Test')
            # return False
    else:
        print("Failed due to wrong number count")

        return False

if __name__ == '__main__':
    startTime = time.time()
    sys.setrecursionlimit(5000)
    # gui.main()
    dataChecker([[0, 9, 4, 8, 1, 2, 3, 0, 0], [0, 3, 0, 7, 0, 0, 1, 9, 0], [1, 0, 0, 0, 9, 6, 0, 0, 0],
                 [0, 3, 0, 0, 0, 8, 0, 0, 6], [9, 0, 4, 6, 1, 3, 2, 0, 0], [6, 0, 0, 0, 4, 9, 0, 0, 1],
                 [4, 0, 3, 5, 0, 0, 0, 6, 0], [5, 0, 0, 0, 2, 0, 0, 0, 8], [0, 0, 8, 7, 0, 0, 4, 1, 5]])
    # dataChecker([[9, 0, 0, 8, 0, 1, 0, 7, 5], [1, 0, 0, 0, 9, 0, 0, 8, 4], [0, 0, 2, 0, 0, 0, 0, 0, 0],
    #              [4, 3, 0, 5, 1, 8, 0, 9, 6], [0, 2, 0, 7, 0, 0, 4, 1, 0], [5, 6, 1, 4, 0, 9, 3, 0, 0],
    #              [0, 0, 0, 0, 6, 0, 7, 0, 2], [0, 7, 0, 0, 3, 1, 5, 4, 0], [0, 0, 0, 0, 5, 0, 6, 0, 3]])

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
