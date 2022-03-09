
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("HELLO GUI")
root.geometry("640x480")  # 가로 * 세로

values = [str(i) + "일" for i in range(1, 32)]  # 1부터 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(
    root, height=10, values=values, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()


Label(root, text="메뉴를 선택하세요").pack()


burger_var = StringVar()  # 버거 바에 인트형으로 값을 저장
btn_burger1 = Radiobutton(root, text="햄버거", value="햄버거", variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value="치즈버거", variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value="치킨버거", variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="메뉴를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(combobox.get())
    print(burger_var.get())  # 햄버거 중 선택된 라디오 항목의 값을 출력
    print(drink_var.get())


btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()
