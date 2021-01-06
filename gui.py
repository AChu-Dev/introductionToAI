from tkinter import *
from tkinter import ttk, filedialog
import time

def main():
    root = Tk()
    gui = GUI(root)
    root.mainloop()

def open_file():
    filename = filedialog.askopenfile(title="Select a File", filetypes=(
        ("Text File", "*.txt"), ("Csv File", "*.csv"), ("Excel", "*.xlsx"), ("JSON File", "*.json")))

def clear():
    pass

class GUI:
    def __init__(self, window=None):

        # Gui window variables
        window.geometry('572x572')
        window.resizable(False, False)
        window.title('Sudoku AI')

        fields = []

        for hor in range(9):
            for ver in range(9):
                fields.append("field" + str(hor) + str(ver))
                indent_ver = int(ver/3+1)
                indent_hor = int(hor/3+1)
                fields[-1] = ttk.Entry(window, justify=CENTER)
                fields[-1].place(x=(61*ver+5*indent_ver), y=(61*hor+5*indent_hor), height=60, width=60)

if __name__ == '__main__':  # for testing purposes it will stay here
    main()
