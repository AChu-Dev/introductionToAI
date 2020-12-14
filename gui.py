from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    gui = GUI(root)
    root.mainloop()

class GUI:
    def __init__(self, window=None):

        # Master window variables
        window.geometry('572x572')
        window.resizable(False, False)
        window.title('Sudoku AI')

        # Set Menu Bar
        menuBar = Menu(window)
        window.config(menu = menuBar)

        program = Menu(menuBar)

        menuBar.add_cascade(menu=program, label='Program')

        program.add_command(label='Restart')

        # Frames
        frame0 = ttk.Frame(window)
        frame0.config(height=180, width=180)
        frame0.place(x=5, y=5)

        frame1 = ttk.Frame(window)
        frame1.config(height=180, width=180)
        frame1.place(x=194, y=5)

        frame2 = ttk.Frame(window)
        frame2.config(height=180, width=180)
        frame2.place(x=383, y=5)

        frame3 = ttk.Frame(window)
        frame3.config(height=180, width=180)
        frame3.place(x=5, y=194)

        frame4 = ttk.Frame(window)
        frame4.config(height=180, width=180)
        frame4.place(x=194, y=194)

        frame5 = ttk.Frame(window)
        frame5.config(height=180, width=180)
        frame5.place(x=383, y=194)

        frame6 = ttk.Frame(window)
        frame6.config(height=180, width=180)
        frame6.place(x=5, y=383)

        frame7 = ttk.Frame(window)
        frame7.config(height=180, width=180)
        frame7.place(x=194, y=383)

        frame8 = ttk.Frame(window)
        frame8.config(height=180, width=180)
        frame8.place(x=383, y=383)

    def loadData(self, array):
        pass
    def updateData(self, x, y, value):
        pass
    def restart(self):
        pass










if __name__ == "__main__": main()