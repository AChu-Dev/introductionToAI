from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    gui = InterfaceGUI(root)
    root.mainloop()


def loadData(data):
    pass


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

    def guiBuilder(self, window):
        frames = []
        fields = []

        # define frame names

        for x in range(9):
            frames.append("frame" + str(x))
            self.field_names(x, fields)

        var_x = 0
        var_y = 0
        for array_num in range(9):
            frames[array_num] = ttk.Frame(window)
            frames[array_num].place(x=(189 * var_x) + 5, y=(189 * var_y) + 5, height=180, width=180)
            self.fields_manager(frames[array_num], fields)
            var_x += 1
            if var_x == 3:
                var_x = 0
                var_y += 1

    def field_names(self, frame_num, fields):
        for x in range(3):
            for y in range(3):
                fields.append("field" + str(frame_num) + str(x) + str(y))

    def fields_manager(self, frame_num, fields):
        var_x = 0
        var_y = 0
        for array_num2 in range(9):
            fields[array_num2] = ttk.Entry(frame_num, justify=CENTER)
            fields[array_num2].place(x=(61 * var_x), y=(61 * var_y), height=60, width=60)
            var_x += 1
            if var_x == 3:
                var_x = 0
                var_y += 1

    def updateData(self, x, y, value):
        pass

    def restart(self):
        pass


if __name__ == '__main__':  # for testing purposes it will stay here
    main()
