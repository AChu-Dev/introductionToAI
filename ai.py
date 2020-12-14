import tensorflow as tf
import time

print('TensorFlow version: ', tf.__version__)

startTime = time.time()

aiData = input('Insert data ')
#insertChecker(aiData)
print(tf.reduce_sum(tf.random.normal([1000, 1000])))

def findEmptySpace(array): # time Complexity quite high, change it
    for x in aiData:
        for y in aiData:
            if y == 0:
                x = input = ('Insert data for x: ', x, 'y:', y)


def insertChecker(array):
    try:
        leftPointer = 0
        levelPointer = 0
        while levelPointer == 8 and leftPointer == 8:
            if leftPointer == 8:
                leftPointer = 0
                levelPointer += 1
            if array[leftPointer][leftPointer] < 0 or array[leftPointer][leftPointer] > 9:
                return False
        return True
    except NameError:
        return NameError

print(f"{(time.time() - startTime)} Compilation Time")

