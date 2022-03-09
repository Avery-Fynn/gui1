from tkinter import *

root = Tk()  # root = 메인 윈도우
root.title("HELLO GUI")
root.geometry("640x480")  # 가로 * 세로
root.geometry("640x480+400+200")  # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False)  # 창 x(너비) y(높이)값 변경 불가

btn1 = Button(root, text="버튼1")
btn1.pack()


#padx, pady = 여백
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=15, text="버튼3")
btn3.pack()

#width = 버튼크기
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="black", text="버튼5")
btn5.pack()

photo = PhotoImage(file="gui_basic/icon.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("메롱")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
