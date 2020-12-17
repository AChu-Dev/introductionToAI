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

        # self.guiBuilder()


        # Frames, 9x9 grid # 3 values there


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
        # frame0

        field000 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field000.place(x=0, y=0, height=60, width=60)

        field001 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field001.place(x=61, y=0, height=60, width=60)

        field002 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field002.place(x=122, y=0, height=60, width=60)

        field010 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field010.place(x=0, y=61, height=60, width=60)

        field011 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field011.place(x=61, y=61, height=60, width=60)

        field012 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field012.place(x=122, y=61, height=60, width=60)

        field020 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field020.place(x=0, y=122, height=60, width=60)

        field021 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field021.place(x=61, y=122, height=60, width=60)

        field022 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field022.place(x=122, y=122, height=60, width=60)

        field000 = ttk.Entry(frame0, justify=CENTER, font=("Cambria", "32", "bold"))
        field000.place(x=0, y=0, height=60, width=60)

        # frame1

        field100 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field100.place(x=0, y=0, height=60, width=60)

        field101 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field101.place(x=61, y=0, height=60, width=60)

        field102 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field102.place(x=122, y=0, height=60, width=60)

        field110 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field110.place(x=0, y=61, height=60, width=60)

        field111 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field111.place(x=61, y=61, height=60, width=60)

        field112 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field112.place(x=122, y=61, height=60, width=60)

        field120 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field120.place(x=0, y=122, height=60, width=60)

        field121 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field121.place(x=61, y=122, height=60, width=60)

        field122 = ttk.Entry(frame1, justify=CENTER, font=("Cambria", "32", "bold"))
        field122.place(x=122, y=122, height=60, width=60)

        # frame2

        field200 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field200.place(x=0, y=0, height=60, width=60)

        field201 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field201.place(x=61, y=0, height=60, width=60)

        field202 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field202.place(x=122, y=0, height=60, width=60)

        field210 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field210.place(x=0, y=61, height=60, width=60)

        field211 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field211.place(x=61, y=61, height=60, width=60)

        field212 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field212.place(x=122, y=61, height=60, width=60)

        field220 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field220.place(x=0, y=122, height=60, width=60)

        field221 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field221.place(x=61, y=122, height=60, width=60)

        field222 = ttk.Entry(frame2, justify=CENTER, font=("Cambria", "32", "bold"))
        field222.place(x=122, y=122, height=60, width=60)

        # frame3

        field300 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field300.place(x=0, y=0, height=60, width=60)

        field301 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field301.place(x=61, y=0, height=60, width=60)

        field302 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field302.place(x=122, y=0, height=60, width=60)

        field310 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field310.place(x=0, y=61, height=60, width=60)

        field311 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field311.place(x=61, y=61, height=60, width=60)

        field312 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field312.place(x=122, y=61, height=60, width=60)

        field320 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field320.place(x=0, y=122, height=60, width=60)

        field321 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field321.place(x=61, y=122, height=60, width=60)

        field322 = ttk.Entry(frame3, justify=CENTER, font=("Cambria", "32", "bold"))
        field322.place(x=122, y=122, height=60, width=60)

        # frame4

        field400 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field400.place(x=0, y=0, height=60, width=60)

        field401 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field401.place(x=61, y=0, height=60, width=60)

        field402 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field402.place(x=122, y=0, height=60, width=60)

        field410 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field410.place(x=0, y=61, height=60, width=60)

        field411 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field411.place(x=61, y=61, height=60, width=60)

        field412 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field412.place(x=122, y=61, height=60, width=60)

        field420 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field420.place(x=0, y=122, height=60, width=60)

        field421 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field421.place(x=61, y=122, height=60, width=60)

        field422 = ttk.Entry(frame4, justify=CENTER, font=("Cambria", "32", "bold"))
        field422.place(x=122, y=122, height=60, width=60)

        # frame5

        field500 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field500.place(x=0, y=0, height=60, width=60)

        field501 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field501.place(x=61, y=0, height=60, width=60)

        field502 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field502.place(x=122, y=0, height=60, width=60)

        field510 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field510.place(x=0, y=61, height=60, width=60)

        field511 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field511.place(x=61, y=61, height=60, width=60)

        field512 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field512.place(x=122, y=61, height=60, width=60)

        field520 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field520.place(x=0, y=122, height=60, width=60)

        field521 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field521.place(x=61, y=122, height=60, width=60)

        field522 = ttk.Entry(frame5, justify=CENTER, font=("Cambria", "32", "bold"))
        field522.place(x=122, y=122, height=60, width=60)

        # frame6

        field600 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field600.place(x=0, y=0, height=60, width=60)

        field601 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field601.place(x=61, y=0, height=60, width=60)

        field602 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field602.place(x=122, y=0, height=60, width=60)

        field610 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field610.place(x=0, y=61, height=60, width=60)

        field611 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field611.place(x=61, y=61, height=60, width=60)

        field612 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field612.place(x=122, y=61, height=60, width=60)

        field620 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field620.place(x=0, y=122, height=60, width=60)

        field621 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field621.place(x=61, y=122, height=60, width=60)

        field622 = ttk.Entry(frame6, justify=CENTER, font=("Cambria", "32", "bold"))
        field622.place(x=122, y=122, height=60, width=60)

        # frame7

        field700 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field700.place(x=0, y=0, height=60, width=60)

        field701 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field701.place(x=61, y=0, height=60, width=60)

        field702 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field702.place(x=122, y=0, height=60, width=60)

        field710 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field710.place(x=0, y=61, height=60, width=60)

        field711 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field711.place(x=61, y=61, height=60, width=60)

        field712 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field712.place(x=122, y=61, height=60, width=60)

        field720 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field720.place(x=0, y=122, height=60, width=60)

        field721 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field721.place(x=61, y=122, height=60, width=60)

        field722 = ttk.Entry(frame7, justify=CENTER, font=("Cambria", "32", "bold"))
        field722.place(x=122, y=122, height=60, width=60)

        # frame8

        field800 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field800.place(x=0, y=0, height=60, width=60)

        field801 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field801.place(x=61, y=0, height=60, width=60)

        field802 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field802.place(x=122, y=0, height=60, width=60)

        field810 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field810.place(x=0, y=61, height=60, width=60)

        field811 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field811.place(x=61, y=61, height=60, width=60)

        field812 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field812.place(x=122, y=61, height=60, width=60)

        field820 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field820.place(x=0, y=122, height=60, width=60)

        field821 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))
        field821.place(x=61, y=122, height=60, width=60)

        field822 = ttk.Entry(frame8, justify=CENTER, font=("Cambria", "32", "bold"))#, command=lambda: self.entryChecker(field822.getint()))
        field822.place(x=122, y=122, height=60, width=60)

    def entryChecker(self, input=0):
        try:
            print(input)
        except:
            pass

    def loadData(self, data):
        pass
    def updateData(self, x, y, value):
        pass
    def restart(self):
        pass
    def guiBuilder(self):
        frames = []
        fields = []

        frame_value0 = 5
        frame_value1 = 194
        frame_value2 = 383

        field_value0 = 0
        field_value1 = 61
        field_value2 = 122

        for x in range(8):
            frames.append("frames" + str(x))
        for x in range(3):
            for y in range(3):
                fields.append("frame" + str(x) + str(y))



if __name__ == '__main__': # for testing purposes it will stay here
    main()
