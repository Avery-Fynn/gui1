
import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("HELLO GUI")
root.geometry("640x480")  # 가로 * 세로


# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)
# progressbar.pack()


# def btncmd1():
#     progressbar.stop()


p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):  # 1부터 100까지
        time.sleep(0.01)  # 0.01초 대기

        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())


btn1 = Button(root, text="시작", command=btncmd2)
btn1.pack()


root.mainloop()
