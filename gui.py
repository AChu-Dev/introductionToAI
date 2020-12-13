from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    gui = GUI(root)
    root.mainloop()

class GUI:
    def __init__(self, window=None):

        # Master window variables
        window.geometry('1280x720')
        window.resizable(False, False)
        window.title('Sudoku AI')
        











if __name__ == "__main__": main()