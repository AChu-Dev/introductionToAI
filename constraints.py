# a b c | 0 1 2 | 4 9 2 |
# d e f | 3 4 5 | 3 5 7 |
# g h i | 6 7 8 | 8 1 6 |
# Format| Format| Solutions


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
    


def grid9Constraints(sudoku):
    print("Full 9 * 9 Sudoku Puzzle analysis")
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

    for x in range(1, 10):
        if (checkUniqueRange(
                [sudoku[horiz1], sudoku[horiz2], sudoku[horiz3], sudoku[horiz4], sudoku[horiz5], sudoku[horiz6],
                 sudoku[horiz7], sudoku[horiz8], sudoku[horiz9]]) and checkUniqueRange(
            [sudoku[verti1], sudoku[verti2], sudoku[verti3], sudoku[verti4], sudoku[verti5], sudoku[verti6],
             sudoku[verti7], sudoku[verti8], sudoku[verti9]])):
            print("Passed vertical & horizontal: " + str(counter))
            horiz1 += 9
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
            if (counter == 9):
                print("Sudoku is correct if ignoring Grid Rules which now are being tested\n")
                return True
        else:
            print("Failed Vertical / Horizontal Constraints")
            return False


def mainConstraint(sudoku):
    if len(sudoku) == 81:
        test = grid9Constraints(sudoku)
        if test:
            grid1 = grid3Constraints(
                [sudoku[0], sudoku[1], sudoku[2],
                 sudoku[9], sudoku[10], sudoku[11],
                 sudoku[18], sudoku[19], sudoku[20]])
            grid2 = grid3Constraints(
                [sudoku[3], sudoku[4], sudoku[5],
                 sudoku[12], sudoku[13], sudoku[14],
                 sudoku[21], sudoku[22], sudoku[23]])
            grid3 = grid3Constraints(
                [sudoku[6], sudoku[7], sudoku[8],
                 sudoku[15], sudoku[16], sudoku[17],
                 sudoku[24], sudoku[25], sudoku[26]])
            grid4 = grid3Constraints(
                [sudoku[27], sudoku[28], sudoku[29],
                 sudoku[36], sudoku[37], sudoku[38],
                 sudoku[45], sudoku[46], sudoku[47]])
            grid5 = grid3Constraints(
                [sudoku[30], sudoku[31], sudoku[32],
                 sudoku[39], sudoku[40], sudoku[41],
                 sudoku[48], sudoku[49], sudoku[50]])
            grid6 = grid3Constraints(
                [sudoku[33], sudoku[34], sudoku[35],
                 sudoku[42], sudoku[43], sudoku[44],
                 sudoku[51], sudoku[52], sudoku[53]])
            grid7 = grid3Constraints(
                [sudoku[54], sudoku[55], sudoku[56],
                 sudoku[63], sudoku[64], sudoku[65],
                 sudoku[72], sudoku[73], sudoku[74]])
            grid8 = grid3Constraints(
                [sudoku[57], sudoku[58], sudoku[59],
                 sudoku[66], sudoku[67], sudoku[68],
                 sudoku[75], sudoku[76], sudoku[77]])
            grid9 = grid3Constraints(
                [sudoku[60], sudoku[61], sudoku[62],
                 sudoku[69], sudoku[70], sudoku[71],
                 sudoku[78], sudoku[79], sudoku[80]])

            if test:
                if grid1 and grid2 and grid3 and grid4 and grid5 and grid6 and grid7 and grid8 and grid9:
                    print("Sudoku is correct! Following Both 9*9 Rules and 3*3 Rules")
                    return True
                elif test and not grid1 or not grid2 or not grid3 or not grid4 or not grid5 or not grid6 or not grid7 or not grid8 or not grid9:
                    print("Sudoku is correct! But it only follows the rules for 9*9 Sudoku")
                    return True
                else:
                    print("Sudoku is incorrect...")
                    print("The Overall Sudoku: " + str(test))
                    print("Grid 1: " + str(grid1) + "\n")
                    print("Grid 2: " + str(grid2) + "\n")
                    print("Grid 3: " + str(grid3) + "\n")
                    print("Grid 4: " + str(grid4) + "\n")
                    print("Grid 5: " + str(grid5) + "\n")
                    print("Grid 6: " + str(grid6) + "\n")
                    print("Grid 7: " + str(grid7) + "\n")
                    print("Grid 8: " + str(grid8) + "\n")
                    print("Grid 9: " + str(grid9) + "\n")
                    return False


# Main Below For testing puproses


sudoku = [3, 9, 1, 2, 8, 6, 5, 7, 4,
          4, 8, 7, 3, 5, 9, 1, 2, 6,
          6, 5, 2, 7, 1, 4, 8, 3, 9,
          8, 7, 5, 4, 3, 1, 6, 9, 2,
          2, 1, 3, 9, 6, 7, 4, 8, 5,
          9, 6, 4, 5, 2, 8, 7, 1, 3,
          1, 4, 9, 6, 7, 3, 2, 5, 8,
          5, 3, 8, 1, 4, 2, 9, 6, 7,
          7, 2, 6, 8, 9, 5, 3, 4, 1]


#mainConstraint(sudoku)

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

import numpy as np
# test if a value on a specific place is possible with current data
def possible(sudoku,rov, col, val):
    if sudoku[rov][col] != 0:
        return False #Already filled
    if val in sudoku[rov]:
        return False #Value already in row
    for a in range(9):
        if sudoku[a][col] == val:
            return False #value already in column
    sqrov = int(int(rov) / 3) * 3
    sqcol = int(int(col) / 3) * 3
    for r in range(sqrov, sqrov + 3):
        for c in range(sqcol, sqcol + 3):
            if sudoku[r][c] == val:
                return False #value already in square
    return True  # Value possible

#solve a sudoku if possible, Fill out list
def solve_Sudoku(sudoku):
    for rov in range(0, 9):
        for col in range(0, 9):
            if sudoku[rov][col] == 0:
                for val in range(1, 10):
                    if possible(sudoku,rov, col, val):
                        sudoku[rov][col] = val
                        if solve_Sudoku(sudoku):
                            return True
                        sudoku[rov][col] = 0 #Backtrack
                return False #Solution failed, backtrack for next value
    return True

solve_Sudoku(sudoku)
print(sudoku)

#Converted to numpy array
sudoku = np.array([[0, 0, 2, 0, 1, 5, 0, 7, 8],
                   [1, 8, 0, 0, 6, 3, 4, 0, 0],
                   [0, 0, 4, 0, 2, 0, 5, 6, 1],
                   [0, 9, 6, 0, 0, 7, 0, 3, 0],
                   [0, 1, 0, 3, 0, 6, 0, 0, 5],
                   [0, 0, 3, 2, 0, 4, 0, 9, 6],
                   [0, 3, 0, 0, 0, 0, 0, 0, 0],
                   [6, 4, 9, 8, 3, 0, 2, 0, 7],
                   [0, 0, 7, 0, 0, 0, 0, 1, 0]
                   ])

