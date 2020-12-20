# a b c | 0 1 2 | 4 9 2 |
# d e f | 3 4 5 | 3 5 7 |
# g h i | 6 7 8 | 8 1 6 |
# Format| Format| Solutions


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
                print("Succeded")
                return True
            else:
                print('Failed due to numbers being out of range or not all numbers being distinct')
                return False
            # print('Failed Test')
            # return False
    else:
        print("Failed due to wrong number count")

        return False


def grid3Constraints(array):
    print("Checking Grid Constraints\n")
    horiz1 = 0
    horiz2 = 1
    horiz3 = 2
    verti1 = 0
    verti2 = 3
    verti3 = 6
    counter = 1
    # Diagonal Constraints dont change so they dont need iteration

    if (array[6] + array[4] + array[2] == 15) and (array[0] + array[4] + array[8] == 15):
        print("Passed Both Diagonal Constraints")
        for x in range(3):
            if (array[horiz1] + array[horiz2] + array[horiz3] == 15) and (
                    array[verti1] + array[verti2] + array[verti3] == 15):
                print("Passed vertical & horizontal: " + str(counter))
                horiz1 += 3
                horiz2 += 3
                horiz3 += 3
                verti1 += 1
                verti2 += 1
                verti3 += 1
                counter += 1
            else:
                print("Failed Test")
                return False
        print("Passed Tests")
        return True

    else:
        print("Failed Test")
        return False


def grid9Constraints(sudoku):
    print("Full Sudoku Puzzle analysis")
    horiz1 = 0
    horiz2 = 1
    horiz3 = 2
    horiz4 = 3
    horiz5 = 4
    horiz6 = 5
    horiz7 = 6
    horiz8 = 7
    horiz9 = 8
    verti1 = 0
    verti2 = 9
    verti3 = 18
    verti4 = 27
    verti5 = 36
    verti6 = 45
    verti7 = 54
    verti8 = 63
    verti9 = 72
    counter = 1

    if (checkUniqueRange(
            [sudoku[72], sudoku[64], sudoku[56], sudoku[48], sudoku[40], sudoku[32], sudoku[24], sudoku[16],
             sudoku[8]]) and checkUniqueRange(
            [sudoku[0], sudoku[10], sudoku[20], sudoku[30], sudoku[40], sudoku[50], sudoku[60], sudoku[70],
             sudoku[80]])):
        print("Diagonal Constraints Passed")
    else:
        print("Failed Diagonal Constraints")
        return False

    for a in range(1, 9):
        if (checkUniqueRange(
                [sudoku[horiz1], sudoku[horiz2], sudoku[horiz3], sudoku[horiz4], sudoku[horiz5], sudoku[horiz6],
                 sudoku[horiz7], sudoku[horiz8], sudoku[horiz9]]) and checkUniqueRange(
                [sudoku[verti1], sudoku[verti2], sudoku[verti3], sudoku[verti4], sudoku[verti5], sudoku[verti6],
                 sudoku[verti7], sudoku[verti8], sudoku[verti9]])):
            print("Passed vertical & horizontal: " + str(counter))
            horiz1 = 0
            horiz2 += 9
            horiz3 += 9
            horiz4 += 9
            horiz5 += 9
            horiz6 += 9
            horiz7 += 9
            horiz8 += 9
            horiz9 += 9
            verti1 += 1
            verti2 += 1
            verti3 += 1
            verti4 += 1
            verti5 += 1
            verti6 += 1
            verti7 += 1
            verti8 += 1
            verti9 += 1
            counter += 1
        else:
            print("Failed Diagonal Constraints")
            return False


array = [4, 9, 2, 3, 5, 7, 8, 1]
sudoku = [5, 3, 2, 9, 8, 6, 7, 4, 1, 2, 8, 7, 2, 1, 5, 3, 6, 9, 6, 9, 1, 4, 3, 7, 5, 8, 2, 3, 2, 6, 1, 7, 4, 1, 8, 9, 6,
          7, 6, 4, 3, 9, 8, 1, 2, 5, 8, 1, 9, 5, 6, 2, 4, 3, 7, 1, 5, 6, 8, 2, 3, 9, 7, 4, 9, 7, 8, 6, 4, 1, 2, 5, 3, 2,
          4, 3, 7, 5, 9, 6, 1, 8]
grid9Constraints(sudoku)