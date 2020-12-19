class Constraints:
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
        verti1 =
        verti2 =
        verti3 =
        verti4 =
        verti5 =
        verti6 =
        verti7 =
        verti8 =
        verti9 =

    array = [4, 9, 2, 3, 5, 7, 8, 1]

