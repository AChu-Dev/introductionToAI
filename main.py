import tensorflow as tf
import gui
import time
import numpy as np
import matplotlib.pyplot as plt
<<<<<<< HEAD

=======
# from pyconstraints import Problem
>>>>>>> 1810bfd48f3d7f98282dc16ac742443d31376e81
from sklearn import linear_model as lm

print('TensorFlow version: ', tf.__version__)


class mainAi:
    def __init__(self):
        data = input('Insert data ')
        self.__aiData = data



    #insertChecker(aiData)
    print(tf.reduce_sum(tf.random.normal([1000, 1000])))

    def findEmptySpace(self, array): # time O(n^2), space O(1), statement to check if still valid,
        # idea 1, pointer checker time: O(n), space O(n)
        # idea 2, recursive check, time O(Log(n)), space O(Log(n))
        for x in range(len(array) - 1):
            for y in range(x+1, len(array)):
                if y == 0:
                    x = input('Insert data for x: ', x, 'y:', y)

    def dataChecker(self, array):
        try:
            leftPointer = 0
            levelPointer = 0
            while levelPointer == 8 and leftPointer == 8:
                if leftPointer == 8:
                    leftPointer = 0
                    levelPointer += 1
                if array[levelPointer][leftPointer] < 0 or array[levelPointer][leftPointer] > 9:
                    return False
            return True
        except NameError:
            return NameError

if __name__ == '__main__':
    startTime = time.time()
    #gui.main()



    print(f"{(time.time() - startTime)} Compilation Time")
