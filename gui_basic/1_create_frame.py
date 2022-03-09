from tkinter import *

root = Tk()
root.title("HELLO GUI")
root.geometry("640x480")  # 가로 * 세로
root.geometry("640x480+400+200")  # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False)  # 창 x(너비) y(높이)값 변경 불가

root.mainloop()
