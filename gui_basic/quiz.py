from tkinter import *
import os

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

# 열기, 저장 파일 이름
filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename):  # 파일있으면 true, 없으면 fal 로  리턴
        with open(filename, "r", encoding="utf8") as file:
            text.delete("1.0", END)
            text.insert(END, file.read())


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(text.get("1.0", END))


menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open File", command=open_file)
menu_file.add_separator()
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_edit)

menu_selection = Menu(menu, tearoff=0)
menu.add_cascade(label="Selection", menu=menu_selection)

menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=menu_view)

menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=menu_help)

root.config(menu=menu)


scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True)
scrollbar.config(command=text.yview)

root.mainloop()
