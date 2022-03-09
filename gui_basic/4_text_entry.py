from tkinter import *

root = Tk()
root.title("HELLO GUI")
root.geometry("640x480")  # 가로 * 세로
root.geometry("640x480+400+200")  # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False)  # 창 x(너비) y(높이)값 변경 불가

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "아이디 : ")


def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1: 첫번째 라인, 0:0번째 column위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
