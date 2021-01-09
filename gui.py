from tkinter import *
from tkinter import ttk, messagebox
import solver
fields = []

def main(array=None):
    root = Tk()
    gui = GUI(root)
    fillGui(array)
    root.mainloop()

def clear():
    try:
        for x in fields:
            x.config(state=NORMAL)
            x.delete(0, END)
    except:
        print("Cleaning GUI error")

def fillGui(array=None):
    try:
        if array is None:
            return False
        num = 0
        for x in fields:
            x.insert(0, array[num])
            num += 1
            x.config(state=DISABLED)
    except:
        messagebox.showerror("Error", "Error outputting the data")
        print("Output Gui Error")
def readGui():
    try:
        for x in fields:
            if not x.get():
                x = 0
            inputList.append(x)
        solver.startMain(inputList)
    except:
        messagebox.showerror("Error", "Error, Reading GUI error")
        print("An Error Occured Reading from GUI")

def infoPrompt(text):
    prompt = messagebox.showinfo("Information", text)

class GUI:
    def __init__(self, window=None):

        # Gui window variables
        window.geometry('572x632')
        window.resizable(False, False)
        window.title('Sudoku AI')

        startButton = ttk.Button(window, text="Start", command=lambda: readGui())
        startButton.place(x=143, y=570, height=50, width=143)
        clearButton = ttk.Button(window, text="Clean", command=lambda: clear())
        clearButton.place(x=286, y=570, height=50, width=143)

        for hor in range(9):
            for ver in range(9):
                fields.append("field" + str(hor) + str(ver))
                indent_ver = int(ver/3+1)
                indent_hor = int(hor/3+1)
                fields[-1] = ttk.Entry(window, justify=CENTER)
                fields[-1].place(x=(61*ver+5*indent_ver), y=(61*hor+5*indent_hor), height=60, width=60)

if __name__ == '__main__':  # for testing purposes it will stay here
    main()
