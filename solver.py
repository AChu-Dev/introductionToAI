import numpy



def sudokuSolver(array):
    # try:
    for x in range(len(array)):
        for y in range(len(array[x])):
            if array[x][y] == 0:
                for value in range(1, 10):
                    if checkValues(array, x, y, value):
                        array[x][y] = value
<<<<<<< HEAD
                        # backtracking
            if grid3Constraints(x):
                print("Grid Follows 3*3 Sudoku Rules")
            else:
                print("Grid Does Not Follow 3*3 Sudoku Rules")
=======
                        # backtracking needed
>>>>>>> 259c1b91a9fd5beae800ab75ec0fba16ea0567a0
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

    def grid3Constraints(array):
        print("Checking 3 *3 Grid Constraints\n")
        print(str(array[0]) + "\t" + str(array[1]) + "\t" +  str(array[2]) + "\n")
        print(str(array[3]) + "\t" + str(array[4]) + "\t" +  str(array[5]) + "\n")
        print(str(array[6]) + "\t" + str(array[7]) + "\t" +  str(array[8]) + "\n")
        horiz1 = 0
        horiz2 = 1
        horiz3 = 2
        verti1 = 0
        verti2 = 3
        verti3 = 6
        counter = 1
        if checkUniqueRange(array) == False:
            return False
        else:
            # Diagonal Constraints dont change so they dont need iteration
            if (array[6] + array[4] + array[2] == 15) and (array[0] + array[4] + array[8] == 15):
                print("Passed Both Diagonal Constraints")
                for x in range(3):
                    if (array[horiz1] + array[horiz2] + array[horiz3] == 15) and (
                            array[verti1] + array[verti2] + array[verti3] == 15):
                        print("Passed vertical & horizontal test: " + str(counter))
                        horiz1 += 3
                        horiz2 += 3
                        horiz3 += 3
                        verti1 += 1
                        verti2 += 1
                        verti3 += 1
                        counter += 1
                    else:
                        print("Failed on Horizontal/Vertical: " + str(counter))
                        return False
                print("Passed Tests")
                return True

            else:
                print("Numbers in Diagonals do not add up to 15")
                return False

def checkUniqueRange(array):
    print("Checking Numbers for being in the correct format\n")
    if (len(array) == 9):
        
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
