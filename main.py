import tensorflow as tf
import gui
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model as lm

print('TensorFlow version: ', tf.__version__)


class mainAi:
    def __init__(self):
        data = input('Insert data ')
        self.__aiData = data



    #insertChecker(aiData)
    print(tf.reduce_sum(tf.random.normal([1000, 1000])))


    def dataChecker(self, array):
        pass
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

    def findEmptySpace(self, array): # time O(n^2), space O(1), statement to check if still valid,
        # idea 1, pointer checker time: O(n), space O(n)
        # idea 2, recursive check, time O(Log(n)), space O(Log(n))
        for x in range(len(array) - 1):
            for y in range(x+1, len(array)):
                if y == 0:
                  self.fillEmptySpace(array[x][y])

    def fillEmptySpace(self, emptySpace):
        variables = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while self.checkColumn() and self.checkRow() and self.checkSubGrid():
            pass
        # for x in variables:
        #     emptySpace = x
        #     if not self.checkSubGrid():
        #         x += 1
        #     elif not self.checkRow():
        #         x += 1
        #     elif not self.checkColumn():
        #         x += 1

    def checkSubGrid(self, array, subArray, variable):
        for x in range(9):
            if array[subArray][x] == variable:
                return False
        else:
            return True

    def checkRow(self, array, subArray, variable):
        row = 0
        if array == 0 or array == 1 or array == 2:
            pass
        elif array == 3 or array == 4 or array == 5:
            pass
        elif array == 6 or array == 7 or array == 8:
            pass

    def checkColumn(self, array, subArray, variable):
        if array == 0 or array == 3 or array == 6:
            pass
        elif array == 1 or array == 4 or array == 7:
            pass
        elif array == 2 or array == 5 or array == 8:
            pass


if __name__ == '__main__':
    startTime = time.time()
    gui.main()

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
