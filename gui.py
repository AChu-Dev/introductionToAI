from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    gui = GUI(root)
    root.mainloop()

class GUI:
    def __init__(self, window=None):

        # Master window variables
        window.geometry('577x577')
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
        frame0.place(x=3, y=3)

        frame1 = ttk.Frame(window)
        frame1.config(height=180, width=180)
        frame1.place(x=187, y=3)

    def loadData(self, array):
        pass
    def updateData(self, x, y, value):
        pass
    def restart(self):
        pass
    









if __name__ == "__main__": main()