from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("HELLO GUI")

# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, text="파일 추가")
btn_add_file.pack(side="left")


btn_del_file = Button(file_frame, padx=5, pady=5, text="선택 삭제")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)


scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(fill="x", padx=5, pady=5)

# 1. 가로 넓이 옵션
lb1_width = Label(frame_option, text="가로 넓이", width=8)
lb1_width.pack()


opt_width = ["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width)
cmb_width.current(0)
cmb_width.pack(fill="x", padx=5)


# 2. 간격 옵션

lb1_space = Label(frame_option, text="간격", width=8)
lb1_space.pack()


opt_width = ["없음", "좁게", "보통", "넓게"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width)
cmb_width.current(0)
cmb_width.pack(fill="x", padx=5)


# 3. 파일 포맷 옵션
lb1_format = Label(frame_option, text="포맷", width=8)
lb1_format.pack()


opt_format = ["PNG", "JPG", "800", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_width)
cmb_format.current(0)
cmb_format.pack(fill="x", padx=5, pady=5)

# 진행 상황
frame_progress = LabelFrame(root, text="진행 상황")
frame_progress.pack(fill="x", padx=5, pady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)


btn_start = Button(frame_run, padx=5, pady=5, text="시작")
btn_start.pack(side="left")


btn_close = Button(frame_run, padx=5, pady=5,
                   text="닫기", command=root.quit)
btn_close.pack(side="right")


root.resizable(False, False)  # 창 x(너비) y(높이)값 변경 불가
root.mainloop()
