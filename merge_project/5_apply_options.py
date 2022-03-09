from asyncio.proactor_events import _ProactorBasePipeTransport
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import filedialog
from PIL import Image
import os

root = Tk()
root.title("HELLO GUI")
root.geometry("500x680")  # 가로 * 세로

# 파일 추가


def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                        filetypes=(
                                            ("PNG 파일", "*.png"), ("모든 파일", "*.*")),
                                        initialdir=r"/Users/gwonminjeong/Desktop")

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

# 저장 경로


def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 동작


def merge_image():

    try:
        # 가로 넓이
        img_width = cmb_width.get()
        if img_width == "원본 유지":
            img_width = -1
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0

        img_format = cmb_format.get().lower()

        # print(list_file.get(0, END))
        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = []
        if img_width > -1:
            image_sizes = [(int(img_width), int(
                img_width * x.size[1] / x.size[0])) for x in images]
        else:
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # #size -> size[0] :width, size[1] : height
        # widths = [x.size[0] for x in images]
        # heights = [x.size[1] for x in images]

        widths, heights = zip(*(image_sizes))

        # print("width : ", widths)
        # print("heights : ", heights)

        max_width, total_height = max(widths), sum(heights)
        # print("max width : ", max_width)
        # print("tatal height : ", total_height)

        # 스케치북 준비
        if img_space > 0:
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new(
            "RGB", (max_width, total_height), (255, 255, 255))
        y_offset = 0
        # for img in images:
        #     result_img.paste(img, (0, y_offset))
        #     y_offset += img.size[1]

        for idx, img in enumerate(images):
            # width 가 원본이 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "merge_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err:  # 예외처리
        msgbox.showerror("에러", err)


# 시작
def start():
    # print("가로 넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    merge_image()

# 저장 경로


def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':  # 사용자가 취소를 누를 때
        print("폴더 선택 취소")
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)


# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5,
                      text="파일 추가", command=add_file)
btn_add_file.pack(side="left")


btn_del_file = Button(file_frame, padx=5, pady=5,
                      text="선택 삭제", command=del_file)
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

btn_dest_path = Button(path_frame, text="찾아보기",
                       width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(fill="x", padx=5, pady=5)

# 1. 가로 넓이 옵션
lb1_width = Label(frame_option, text="가로 넓이", width=7)
lb1_width.pack(side="left")

opt_width = ["원본 유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=7)
cmb_width.current(0)
cmb_width.pack(side="left", pady=5)

# 2. 간격 옵션
lb1_space = Label(frame_option, text="간     격", width=7)
lb1_space.pack(side="left", pady=5)

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=7)
cmb_space.current(0)
cmb_space.pack(side="left", pady=5)

# 3. 파일 포맷 옵션
lb1_format = Label(frame_option, text="포     맷", width=7)
lb1_format.pack(side="left")

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(
    frame_option, state="readonly", values=opt_format, width=7)
cmb_format.current(0)
cmb_format.pack(side="left", pady=10)

# 진행 상황
frame_progress = LabelFrame(root, text="진행 상황")
frame_progress.pack(fill="x", padx=5, pady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=10)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", command=start)
btn_start.pack(side="right")

btn_close = Button(frame_run, padx=5, pady=5,
                   text="닫기", command=root.quit)
btn_close.pack(side="left")


root.resizable(False, False)  # 창 x(너비) y(높이)값 변경 불가
root.mainloop()
