from tkinter import *


########################################################
root = Tk()
root.title("HELLO GUI")
root.geometry("640x480")  # 가로 * 세로
root.geometry("640x480+400+200")  # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False)  # 창 x(너비) y(높이)값 변경 불가
########################################################

label1 = Label(root, text="안녕")
label1.pack()

photo = PhotoImage(file="gui_basic/icon.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="뭐해?")

    global photo2
    photo2 = PhotoImage(file="gui_basic/icon1.png")
    label2.config(image=photo2)


btn = Button(root, text="안녕?", command=change)
btn.pack()

root.mainloop()
