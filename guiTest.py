from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    gui = InterfaceGUI(root)
    root.mainloop()


class InterfaceGUI:
    def __init__(self, window=None):

        # Master window variables
        window.geometry('572x572')
        window.resizable(False, False)
        window.title('Sudoku AI')

        # Set Menu Bar
        menuBar = Menu(window)
        window.config(menu=menuBar)

        program = Menu(menuBar)

        menuBar.add_cascade(menu=program, label='Program')

        program.add_command(label='Restart')

        self.guiBuilder(window)
        # frame0 = ttk.Frame(window)
        # frame0.place(x=5, y=5, height=180, width=180)

        # field000 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        # field000.place(x=0, y=0, height=60, width=60)


        # Frames, 9x9 grid # 3 values there

    def entryChecker(self, input=0):
        try:
            print(input)
        except:
            pass

    def loadData(self, data):
        pass

    def updateData(self, x, y, value):
        pass

    def clear(self):
        pass

    def guiBuilder(self, window):
        frames = []
        fields = []
        frame_diff = 189  # dont forget 5 px border
        field_diff = 61

        # define frame names
        for x in range(9):
            frames.append("frame" + str(x))
            self.field_names(x, fields)
        self.field_names(x, fields)
        print(fields)
        varX = 0
        varY = 0
        for array_num in range(9):
            frames[array_num] = ttk.Frame(window)
            frames[array_num].config(height=180, width=180)
            frames[array_num].place(x=(189 * varX) + 5, y=(189 * varY) + 5)
            print(frames[array_num], ' ', varX, ' varX ', varY, ' varY')
            varX += 1
            if varX == 3:
                varX = 0
                varY += 1

    def field_names(self, frame_num, fields):
        left_pointer = 0
        level_pointer = 0
        while left_pointer == 2 and level_pointer == 2:
            fields.append("field" + str(frame_num) + str(level_pointer) + str(left_pointer))
            left_pointer += 1
            if left_pointer == 2:
                left_pointer = 0
                level_pointer += 1
        # for x in range(3):
        #    for y in range(3):
        #        fields.append("frame" + str(x) + str(y))

        # frame0 = ttk.Frame(window)
        # frame0.config(height=180, width=180)
        # frame0.place(x=5, y=5)
        # for z in range(len(frames)):
        #    frames[z] = ttk.Frame(window)
        #    frames[z].config(height=180, width=180)
        # if list(frames[z])[5]:
        #    frames[z].place(x=frame_value0+z*10, y=frame_value0+z*10)
    def object_placement(self, varX, varY, varHeight, varWidth, window, **kwargs):
        pass



if __name__ == '__main__':  # for testing purposes it will stay here
    main()
