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

        # Frames, 9x9 grid
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
        # Text Boxies
        field00 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field00.place(x=0, y=0, height=60, width=60)

        field01 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field01.place(x=61, y=0, height=60, width=60)

        field02 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field02.place(x=122, y=0, height=60, width=60)

        field10 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field10.place(x=0, y=61, height=60, width=60)

        field11 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field11.place(x=61, y=61, height=60, width=60)

        field12 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field12.place(x=122, y=61, height=60, width=60)

        field20 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field20.place(x=0, y=122, height=60, width=60)

        field21 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field21.place(x=61, y=122, height=60, width=60)

        field22 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field22.place(x=122, y=122, height=60, width=60)
        field22.config(state="DISABLED")

    def loadData(self, array):
        pass
    def updateData(self, x, y, value):
        pass
    def restart(self):
        pass


if __name__ == '__main__': # for testing purposes it will stay here
    main()
